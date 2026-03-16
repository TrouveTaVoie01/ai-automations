#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projet 2 — Document Extractor
Application Streamlit qui détecte le type de document (facture, CV, contrat)
et extrait les données clés via Claude AI.
"""

import streamlit as st
import pandas as pd
import anthropic
import plotly.express as px
import json
import time
import os

# --- Configuration ---
st.set_page_config(
    page_title="Document Extractor AI",
    page_icon="📄",
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
    .doc-type-facture { border-left: 4px solid #e67e22; padding-left: 1rem; }
    .doc-type-cv { border-left: 4px solid #3498db; padding-left: 1rem; }
    .doc-type-contrat { border-left: 4px solid #2ecc71; padding-left: 1rem; }
</style>
""", unsafe_allow_html=True)

# --- Types de documents ---
DOC_TYPES = {
    "Facture": {"couleur": "#e67e22", "icone": "🧾"},
    "CV": {"couleur": "#3498db", "icone": "👤"},
    "Contrat": {"couleur": "#2ecc71", "icone": "📝"},
}

# --- Sidebar ---
with st.sidebar:
    st.title("Configuration")
    api_key = st.text_input("Clé API Anthropic", type="password", value="")
    modele = st.selectbox("Modèle Claude", [
        "claude-sonnet-4-20250514",
        "claude-haiku-4-5-20251001",
    ])
    st.divider()
    st.markdown("### Types détectés")
    for doc_type, info in DOC_TYPES.items():
        st.markdown(f"{info['icone']} **{doc_type}**")
    st.divider()
    st.markdown("### Données extraites")
    st.markdown("""
    **Facture** : fournisseur, date, montant HT, TVA, TTC

    **CV** : nom, email, compétences, expériences

    **Contrat** : parties, objet, durée, conditions
    """)
    st.caption("Propulsé par Claude AI")


def extraire_document(texte, api_key, modele):
    """Détecte le type et extrait les données clés via Claude."""
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""Analyse ce document et réponds UNIQUEMENT avec un JSON valide (pas de markdown, pas de ```).

Document :
---
{texte}
---

Étape 1 : Détecte le type parmi : Facture, CV, Contrat
Étape 2 : Extrais les données clés selon le type

Si Facture, retourne :
{{"type": "Facture", "confiance": 0.95, "donnees": {{"fournisseur": "...", "date": "...", "numero_facture": "...", "montant_ht": "...", "tva": "...", "montant_ttc": "...", "description": "..."}}}}

Si CV, retourne :
{{"type": "CV", "confiance": 0.95, "donnees": {{"nom": "...", "email": "...", "telephone": "...", "competences": ["...", "..."], "experiences": ["...", "..."], "formation": "..."}}}}

Si Contrat, retourne :
{{"type": "Contrat", "confiance": 0.95, "donnees": {{"parties": ["...", "..."], "objet": "...", "duree": "...", "date_signature": "...", "conditions_particulieres": "..."}}}}"""

    message = client.messages.create(
        model=modele,
        max_tokens=800,
        messages=[{"role": "user", "content": prompt}]
    )

    reponse = message.content[0].text.strip()
    if reponse.startswith("```"):
        reponse = reponse.split("\n", 1)[1]
        if reponse.endswith("```"):
            reponse = reponse[:-3]
        reponse = reponse.strip()

    return json.loads(reponse)


def afficher_resultat_document(resultat):
    """Affiche les données extraites selon le type."""
    doc_type = resultat["type"]
    info = DOC_TYPES.get(doc_type, {"icone": "📄", "couleur": "#999"})
    donnees = resultat["donnees"]

    st.markdown(f"### {info['icone']} Type détecté : **{doc_type}** (confiance : {resultat['confiance']*100:.0f}%)")

    if doc_type == "Facture":
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Fournisseur", donnees.get("fournisseur", "N/A"))
            st.metric("Date", donnees.get("date", "N/A"))
            st.metric("N° Facture", donnees.get("numero_facture", "N/A"))
        with col2:
            st.metric("Montant HT", donnees.get("montant_ht", "N/A"))
            st.metric("TVA", donnees.get("tva", "N/A"))
            st.metric("Montant TTC", donnees.get("montant_ttc", "N/A"))
        if donnees.get("description"):
            st.info(f"**Description :** {donnees['description']}")

    elif doc_type == "CV":
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Nom", donnees.get("nom", "N/A"))
            st.metric("Email", donnees.get("email", "N/A"))
            st.metric("Téléphone", donnees.get("telephone", "N/A"))
        with col2:
            st.metric("Formation", donnees.get("formation", "N/A"))
        st.markdown("**Compétences :**")
        competences = donnees.get("competences", [])
        if competences:
            cols = st.columns(min(len(competences), 4))
            for i, comp in enumerate(competences):
                with cols[i % 4]:
                    st.success(comp)
        st.markdown("**Expériences :**")
        for exp in donnees.get("experiences", []):
            st.markdown(f"- {exp}")

    elif doc_type == "Contrat":
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Objet", donnees.get("objet", "N/A"))
            st.metric("Durée", donnees.get("duree", "N/A"))
        with col2:
            st.metric("Date signature", donnees.get("date_signature", "N/A"))
        st.markdown("**Parties :**")
        for partie in donnees.get("parties", []):
            st.markdown(f"- {partie}")
        if donnees.get("conditions_particulieres"):
            st.info(f"**Conditions particulières :** {donnees['conditions_particulieres']}")


# --- En-tête ---
st.markdown('<p class="main-header">📄 Document Extractor AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Détection automatique et extraction de données depuis vos documents</p>', unsafe_allow_html=True)

# --- Onglets ---
tab1, tab2, tab3 = st.tabs(["📄 Document unique", "📊 Mode Batch", "📈 Dashboard"])

if "resultats_batch_doc" not in st.session_state:
    st.session_state.resultats_batch_doc = None
if "resultat_unique_doc" not in st.session_state:
    st.session_state.resultat_unique_doc = None

# === ONGLET 1 : Document unique ===
with tab1:
    st.subheader("Analyser un document")

    upload_mode = st.radio("Mode d'entrée :", ["Coller le texte", "Uploader un fichier .txt"], horizontal=True)

    doc_text = ""
    if upload_mode == "Coller le texte":
        doc_text = st.text_area(
            "Collez le contenu du document ici :",
            height=300,
            placeholder="FACTURE N° FAC-2024-0891\nFournisseur : TechSolutions SAS..."
        )
    else:
        uploaded = st.file_uploader("Choisir un fichier .txt", type=["txt"])
        if uploaded:
            doc_text = uploaded.read().decode("utf-8")
            st.text_area("Contenu du fichier :", value=doc_text, height=200, disabled=True)

    btn = st.button("🔍 Analyser le document", type="primary")

    if btn:
        if not api_key:
            st.error("Entrez votre clé API Anthropic dans la sidebar.")
        elif not doc_text.strip():
            st.warning("Fournissez un document avant d'analyser.")
        else:
            with st.spinner("Analyse en cours..."):
                start = time.time()
                try:
                    resultat = extraire_document(doc_text, api_key, modele)
                    duree = time.time() - start
                    st.session_state.resultat_unique_doc = {**resultat, "duree": duree}
                except Exception as e:
                    st.error(f"Erreur : {e}")

    if st.session_state.resultat_unique_doc:
        r = st.session_state.resultat_unique_doc
        st.divider()
        st.metric("Temps d'analyse", f"{r['duree']:.1f}s")
        afficher_resultat_document(r)


# === ONGLET 2 : Mode Batch ===
with tab2:
    st.subheader("Traitement par lot")
    st.info("Uploadez plusieurs fichiers .txt (factures, CV, contrats)")

    uploaded_files = st.file_uploader(
        "Choisir des fichiers .txt",
        type=["txt"],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.write(f"**{len(uploaded_files)} fichier(s) détecté(s)**")
        for f in uploaded_files:
            st.markdown(f"- `{f.name}`")

        btn_batch = st.button("🚀 Analyser tous les documents", type="primary")

        if btn_batch:
            if not api_key:
                st.error("Entrez votre clé API Anthropic dans la sidebar.")
            else:
                resultats = []
                progress = st.progress(0, text="Analyse en cours...")
                start_total = time.time()

                for i, fichier in enumerate(uploaded_files):
                    texte = fichier.read().decode("utf-8")
                    try:
                        r = extraire_document(texte, api_key, modele)
                        donnees = r["donnees"]
                        ligne = {
                            "fichier": fichier.name,
                            "type": r["type"],
                            "confiance": r["confiance"],
                        }
                        # Aplatir les données clés
                        for cle, val in donnees.items():
                            if isinstance(val, list):
                                ligne[cle] = ", ".join(val)
                            else:
                                ligne[cle] = val
                        resultats.append(ligne)
                    except Exception as e:
                        resultats.append({
                            "fichier": fichier.name,
                            "type": "Erreur",
                            "confiance": 0,
                            "erreur": str(e)
                        })
                    progress.progress((i + 1) / len(uploaded_files), text=f"Document {i+1}/{len(uploaded_files)}")

                duree_total = time.time() - start_total
                progress.empty()

                df_resultats = pd.DataFrame(resultats)
                st.session_state.resultats_batch_doc = df_resultats
                st.session_state.duree_batch_doc = duree_total

                st.success(f"**{len(uploaded_files)} documents analysés en {duree_total:.1f}s**")

    if st.session_state.resultats_batch_doc is not None:
        df_r = st.session_state.resultats_batch_doc
        st.dataframe(df_r, use_container_width=True, height=400)

        csv_output = df_r.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Télécharger les résultats (CSV)",
            data=csv_output,
            file_name="documents_extraits.csv",
            mime="text/csv"
        )


# === ONGLET 3 : Dashboard ===
with tab3:
    st.subheader("Tableau de bord")

    if st.session_state.resultats_batch_doc is not None:
        df_r = st.session_state.resultats_batch_doc

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total documents", len(df_r))
        with col2:
            confiance_moy = df_r["confiance"].mean()
            st.metric("Confiance moyenne", f"{confiance_moy*100:.0f}%")
        with col3:
            duree = st.session_state.get("duree_batch_doc", 0)
            st.metric("Temps total", f"{duree:.1f}s")

        st.divider()

        col_chart1, col_chart2 = st.columns(2)

        with col_chart1:
            st.markdown("#### Répartition par type")
            type_counts = df_r["type"].value_counts()
            fig = px.pie(
                values=type_counts.values,
                names=type_counts.index,
                color=type_counts.index,
                color_discrete_map={
                    t: info["couleur"] for t, info in DOC_TYPES.items()
                },
                hole=0.4
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

        with col_chart2:
            st.markdown("#### Confiance par type")
            conf_by_type = df_r.groupby("type")["confiance"].mean().reset_index()
            fig2 = px.bar(
                conf_by_type,
                x="type",
                y="confiance",
                color="type",
                color_discrete_map={
                    t: info["couleur"] for t, info in DOC_TYPES.items()
                },
                labels={"confiance": "Confiance moyenne", "type": "Type"}
            )
            fig2.update_layout(height=400, showlegend=False)
            fig2.update_yaxes(range=[0, 1])
            st.plotly_chart(fig2, use_container_width=True)

        st.divider()
        st.markdown("#### Détail par type")
        for doc_type in df_r["type"].unique():
            info = DOC_TYPES.get(doc_type, {"icone": "📄", "couleur": "#999"})
            nb = len(df_r[df_r["type"] == doc_type])
            with st.expander(f"{info['icone']} {doc_type} — {nb} document(s)"):
                st.dataframe(
                    df_r[df_r["type"] == doc_type],
                    use_container_width=True
                )
    else:
        st.info("Lancez un traitement batch pour voir le dashboard.")
