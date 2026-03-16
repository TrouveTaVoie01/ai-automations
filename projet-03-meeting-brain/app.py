#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projet 3 — Meeting Brain
Application Streamlit qui analyse des transcripts de réunion via Claude AI.
Génère : résumé, décisions, actions, points en suspens. Export PDF.
"""

import streamlit as st
import pandas as pd
import anthropic
import json
import time
import io
from fpdf import FPDF

# --- Configuration ---
st.set_page_config(
    page_title="Meeting Brain AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A5F;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .decision-card {
        background: #f0f7ff;
        border-left: 4px solid #3498db;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
        border-radius: 4px;
    }
    .action-card {
        background: #f0fff4;
        border-left: 4px solid #2ecc71;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
        border-radius: 4px;
    }
    .pending-card {
        background: #fff8f0;
        border-left: 4px solid #e67e22;
        padding: 0.8rem 1rem;
        margin: 0.5rem 0;
        border-radius: 4px;
    }
</style>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.title("Configuration")
    api_key = st.text_input("Clé API Anthropic", type="password", value="")
    modele = st.selectbox("Modèle Claude", [
        "claude-sonnet-4-20250514",
        "claude-haiku-4-5-20251001",
    ])
    st.divider()
    st.markdown("### Ce que Meeting Brain extrait")
    st.markdown("""
    - **Résumé exécutif** (5 lignes max)
    - **Décisions prises**
    - **Actions** (qui, quoi, deadline)
    - **Points en suspens**
    """)
    st.caption("Propulsé par Claude AI")


def analyser_reunion(transcript, api_key, modele):
    """Analyse un transcript de réunion via Claude."""
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""Analyse ce transcript de réunion et réponds UNIQUEMENT avec un JSON valide (pas de markdown, pas de ```).

Transcript :
---
{transcript}
---

Retourne ce JSON exact :
{{
  "resume_executif": "Résumé de la réunion en 5 lignes maximum, en français",
  "decisions": [
    {{"decision": "Description de la décision", "contexte": "Pourquoi cette décision"}}
  ],
  "actions": [
    {{"action": "Description de l'action", "responsable": "Nom de la personne", "deadline": "Date ou délai", "priorite": "Haute|Moyenne|Basse"}}
  ],
  "points_en_suspens": [
    {{"point": "Description du point", "raison": "Pourquoi c'est en suspens"}}
  ],
  "participants": ["Nom1", "Nom2"],
  "duree_estimee": "Durée estimée de la réunion",
  "sujet_principal": "Le sujet principal en une phrase"
}}

Règles :
- resume_executif : 5 lignes max, en français, factuel
- decisions : toutes les décisions prises pendant la réunion
- actions : chaque action avec responsable et deadline
- points_en_suspens : tout ce qui n'a pas été tranché
- Si une info n'est pas dans le transcript, mets "Non spécifié"
"""

    message = client.messages.create(
        model=modele,
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}]
    )

    reponse = message.content[0].text.strip()
    if reponse.startswith("```"):
        reponse = reponse.split("\n", 1)[1]
        if reponse.endswith("```"):
            reponse = reponse[:-3]
        reponse = reponse.strip()

    return json.loads(reponse)


def generer_pdf(resultat):
    """Génère un PDF du compte-rendu de réunion."""
    pdf = FPDF()
    pdf.add_page()

    # Police Unicode
    pdf.add_font("DejaVu", "", "C:/Windows/Fonts/arial.ttf")
    pdf.add_font("DejaVu", "B", "C:/Windows/Fonts/arialbd.ttf")

    # Titre
    pdf.set_font("DejaVu", "B", 18)
    pdf.cell(0, 15, "Compte-rendu de réunion", new_x="LMARGIN", new_y="NEXT", align="C")
    pdf.ln(5)

    # Sujet et participants
    pdf.set_font("DejaVu", "B", 12)
    pdf.cell(0, 8, f"Sujet : {resultat.get('sujet_principal', 'N/A')}", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DejaVu", "", 10)
    participants = ", ".join(resultat.get("participants", []))
    pdf.cell(0, 8, f"Participants : {participants}", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 8, f"Durée estimée : {resultat.get('duree_estimee', 'N/A')}", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(5)

    # Résumé
    pdf.set_font("DejaVu", "B", 14)
    pdf.cell(0, 10, "Résumé exécutif", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DejaVu", "", 10)
    pdf.multi_cell(0, 6, resultat.get("resume_executif", "N/A"))
    pdf.ln(5)

    # Décisions
    pdf.set_font("DejaVu", "B", 14)
    pdf.cell(0, 10, "Décisions prises", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DejaVu", "", 10)
    for i, d in enumerate(resultat.get("decisions", []), 1):
        pdf.multi_cell(0, 6, f"{i}. {d['decision']}")
        if d.get("contexte"):
            pdf.set_font("DejaVu", "", 9)
            pdf.multi_cell(0, 5, f"   Contexte : {d['contexte']}")
            pdf.set_font("DejaVu", "", 10)
        pdf.ln(2)
    pdf.ln(3)

    # Actions
    pdf.set_font("DejaVu", "B", 14)
    pdf.cell(0, 10, "Plan d'action", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DejaVu", "", 10)
    for i, a in enumerate(resultat.get("actions", []), 1):
        pdf.multi_cell(0, 6, f"{i}. {a['action']}")
        pdf.set_font("DejaVu", "", 9)
        pdf.multi_cell(0, 5, f"   Responsable : {a['responsable']} | Deadline : {a['deadline']} | Priorité : {a['priorite']}")
        pdf.set_font("DejaVu", "", 10)
        pdf.ln(2)
    pdf.ln(3)

    # Points en suspens
    pdf.set_font("DejaVu", "B", 14)
    pdf.cell(0, 10, "Points en suspens", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("DejaVu", "", 10)
    for i, p in enumerate(resultat.get("points_en_suspens", []), 1):
        pdf.multi_cell(0, 6, f"{i}. {p['point']}")
        if p.get("raison"):
            pdf.set_font("DejaVu", "", 9)
            pdf.multi_cell(0, 5, f"   Raison : {p['raison']}")
            pdf.set_font("DejaVu", "", 10)
        pdf.ln(2)

    # Footer
    pdf.ln(10)
    pdf.set_font("DejaVu", "", 8)
    pdf.cell(0, 5, "Généré automatiquement par Meeting Brain AI", align="C")

    return pdf.output()


# --- En-tête ---
st.markdown('<p class="main-header">🧠 Meeting Brain AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Transformez vos réunions en actions concrètes grâce à l\'IA</p>', unsafe_allow_html=True)

# --- Onglets ---
tab1, tab2 = st.tabs(["📝 Analyser un transcript", "📋 Suivi des tâches"])

if "resultat_reunion" not in st.session_state:
    st.session_state.resultat_reunion = None
if "taches" not in st.session_state:
    st.session_state.taches = []

# === EXEMPLES DE TRANSCRIPTS ===
EXEMPLE_TRANSCRIPT = """Réunion : Lancement du projet e-commerce
Date : 12 mars 2024
Participants : Sarah (Chef de projet), Marc (Développeur), Julie (Design), Thomas (Marketing)

Sarah : Bonjour à tous, merci d'être là. On est réunis pour lancer officiellement le projet de refonte de notre site e-commerce. L'objectif est d'augmenter le taux de conversion de 2,1% à 3,5% d'ici septembre.

Marc : J'ai fait un audit technique du site actuel. Le temps de chargement est de 4,2 secondes en moyenne. C'est beaucoup trop. Je recommande de passer sur Next.js avec un CDN Cloudflare.

Sarah : OK, on valide la migration technique vers Next.js. Marc, tu peux me faire un planning détaillé pour vendredi ?

Marc : Oui, je m'en occupe. Par contre, il faut qu'on tranche sur l'hébergement. On reste chez OVH ou on passe sur Vercel ?

Julie : Côté design, j'ai préparé 3 maquettes pour la nouvelle page d'accueil. Je les présente la semaine prochaine. Je pense qu'on devrait faire des tests utilisateurs avant de valider.

Sarah : Très bien. On planifie les tests utilisateurs pour fin mars. Julie, tu peux contacter notre panel de testeurs ?

Thomas : Pour le marketing, je propose de préparer une campagne de lancement avec 3 phases : teasing, lancement, et rétention. Budget estimé : 15 000 euros.

Sarah : Le budget marketing de 15 000 euros est validé. Thomas, prépare-moi le plan détaillé des 3 phases pour mercredi prochain.

Marc : Il y a un point important : on n'a pas encore décidé si on intègre le paiement en 3 fois. Ça demande un développement supplémentaire de 2 semaines.

Sarah : On ne tranche pas aujourd'hui sur le paiement en 3 fois. Marc, fais-moi une estimation du coût et du ROI attendu pour la prochaine réunion.

Thomas : Et pour les réseaux sociaux, on crée un compte TikTok ou pas ?

Sarah : On reporte la décision TikTok à la prochaine réunion aussi. Thomas, fais une analyse rapide des concurrents sur TikTok.

Sarah : OK, pour résumer : Marc fait le planning technique pour vendredi, Julie prépare les tests utilisateurs pour fin mars, Thomas fait le plan marketing pour mercredi. Prochaine réunion mardi prochain à 14h. Merci à tous !"""


# === ONGLET 1 : Analyser ===
with tab1:
    st.subheader("Analyser un transcript de réunion")

    col_input, col_example = st.columns([4, 1])
    with col_example:
        st.write("")
        st.write("")
        use_example = st.button("Charger un exemple")

    transcript = st.text_area(
        "Collez le transcript de votre réunion ici :",
        height=350,
        value=EXEMPLE_TRANSCRIPT if use_example else "",
        placeholder="Réunion du 12 mars 2024\nParticipants : ...\n\nAlice : Bonjour à tous..."
    )

    btn = st.button("🧠 Analyser la réunion", type="primary")

    if btn:
        if not api_key:
            st.error("Entrez votre clé API Anthropic dans la sidebar.")
        elif not transcript.strip():
            st.warning("Collez un transcript avant d'analyser.")
        else:
            with st.spinner("Analyse en cours..."):
                start = time.time()
                try:
                    resultat = analyser_reunion(transcript, api_key, modele)
                    duree = time.time() - start
                    st.session_state.resultat_reunion = {**resultat, "duree": duree}
                    # Ajouter les actions au suivi de tâches
                    for action in resultat.get("actions", []):
                        st.session_state.taches.append({
                            **action,
                            "statut": "A faire"
                        })
                except Exception as e:
                    st.error(f"Erreur : {e}")

    if st.session_state.resultat_reunion:
        r = st.session_state.resultat_reunion
        st.divider()

        # Métriques
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Temps d'analyse", f"{r['duree']:.1f}s")
        with col2:
            st.metric("Décisions", len(r.get("decisions", [])))
        with col3:
            st.metric("Actions", len(r.get("actions", [])))
        with col4:
            st.metric("Points en suspens", len(r.get("points_en_suspens", [])))

        # Sujet et participants
        st.markdown(f"**Sujet :** {r.get('sujet_principal', 'N/A')}")
        st.markdown(f"**Participants :** {', '.join(r.get('participants', []))}")
        st.markdown(f"**Durée estimée :** {r.get('duree_estimee', 'N/A')}")

        st.divider()

        # Résumé exécutif
        st.markdown("### Résumé exécutif")
        st.info(r.get("resume_executif", "N/A"))

        # Décisions
        st.markdown("### Décisions prises")
        for d in r.get("decisions", []):
            st.markdown(f"""<div class="decision-card">
                <strong>{d['decision']}</strong><br>
                <small>{d.get('contexte', '')}</small>
            </div>""", unsafe_allow_html=True)

        # Actions
        st.markdown("### Plan d'action")
        if r.get("actions"):
            df_actions = pd.DataFrame(r["actions"])
            st.dataframe(df_actions, use_container_width=True)

        # Points en suspens
        st.markdown("### Points en suspens")
        for p in r.get("points_en_suspens", []):
            st.markdown(f"""<div class="pending-card">
                <strong>{p['point']}</strong><br>
                <small>{p.get('raison', '')}</small>
            </div>""", unsafe_allow_html=True)

        # Export PDF
        st.divider()
        st.markdown("### Exporter le compte-rendu")
        try:
            pdf_bytes = generer_pdf(r)
            st.download_button(
                "📥 Télécharger le PDF",
                data=pdf_bytes,
                file_name="compte_rendu_reunion.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.warning(f"Export PDF indisponible : {e}")

        # Vue JSON brute
        with st.expander("Voir les données brutes (JSON)"):
            st.json(r)


# === ONGLET 2 : Suivi des tâches ===
with tab2:
    st.subheader("Suivi des tâches")

    if st.session_state.taches:
        for i, tache in enumerate(st.session_state.taches):
            col1, col2, col3, col4 = st.columns([3, 2, 2, 2])
            with col1:
                st.markdown(f"**{tache['action']}**")
            with col2:
                st.markdown(f"Resp: {tache['responsable']}")
            with col3:
                st.markdown(f"Deadline: {tache['deadline']}")
            with col4:
                nouveau_statut = st.selectbox(
                    "Statut",
                    ["A faire", "En cours", "Fait"],
                    index=["A faire", "En cours", "Fait"].index(tache["statut"]),
                    key=f"statut_{i}"
                )
                st.session_state.taches[i]["statut"] = nouveau_statut

        st.divider()

        # Métriques de suivi
        col1, col2, col3 = st.columns(3)
        total = len(st.session_state.taches)
        fait = sum(1 for t in st.session_state.taches if t["statut"] == "Fait")
        en_cours = sum(1 for t in st.session_state.taches if t["statut"] == "En cours")
        a_faire = sum(1 for t in st.session_state.taches if t["statut"] == "A faire")

        with col1:
            st.metric("A faire", a_faire)
        with col2:
            st.metric("En cours", en_cours)
        with col3:
            st.metric("Fait", fait)

        if total > 0:
            st.progress(fait / total, text=f"Progression : {fait}/{total} ({fait/total*100:.0f}%)")

        # Reset
        if st.button("Effacer toutes les tâches"):
            st.session_state.taches = []
            st.rerun()
    else:
        st.info("Analysez un transcript de réunion pour remplir le suivi des tâches.")
