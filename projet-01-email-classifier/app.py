#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Projet 1 — Email Classifier
Application Streamlit qui classifie automatiquement les emails
en catégories via l'API Claude, avec mode batch et dashboard.
"""

import streamlit as st
import pandas as pd
import anthropic
import plotly.express as px
import json
import time
import io

# --- Configuration de la page ---
st.set_page_config(
    page_title="Email Classifier AI",
    page_icon="📧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Styles CSS personnalisés ---
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
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 12px;
        color: white;
        text-align: center;
    }
    .category-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        font-weight: 600;
        font-size: 0.9rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        padding: 10px 20px;
        border-radius: 8px;
    }
</style>
""", unsafe_allow_html=True)

# --- Catégories et couleurs ---
CATEGORIES = {
    "Support": {"couleur": "#3498db", "icone": "🔧"},
    "Commercial": {"couleur": "#2ecc71", "icone": "💰"},
    "Facturation": {"couleur": "#e67e22", "icone": "🧾"},
    "RH": {"couleur": "#9b59b6", "icone": "👥"},
    "Spam": {"couleur": "#e74c3c", "icone": "🚫"},
    "Urgent": {"couleur": "#c0392b", "icone": "🚨"},
}

# --- Sidebar ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/email-open.png", width=80)
    st.title("Configuration")
    api_key = st.text_input("Clé API Anthropic", type="password", value="")
    modele = st.selectbox("Modèle Claude", [
        "claude-sonnet-4-20250514",
        "claude-haiku-4-5-20251001",
    ])
    st.divider()
    st.markdown("### Catégories")
    for cat, info in CATEGORIES.items():
        st.markdown(f"{info['icone']} **{cat}**")
    st.divider()
    st.caption("Propulsé par Claude AI")


def classifier_email(email_text, api_key, modele):
    """Classifie un email via l'API Claude."""
    client = anthropic.Anthropic(api_key=api_key)

    prompt = f"""Analyse cet email et réponds UNIQUEMENT avec un JSON valide (pas de markdown, pas de ```).

Email :
---
{email_text}
---

Réponds avec ce format JSON exact :
{{"categorie": "Support|Commercial|Facturation|RH|Spam|Urgent", "confiance": 0.95, "raison": "explication courte en français", "brouillon_reponse": "brouillon de réponse professionnelle en français"}}

Règles :
- categorie : exactement une parmi Support, Commercial, Facturation, RH, Spam, Urgent
- confiance : nombre entre 0 et 1
- raison : 1-2 phrases maximum
- brouillon_reponse : réponse professionnelle et courtoise, 2-4 phrases"""

    message = client.messages.create(
        model=modele,
        max_tokens=500,
        messages=[{"role": "user", "content": prompt}]
    )

    reponse = message.content[0].text.strip()
    # Nettoyer si Claude envoie du markdown
    if reponse.startswith("```"):
        reponse = reponse.split("\n", 1)[1]
        if reponse.endswith("```"):
            reponse = reponse[:-3]
        reponse = reponse.strip()

    return json.loads(reponse)


# --- En-tête ---
st.markdown('<p class="main-header">📧 Email Classifier AI</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Classification automatique des emails par intelligence artificielle</p>', unsafe_allow_html=True)

# --- Onglets ---
tab1, tab2, tab3 = st.tabs(["✉️ Email unique", "📊 Mode Batch", "📈 Dashboard"])

# --- Stockage session ---
if "resultats_batch" not in st.session_state:
    st.session_state.resultats_batch = None
if "resultat_unique" not in st.session_state:
    st.session_state.resultat_unique = None

# === ONGLET 1 : Email unique ===
with tab1:
    st.subheader("Classifier un email")

    EXEMPLE_EMAIL = "Bonjour,\n\nJe n'arrive plus à me connecter à mon compte depuis ce matin. J'ai essayé de réinitialiser mon mot de passe 3 fois mais je ne reçois aucun email de confirmation.\n\nMon identifiant est marie.dupont@entreprise.fr et c'est assez urgent car j'ai des documents importants à récupérer pour une réunion cet après-midi.\n\nMerci de votre aide rapide.\n\nCordialement,\nMarie Dupont"

    col_input, col_example = st.columns([4, 1])
    with col_example:
        st.write("")
        st.write("")
        use_example = st.button("Charger un exemple")

    with col_input:
        email_input = st.text_area(
            "Collez le contenu de l'email ici :",
            height=200,
            value=EXEMPLE_EMAIL if use_example else "",
            placeholder="Bonjour, je n'arrive pas à accéder à mon compte depuis ce matin..."
        )

    col_btn, col_info = st.columns([1, 3])
    with col_btn:
        btn_classifier = st.button("🔍 Classifier", type="primary", use_container_width=True)

    if btn_classifier:
        if not api_key:
            st.error("Entrez votre clé API Anthropic dans la sidebar.")
        elif not email_input.strip():
            st.warning("Collez un email avant de classifier.")
        else:
            with st.spinner("Analyse en cours..."):
                start = time.time()
                try:
                    resultat = classifier_email(email_input, api_key, modele)
                    duree = time.time() - start
                    st.session_state.resultat_unique = {**resultat, "duree": duree}
                except Exception as e:
                    st.error(f"Erreur : {e}")

    if st.session_state.resultat_unique:
        r = st.session_state.resultat_unique
        cat_info = CATEGORIES.get(r["categorie"], {"couleur": "#999", "icone": "❓"})

        st.divider()
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Catégorie", f"{cat_info['icone']} {r['categorie']}")
        with col2:
            st.metric("Confiance", f"{r['confiance']*100:.0f}%")
        with col3:
            st.metric("Temps", f"{r['duree']:.1f}s")

        st.markdown(f"**Raison :** {r['raison']}")

        with st.expander("📝 Brouillon de réponse suggéré", expanded=True):
            st.text_area("", value=r["brouillon_reponse"], height=120, key="brouillon")


# === ONGLET 2 : Mode Batch ===
with tab2:
    st.subheader("Traitement par lot")
    st.info("Uploadez un CSV avec une colonne **email** contenant le texte des emails.")

    uploaded_file = st.file_uploader("Choisir un fichier CSV", type=["csv"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
        except Exception as e:
            st.error(f"Erreur de lecture CSV : {e}")
            df = None

        if df is not None:
            # Chercher la colonne email
            col_email = None
            for col in df.columns:
                if "email" in col.lower() or "contenu" in col.lower() or "texte" in col.lower():
                    col_email = col
                    break
            if col_email is None:
                col_email = df.columns[0]

            st.write(f"**{len(df)} emails détectés** (colonne : `{col_email}`)")
            st.dataframe(df[[col_email]].head(5), use_container_width=True)

            btn_batch = st.button("🚀 Classifier tout le lot", type="primary")

            if btn_batch:
                if not api_key:
                    st.error("Entrez votre clé API Anthropic dans la sidebar.")
                else:
                    resultats = []
                    progress = st.progress(0, text="Classification en cours...")
                    start_total = time.time()

                    for i, row in df.iterrows():
                        email_text = str(row[col_email])
                        try:
                            r = classifier_email(email_text, api_key, modele)
                            resultats.append({
                                "email": email_text[:100] + "..." if len(email_text) > 100 else email_text,
                                "categorie": r["categorie"],
                                "confiance": r["confiance"],
                                "raison": r["raison"],
                                "brouillon": r["brouillon_reponse"]
                            })
                        except Exception as e:
                            resultats.append({
                                "email": email_text[:100] + "...",
                                "categorie": "Erreur",
                                "confiance": 0,
                                "raison": str(e),
                                "brouillon": ""
                            })
                        progress.progress((i + 1) / len(df), text=f"Email {i+1}/{len(df)}")

                    duree_total = time.time() - start_total
                    progress.empty()

                    df_resultats = pd.DataFrame(resultats)
                    st.session_state.resultats_batch = df_resultats
                    st.session_state.duree_batch = duree_total

                    st.success(f"✅ {len(df)} emails classifiés en {duree_total:.1f}s")

    if st.session_state.resultats_batch is not None:
        df_r = st.session_state.resultats_batch
        st.dataframe(df_r, use_container_width=True, height=400)

        # Export CSV
        csv_output = df_r.to_csv(index=False).encode("utf-8")
        st.download_button(
            "📥 Télécharger les résultats (CSV)",
            data=csv_output,
            file_name="emails_classifies.csv",
            mime="text/csv"
        )


# === ONGLET 3 : Dashboard ===
with tab3:
    st.subheader("Tableau de bord")

    if st.session_state.resultats_batch is not None:
        df_r = st.session_state.resultats_batch

        # Métriques
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total emails", len(df_r))
        with col2:
            nb_urgents = len(df_r[df_r["categorie"] == "Urgent"])
            st.metric("Urgents", nb_urgents)
        with col3:
            confiance_moy = df_r["confiance"].mean()
            st.metric("Confiance moyenne", f"{confiance_moy*100:.0f}%")
        with col4:
            duree = st.session_state.get("duree_batch", 0)
            st.metric("Temps total", f"{duree:.1f}s")

        st.divider()

        col_chart1, col_chart2 = st.columns(2)

        # Camembert des catégories
        with col_chart1:
            st.markdown("#### Répartition par catégorie")
            cat_counts = df_r["categorie"].value_counts()
            fig = px.pie(
                values=cat_counts.values,
                names=cat_counts.index,
                color=cat_counts.index,
                color_discrete_map={
                    cat: info["couleur"] for cat, info in CATEGORIES.items()
                },
                hole=0.4
            )
            fig.update_layout(height=400)
            st.plotly_chart(fig, use_container_width=True)

        # Barres de confiance
        with col_chart2:
            st.markdown("#### Confiance par catégorie")
            conf_by_cat = df_r.groupby("categorie")["confiance"].mean().reset_index()
            fig2 = px.bar(
                conf_by_cat,
                x="categorie",
                y="confiance",
                color="categorie",
                color_discrete_map={
                    cat: info["couleur"] for cat, info in CATEGORIES.items()
                },
                labels={"confiance": "Confiance moyenne", "categorie": "Catégorie"}
            )
            fig2.update_layout(height=400, showlegend=False)
            fig2.update_yaxes(range=[0, 1])
            st.plotly_chart(fig2, use_container_width=True)

        # Détail par catégorie
        st.divider()
        st.markdown("#### Détail par catégorie")
        for cat in df_r["categorie"].unique():
            info = CATEGORIES.get(cat, {"icone": "❓", "couleur": "#999"})
            nb = len(df_r[df_r["categorie"] == cat])
            with st.expander(f"{info['icone']} {cat} — {nb} email(s)"):
                st.dataframe(
                    df_r[df_r["categorie"] == cat][["email", "confiance", "raison"]],
                    use_container_width=True
                )
    else:
        st.info("Lancez un traitement batch pour voir le dashboard.")
