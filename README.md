# 🤖 AI Automations — Portfolio d'un AI Automation Specialist

> 4 projets d'automatisation IA complets, testables et documentés.
> Chaque projet inclut une app Streamlit, un workflow N8N et des données de démo.

---

## Les projets

### 📧 [Projet 1 — Email Classifier AI](./projet-01-email-classifier/)
**Classification automatique d'emails par IA en 6 catégories.**
- 50 emails classifiés en ~45s | Précision ~94% | Détection des urgences
- Mode batch + dashboard interactif + brouillon de réponse
- Workflow N8N : webhook → Claude → alerte urgent → Google Sheet

### 📄 [Projet 2 — Document Extractor AI](./projet-02-document-extractor/)
**Détection et extraction automatique de données depuis factures, CV et contrats.**
- 15 documents analysés en ~20s | Précision type ~97%
- Extraction structurée selon le type de document
- Workflow N8N : watch folder → Claude → Google Sheet → notification

### 🧠 [Projet 3 — Meeting Brain AI](./projet-03-meeting-brain/)
**Transforme vos transcripts de réunion en actions concrètes.**
- Analyse d'un transcript de 45 min en ~3s | Export PDF
- Résumé, décisions, plan d'action, points en suspens
- Workflow N8N : webhook → Claude → email résumé → Google Sheet

### 🎯 [Projet 4 — Lead Qualifier AI](./projet-04-lead-qualifier/)
**Qualification automatique de leads commerciaux avec scoring IA.**
- 50 leads qualifiés en ~50s | Score 1-10 | Hot/Warm/Cold
- Réponse personnalisée pour chaque lead + tri par priorité
- Workflow N8N : Google Sheet → Claude → IF Hot → alerte email

---

## Stack technique

| Outil | Usage |
|---|---|
| **Python 3.14** | Langage principal |
| **Streamlit** | Interfaces web interactives |
| **Claude API (Anthropic)** | Intelligence artificielle |
| **Plotly** | Visualisations et dashboards |
| **Pandas** | Manipulation de données |
| **fpdf2** | Génération de PDF |
| **N8N** | Workflows d'automatisation |

## Lancer un projet

```bash
# Cloner le repo
git clone https://github.com/TrouveTaVoie01/ai-automations.git
cd ai-automations

# Installer les dépendances
pip install streamlit anthropic pandas plotly fpdf2

# Lancer un projet (exemple : Email Classifier)
cd projet-01-email-classifier
streamlit run app.py
```

Chaque projet a son propre `README.md` avec les instructions détaillées.

## Structure du repo

```
ai-automations/
├── python-basics/                    # 5 scripts Python commentés
│   ├── hello.py
│   ├── conditions.py
│   ├── boucles.py
│   ├── fonctions.py
│   └── api_claude.py
├── projet-01-email-classifier/       # Classification d'emails
│   ├── app.py
│   ├── emails_demo.csv
│   ├── workflow_n8n.json
│   └── README.md
├── projet-02-document-extractor/     # Extraction de documents
│   ├── app.py
│   ├── documents_demo/
│   ├── workflow_n8n.json
│   └── README.md
├── projet-03-meeting-brain/          # Analyse de réunions
│   ├── app.py
│   ├── transcripts_demo/
│   ├── workflow_n8n.json
│   └── README.md
├── projet-04-lead-qualifier/         # Qualification de leads
│   ├── app.py
│   ├── leads_demo.csv
│   ├── workflow_n8n.json
│   └── README.md
├── STACK.md
└── README.md
```

## Auteur

**Lenny** — AI Automation Specialist
- Stack : Python, Claude API, N8N, Streamlit
- Disponible en CDI full remote
