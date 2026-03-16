# Stack Technique — AI Automations

## Langage
- **Python 3.14** — Langage principal pour toutes les applications et scripts

## IA & NLP
- **Claude API (Anthropic)** — Moteur d'intelligence artificielle pour la classification, l'extraction, l'analyse et la qualification
- **Modèles utilisés** : claude-sonnet-4-20250514 (principal), claude-haiku-4-5-20251001 (rapide)

## Frontend & Interface
- **Streamlit** — Framework Python pour créer des interfaces web interactives sans HTML/CSS/JS
- **CSS personnalisé** — Styles injectés dans Streamlit pour un design professionnel

## Visualisation
- **Plotly** — Graphiques interactifs (camemberts, histogrammes, barres)
- **Streamlit metrics** — Métriques clés affichées en cards

## Données
- **Pandas** — Manipulation de DataFrames, lecture/écriture CSV, agrégations
- **CSV** — Format d'échange pour les données de démo et les exports

## Génération de documents
- **fpdf2** — Génération de PDF (comptes-rendus de réunion)

## Automatisation
- **N8N** — Plateforme d'automatisation de workflows (self-hosted)
- **Webhooks** — Points d'entrée pour recevoir des données
- **Google Sheets** — Stockage et logging des résultats
- **Email** — Notifications et alertes automatiques

## Infrastructure
- **Git & GitHub** — Versioning et hébergement du code
- **Windows 11** — Environnement de développement
- **RTX 4050** — GPU disponible pour du traitement local si nécessaire

## Architecture des projets
Chaque projet suit la même structure :
1. **app.py** — Application Streamlit (interface utilisateur)
2. **workflow_n8n.json** — Workflow d'automatisation exportable
3. **Données de démo** — Datasets réalistes pour tester
4. **requirements.txt** — Dépendances Python
5. **README.md** — Documentation avec résultats chiffrés
