#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projet 4 — Lead Qualifier
Application Streamlit qui analyse et qualifie des leads commerciaux
via Claude AI avec scoring, catégorisation et réponse personnalisée.
"""

import streamlit as st
import pandas as pd
import anthropic
import plotly.express as px
import json
import time

# --- Configuration ---
st.set_page_config(
    page_title="Lead Qualifier AI",
    page_icon="🎯",
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
    .lead-hot {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        text-align: center;
        font-weight: 700;
    }
    .lead-warm {
        background: linear-gradient(135deg, #ffa502, #e67e22);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        text-align: center;
        font-weight: 700;
    }
    .lead-cold {
        background: linear-gradient(135deg, #74b9ff, #3498db);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        text-align: center;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

LEAD_CATEGORIES = {
    "Hot": {"couleur": "#ee5a24", "icone": "🔥"},
    "Warm": {"couleur": "#e67e22", "icone": "☀️"},
    "Cold": {"couleur": "#3498db", "icone": "❄️"},
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
    st.markdown("### Critères de scoring")
    st.markdown("""
    **Hot (8-10)** : Budget confirmé, besoin immédiat, décideur

    **Warm (5-7)** : Intérêt réel, en phase d'exploration

    **Cold (1-4)** : Simple curiosité, pas de budget, timing flou
    """)
    st.caption("Propulsé par Claude AI")


def qualifier_lead(nom_entreprise, email_contact, message_lead, api_key, modele):
    """Qualifie un lead via Claude."""
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""Analyse ce lead commercial et réponds UNIQUEMENT avec un JSON valide (pas de markdown, pas de ```).

Lead :
- Entreprise : {nom_entreprise}
- Email contact : {email_contact}
- Message du lead : {message_lead}

Retourne ce JSON exact :
{{
  "score": 8,
  "categorie": "Hot",
  "raison_score": "Explication du score en 2-3 phrases",
  "signaux_positifs": ["signal 1", "signal 2"],
  "signaux_negatifs": ["signal 1"],
  "taille_entreprise_estimee": "PME / ETI / Grande entreprise / Startup / Indéterminé",
  "urgence": "Haute / Moyenne / Basse",
  "budget_estime": "Estimation ou 'Non mentionné'",
  "reponse_personnalisee": "Réponse professionnelle et personnalisée de 3-5 phrases en français, adaptée au niveau d'intérêt du lead"
}}

Règles :
- score : nombre entier de 1 à 10
- categorie : Hot (8-10), Warm (5-7), Cold (1-4)
- Sois réaliste et pragmatique dans ton évaluation
- La réponse personnalisée doit être actionnable et professionnelle"""

    message = client.messages.create(
        model=modele,
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}]
    )

    reponse = message.content[0].text.strip()
    if reponse.startswith("```"):
        reponse = reponse.split("\n", 1)[1]
        if reponse.endswith("```"):
            reponse = reponse[:-3]
        reponse = reponse.strip()

    return json.loads(reponse)


# --- En-tête ---
st.markdown('<p class="main-header">🎯 Lead Qualifier AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Qualifiez vos leads commerciaux automatiquement par IA</p>', unsafe_allow_html=True)

# --- Onglets ---
tab1, tab2, tab3 = st.tabs(["🎯 Lead unique", "📊 Mode Batch", "📈 Dashboard"])

if "resultats_batch_lead" not in st.session_state:
    st.session_state.resultats_batch_lead = None
if "resultat_unique_lead" not in st.session_state:
    st.session_state.resultat_unique_lead = None

# === ONGLET 1 : Lead unique ===
with tab1:
    st.subheader("Qualifier un lead")

    col1, col2 = st.columns(2)
    with col1:
        nom_entreprise = st.text_input("Nom de l'entreprise", placeholder="TechCorp SAS")
        email_contact = st.text_input("Email du contact", placeholder="pierre.martin@techcorp.fr")
    with col2:
        message_lead = st.text_area(
            "Message du lead",
            height=130,
            placeholder="Bonjour, nous cherchons une solution d'automatisation pour notre service client de 50 personnes..."
        )

    col_btn, col_example = st.columns([1, 1])
    with col_btn:
        btn_qualifier = st.button("🎯 Qualifier", type="primary", use_container_width=True)
    with col_example:
        use_example = st.button("Charger un exemple", use_container_width=True)

    if use_example:
        st.session_state["_example"] = True
        st.rerun()

    if st.session_state.get("_example"):
        nom_entreprise = "DataFlow Industries"
        email_contact = "sophie.durand@dataflow.fr"
        message_lead = "Bonjour, nous sommes une PME de 120 personnes dans la logistique. Nous cherchons une solution d'automatisation IA pour traiter nos 500 emails de support quotidiens. Nous avons un budget de 2000 EUR/mois et souhaitons démarrer avant fin avril. Pouvez-vous organiser une démo cette semaine ?"
        st.session_state["_example"] = False

    if btn_qualifier:
        if not api_key:
            st.error("Entrez votre clé API Anthropic dans la sidebar.")
        elif not nom_entreprise or not message_lead:
            st.warning("Remplissez au moins le nom et le message du lead.")
        else:
            with st.spinner("Qualification en cours..."):
                start = time.time()
                try:
                    resultat = qualifier_lead(nom_entreprise, email_contact, message_lead, api_key, modele)
                    duree = time.time() - start
                    st.session_state.resultat_unique_lead = {**resultat, "duree": duree}
                except Exception as e:
                    st.error(f"Erreur : {e}")

    if st.session_state.resultat_unique_lead:
        r = st.session_state.resultat_unique_lead
        cat_info = LEAD_CATEGORIES.get(r["categorie"], {"couleur": "#999", "icone": "❓"})

        st.divider()

        # Score et catégorie
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Score", f"{r['score']}/10")
        with col2:
            st.markdown(f'<div class="lead-{r["categorie"].lower()}">{cat_info["icone"]} {r["categorie"]}</div>', unsafe_allow_html=True)
        with col3:
            st.metric("Urgence", r.get("urgence", "N/A"))
        with col4:
            st.metric("Temps", f"{r['duree']:.1f}s")

        st.markdown(f"**Raison du score :** {r['raison_score']}")
        st.markdown(f"**Taille estimée :** {r.get('taille_entreprise_estimee', 'N/A')}")
        st.markdown(f"**Budget estimé :** {r.get('budget_estime', 'N/A')}")

        col_pos, col_neg = st.columns(2)
        with col_pos:
            st.markdown("**Signaux positifs**")
            for s in r.get("signaux_positifs", []):
                st.success(f"+ {s}")
        with col_neg:
            st.markdown("**Signaux négatifs**")
            for s in r.get("signaux_negatifs", []):
                st.error(f"- {s}")

        with st.expander("📧 Réponse personnalisée suggérée", expanded=True):
            st.text_area("", value=r.get("reponse_personnalisee", ""), height=120, key="reponse_lead")

        with st.expander("Données brutes (JSON)"):
            st.json(r)


# === ONGLET 2 : Mode Batch ===
with tab2:
    st.subheader("Qualification par lot")
    st.info("Uploadez un CSV avec les colonnes **entreprise**, **email**, **message**")

    uploaded_file = st.file_uploader("Choisir un fichier CSV", type=["csv"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"Erreur : {e}")
            df = None

        if df is not None:
            # Détecter les colonnes
            col_map = {}
            for col in df.columns:
                cl = col.lower()
                if "entreprise" in cl or "company" in cl or "nom" in cl:
                    col_map["entreprise"] = col
                elif "email" in cl:
                    col_map["email"] = col
                elif "message" in cl or "contenu" in cl or "texte" in cl:
                    col_map["message"] = col

            if len(col_map) < 2:
                col_map = {"entreprise": df.columns[0], "email": df.columns[1] if len(df.columns) > 1 else df.columns[0], "message": df.columns[2] if len(df.columns) > 2 else df.columns[0]}

            st.write(f"**{len(df)} leads détectés**")
            st.dataframe(df.head(5), use_container_width=True)

            btn_batch = st.button("🚀 Qualifier tout le lot", type="primary")

            if btn_batch:
                if not api_key:
                    st.error("Entrez votre clé API Anthropic dans la sidebar.")
                else:
                    resultats = []
                    progress = st.progress(0, text="Qualification en cours...")
                    start_total = time.time()

                    for i, row in df.iterrows():
                        entreprise = str(row.get(col_map.get("entreprise", ""), ""))
                        email = str(row.get(col_map.get("email", ""), ""))
                        message = str(row.get(col_map.get("message", ""), ""))

                        try:
                            r = qualifier_lead(entreprise, email, message, api_key, modele)
                            resultats.append({
                                "entreprise": entreprise,
                                "email": email,
                                "score": r["score"],
                                "categorie": r["categorie"],
                                "urgence": r.get("urgence", ""),
                                "raison": r["raison_score"],
                                "reponse": r.get("reponse_personnalisee", "")
                            })
                        except Exception as e:
                            resultats.append({
                                "entreprise": entreprise,
                                "email": email,
                                "score": 0,
                                "categorie": "Erreur",
                                "urgence": "",
                                "raison": str(e),
                                "reponse": ""
                            })
                        progress.progress((i + 1) / len(df), text=f"Lead {i+1}/{len(df)}")

                    duree_total = time.time() - start_total
                    progress.empty()

                    df_resultats = pd.DataFrame(resultats)
                    # Trier par score décroissant
                    df_resultats = df_resultats.sort_values("score", ascending=False).reset_index(drop=True)
                    st.session_state.resultats_batch_lead = df_resultats
                    st.session_state.duree_batch_lead = duree_total

                    st.success(f"**{len(df)} leads qualifiés en {duree_total:.1f}s**")

    if st.session_state.resultats_batch_lead is not None:
        df_r = st.session_state.resultats_batch_lead
        st.dataframe(df_r, use_container_width=True, height=400)

        csv_output = df_r.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Télécharger les résultats (CSV)",
            data=csv_output,
            file_name="leads_qualifies.csv",
            mime="text/csv"
        )


# === ONGLET 3 : Dashboard ===
with tab3:
    st.subheader("Tableau de bord")

    if st.session_state.resultats_batch_lead is not None:
        df_r = st.session_state.resultats_batch_lead

        # Métriques
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.metric("Total leads", len(df_r))
        with col2:
            nb_hot = len(df_r[df_r["categorie"] == "Hot"])
            st.metric("🔥 Hot", nb_hot)
        with col3:
            nb_warm = len(df_r[df_r["categorie"] == "Warm"])
            st.metric("☀️ Warm", nb_warm)
        with col4:
            nb_cold = len(df_r[df_r["categorie"] == "Cold"])
            st.metric("❄️ Cold", nb_cold)
        with col5:
            score_moy = df_r["score"].mean()
            st.metric("Score moyen", f"{score_moy:.1f}/10")

        st.divider()

        col_chart1, col_chart2 = st.columns(2)

        with col_chart1:
            st.markdown("#### Répartition Hot / Warm / Cold")
            cat_counts = df_r["categorie"].value_counts()
            fig = px.pie(
                values=cat_counts.values,
                names=cat_counts.index,
                color=cat_counts.index,
                color_discrete_map={
                    cat: info["couleur"] for cat, info in LEAD_CATEGORIES.items()
                },
                hole=0.4
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

        with col_chart2:
            st.markdown("#### Distribution des scores")
            fig2 = px.histogram(
                df_r,
                x="score",
                nbins=10,
                color="categorie",
                color_discrete_map={
                    cat: info["couleur"] for cat, info in LEAD_CATEGORIES.items()
                },
                labels={"score": "Score", "count": "Nombre de leads"}
            )
            fig2.update_layout(height=400)
            fig2.update_xaxes(range=[0, 11])
            st.plotly_chart(fig2, use_container_width=True)

        # Top leads
        st.divider()
        st.markdown("#### Top 10 leads prioritaires")
        top10 = df_r.head(10)[["entreprise", "score", "categorie", "urgence", "raison"]]
        st.dataframe(top10, use_container_width=True)

        # Détail par catégorie
        st.markdown("#### Détail par catégorie")
        for cat in ["Hot", "Warm", "Cold"]:
            info = LEAD_CATEGORIES.get(cat, {"icone": "❓"})
            nb = len(df_r[df_r["categorie"] == cat])
            if nb > 0:
                with st.expander(f"{info['icone']} {cat} — {nb} lead(s)"):
                    st.dataframe(
                        df_r[df_r["categorie"] == cat][["entreprise", "score", "raison"]],
                        use_container_width=True
                    )
    else:
        st.info("Lancez un traitement batch pour voir le dashboard.")
