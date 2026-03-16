#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génère 15 faux documents texte pour la démo (5 factures, 5 CV, 5 contrats).
"""
import os

os.makedirs("documents_demo", exist_ok=True)

# === 5 FACTURES ===

factures = [
    """FACTURE N° FAC-2024-0891
Date : 15/02/2024

FOURNISSEUR :
TechSolutions SAS
45 rue de l'Innovation
69003 Lyon
SIRET : 123 456 789 00012

CLIENT :
Entreprise Dupont SARL
12 avenue des Champs
75008 Paris

DESIGNATION                          QTE    PU HT     TOTAL HT
Licence logiciel CRM Pro (annuel)      1    2 400,00   2 400,00
Formation utilisateurs (2 jours)       1      800,00     800,00
Support premium (12 mois)              1      600,00     600,00

                                    TOTAL HT :   3 800,00 EUR
                                    TVA 20% :      760,00 EUR
                                    TOTAL TTC :  4 560,00 EUR

Conditions de paiement : 30 jours date de facture
IBAN : FR76 1234 5678 9012 3456 7890 123
""",
    """FACTURE N° 2024-03-127
Date d'émission : 03/03/2024

Émetteur : CloudHost Pro
15 boulevard Haussmann, 75009 Paris
TVA Intracommunautaire : FR 12 345678901

Destinataire : Startup InnoVenture
8 rue du Faubourg, 33000 Bordeaux

Description                              Montant HT
Hébergement serveur dédié (mars 2024)      450,00 EUR
Certificat SSL wildcard                     120,00 EUR
Sauvegarde automatique quotidienne           80,00 EUR
Bande passante supplémentaire (500 Go)       50,00 EUR

Sous-total HT :    700,00 EUR
TVA (20%) :        140,00 EUR
Total TTC :        840,00 EUR

Paiement par prélèvement automatique le 10/03/2024.
""",
    """FACTURE

Numéro : INV-2024-445
Date : 28 janvier 2024

De : Agence WebDesign Studio
    22 rue du Commerce, 31000 Toulouse

Pour : Restaurant Le Gourmet
      5 place Bellecour, 69002 Lyon

Prestations réalisées :
- Refonte site web responsive : 3 500,00 EUR HT
- Création logo et charte graphique : 1 200,00 EUR HT
- Shooting photo (20 photos) : 600,00 EUR HT
- Rédaction contenu SEO (10 pages) : 800,00 EUR HT

Total HT : 6 100,00 EUR
TVA 20% : 1 220,00 EUR
Total TTC : 7 320,00 EUR

Règlement sous 45 jours par virement bancaire.
Pénalités de retard : 3 fois le taux d'intérêt légal.
""",
    """FACTURE N° F-2024-0023
Date : 10/02/2024

FOURNISSEUR : DataSécurité SARL
Adresse : 78 avenue de la République, 92100 Boulogne

CLIENT : Cabinet Juridique Martin & Associés
Adresse : 156 rue du Palais, 13006 Marseille

Réf.   Désignation                          HT
001    Audit sécurité informatique           2 800,00
002    Installation pare-feu nouvelle gén.   1 500,00
003    Formation cybersécurité (10 pers.)    1 200,00
004    Licence antivirus entreprise (1 an)     450,00

Total Hors Taxes :  5 950,00 EUR
TVA 20% :          1 190,00 EUR
Total TTC :        7 140,00 EUR

Mode de paiement : Virement - 30 jours fin de mois
""",
    """FACTURE PROFORMA
N° : PF-2024-0156
Date : 20/03/2024

Société émettrice :
MobilityTech SAS - 90 rue de Rivoli, 75001 Paris

Client :
Mairie de Nantes - 2 rue de l'Hôtel de Ville, 44000 Nantes

Objet : Déploiement solution mobilité urbaine

Détail des prestations :
1. Étude de faisabilité et audit terrain           4 500,00 EUR HT
2. Développement application mobile (iOS + Android) 25 000,00 EUR HT
3. Installation 50 bornes connectées               15 000,00 EUR HT
4. Maintenance et support (24 mois)                 8 000,00 EUR HT

Total HT :  52 500,00 EUR
TVA 20% :   10 500,00 EUR
Total TTC : 63 000,00 EUR

Validité de l'offre : 30 jours.
Paiement : 30% à la commande, 40% à la livraison, 30% à la recette.
""",
]

# === 5 CV ===

cvs = [
    """CURRICULUM VITAE

Sophie MARTIN
Email : sophie.martin@email.com
Téléphone : 06 12 34 56 78
Adresse : 25 rue des Lilas, 75011 Paris
LinkedIn : linkedin.com/in/sophie-martin

FORMATION
2018 - Master Data Science, École Polytechnique
2016 - Licence Mathématiques Appliquées, Université Paris-Saclay

EXPÉRIENCE PROFESSIONNELLE
2021-Présent : Data Scientist Senior - BNP Paribas, Paris
- Développement de modèles de scoring crédit (XGBoost, Random Forest)
- Mise en production de pipelines ML sur AWS SageMaker
- Réduction de 30% des faux positifs sur la détection de fraude

2018-2021 : Data Analyst - Criteo, Paris
- Analyse comportementale des utilisateurs (SQL, Python, Tableau)
- A/B testing et optimisation des campagnes publicitaires
- Création de dashboards automatisés pour le comité de direction

COMPÉTENCES
Python, R, SQL, TensorFlow, PyTorch, AWS, Docker, Spark, Tableau, Power BI

LANGUES
Français (natif), Anglais (C1), Espagnol (B2)
""",
    """CV - THOMAS BERNARD

Contact : thomas.bernard@protonmail.com | 07 98 76 54 32
Localisation : Lyon | Mobilité : France entière

PROFIL
Développeur Full-Stack avec 7 ans d'expérience, spécialisé en
applications SaaS B2B. Passionné par les architectures microservices
et le DevOps.

EXPÉRIENCES
2022-Présent : Lead Développeur - Doctolib, Lyon
- Management d'une équipe de 6 développeurs
- Migration architecture monolithique vers microservices (Kubernetes)
- Réduction du temps de déploiement de 4h à 15 minutes

2019-2022 : Développeur Senior - OVHcloud, Roubaix
- Développement API REST haute performance (Go, gRPC)
- Mise en place CI/CD avec GitLab et ArgoCD
- Optimisation des requêtes : temps de réponse divisé par 5

2017-2019 : Développeur Junior - Capgemini, Paris
- Développement d'applications web React/Node.js
- Intégration de systèmes de paiement (Stripe, PayPal)

FORMATION
2017 : Diplôme d'Ingénieur - INSA Lyon, spécialité Informatique

COMPÉTENCES TECHNIQUES
JavaScript, TypeScript, React, Node.js, Go, Python, PostgreSQL,
MongoDB, Docker, Kubernetes, AWS, GCP, Terraform, GitLab CI
""",
    """CURRICULUM VITAE

Prénom Nom : Amina HASSAN
Date de naissance : 15/06/1995
Email : amina.hassan@gmail.com
Tél : 06 45 67 89 01
Ville : Marseille

OBJECTIF
Intégrer une entreprise innovante en tant que Chef de Projet Digital
pour piloter des projets de transformation numérique.

PARCOURS PROFESSIONNEL

2023-Présent : Chef de Projet Digital - Decathlon, Marseille
- Pilotage du projet e-commerce international (budget 1,2M EUR)
- Coordination de 3 équipes (dev, design, marketing) - 15 personnes
- Lancement réussi dans 4 pays en 8 mois

2020-2023 : Product Owner - Ubisoft, Montpellier
- Gestion du backlog et priorisation des features pour un jeu mobile
- Augmentation de la rétention joueur de 25% en 6 mois
- Méthode agile Scrum, sprints de 2 semaines

2019-2020 : Stage puis CDI - Junior PM chez Thales, Sophia Antipolis
- Suivi de projet pour application de défense

DIPLÔMES
2019 : Master Management de Projet Digital - Kedge Business School
2017 : Licence Gestion - Université Aix-Marseille

COMPÉTENCES
Jira, Confluence, Figma, Notion, Google Analytics, SQL, Agile/Scrum,
Lean, Design Thinking, Anglais courant
""",
    """CV

Nom : Pierre DURAND
Email : p.durand@outlook.fr
Téléphone : 06 11 22 33 44
LinkedIn : linkedin.com/in/pierre-durand-rh

Titre : Responsable Ressources Humaines - 12 ans d'expérience

EXPÉRIENCE

2020-2024 : DRH Adjoint - Groupe Leclerc (siège), Ivry-sur-Seine
- Supervision RH de 2 500 collaborateurs sur 35 sites
- Mise en place du SIRH Workday (budget 800K EUR)
- Négociation des accords d'entreprise avec 4 syndicats
- Réduction du turnover de 18% à 11%

2015-2020 : Responsable Recrutement - Accenture, Paris
- Recrutement de 300+ consultants par an
- Création du programme de cooptation (40% des recrutements)
- Déploiement de l'outil ATS SmartRecruiters

2012-2015 : Chargé RH - PME industrielle, Nantes
- Gestion administrative de 150 salariés
- Paie, formation, relations sociales

FORMATION
2012 : Master RH - IGS Paris
2010 : Licence Droit Social - Université de Nantes

COMPÉTENCES
Droit du travail, SIRH (Workday, SAP HR), Recrutement, Formation,
Relations sociales, Paie, GPEC, Excel avancé
""",
    """CURRICULUM VITAE

Julie LAMBERT
Développeuse IA / Machine Learning

Contact : julie.lambert.ai@gmail.com
Tél : 07 66 55 44 33
GitHub : github.com/julielambert
Localisation : Toulouse (full remote possible)

FORMATION
2021 : PhD Intelligence Artificielle - IRIT Toulouse
       Thèse : "Apprentissage par renforcement pour la robotique collaborative"
2017 : Master Informatique spé. IA - INP Toulouse

EXPÉRIENCE PROFESSIONNELLE
2021-Présent : ML Engineer Senior - Airbus, Toulouse
- Développement de modèles de vision par ordinateur pour l'inspection aéro
- Déploiement de modèles en edge computing (NVIDIA Jetson)
- Publication de 3 papiers de recherche (NeurIPS, ICML)

2017-2021 : Doctorante / ATER - IRIT Toulouse
- Recherche en RL multi-agents
- Enseignement (Python, Algo, ML) à l'INP

COMPÉTENCES
Python, PyTorch, TensorFlow, JAX, OpenCV, C++, CUDA, Docker, MLflow,
Weights & Biases, Linux, Git, LaTeX

PUBLICATIONS
- Lambert et al. (2021) "Multi-Agent RL for Collaborative Robotics" - NeurIPS
- Lambert et al. (2020) "Sim-to-Real Transfer in Manufacturing" - ICML

LANGUES
Français (natif), Anglais (C2), Allemand (B1)
""",
]

# === 5 CONTRATS ===

contrats = [
    """CONTRAT DE PRESTATION DE SERVICES

Entre les soussignés :

La société DigitalAgency SAS, au capital de 50 000 EUR,
dont le siège social est situé 15 rue de la Tech, 75003 Paris,
immatriculée au RCS de Paris sous le numéro 987 654 321,
représentée par M. Alexandre PETIT, en qualité de Directeur Général,
ci-après dénommée "le Prestataire",

ET

La société BioPharm SA, au capital de 500 000 EUR,
dont le siège social est situé 200 avenue de la Santé, 92400 Courbevoie,
représentée par Mme Claire MOREAU, en qualité de Directrice Marketing,
ci-après dénommée "le Client",

IL A ÉTÉ CONVENU CE QUI SUIT :

Article 1 - Objet
Le Prestataire s'engage à réaliser pour le Client la refonte complète
du site web corporate et la mise en place d'une stratégie SEO.

Article 2 - Durée
Le présent contrat est conclu pour une durée de 6 mois à compter
de sa date de signature, soit du 01/03/2024 au 31/08/2024.

Article 3 - Prix
Le montant total de la prestation s'élève à 35 000 EUR HT.
Paiement en 3 échéances : 40% à la signature, 30% à mi-parcours, 30% à la livraison.

Article 4 - Confidentialité
Les parties s'engagent à maintenir confidentielles toutes les
informations échangées dans le cadre du présent contrat.

Fait à Paris, le 25/02/2024, en deux exemplaires originaux.
""",
    """CONTRAT DE TRAVAIL À DURÉE INDÉTERMINÉE

Entre :
L'employeur : StartupVerte SAS
Siège : 10 rue de l'Écologie, 44000 Nantes
SIRET : 456 789 012 00034
Représentée par : Julien ROUSSEAU, CEO

Et :
Le salarié : Mme Fatima BENALI
Née le : 22/08/1992 à Casablanca
Adresse : 34 rue de la Loire, 44100 Nantes
N° SS : 2 92 08 99 xxx xxx xx

Article 1 - Engagement et fonctions
Mme BENALI est engagée en qualité de Responsable Marketing Digital,
statut Cadre, coefficient 350 de la convention collective SYNTEC.

Article 2 - Date d'effet et période d'essai
Le présent contrat prend effet le 01/04/2024.
Période d'essai : 4 mois, renouvelable une fois.

Article 3 - Rémunération
Salaire brut mensuel : 4 200 EUR sur 12 mois.
Prime sur objectifs : jusqu'à 15% du salaire annuel brut.

Article 4 - Durée du travail
Forfait jours : 218 jours par an. Télétravail : 3 jours par semaine.

Article 5 - Lieu de travail
Siège social de l'entreprise à Nantes, avec possibilité de télétravail.

Fait à Nantes, le 15/03/2024.
""",
    """CONTRAT DE LICENCE LOGICIELLE

ENTRE :
L'Éditeur : SoftwareForge SARL
Siège social : 5 impasse du Code, 31000 Toulouse
RCS Toulouse : 789 012 345

ET :
Le Licencié : Hôpital Saint-Antoine
Adresse : 184 rue du Faubourg Saint-Antoine, 75012 Paris
Représenté par : Dr. Philippe GARNIER, Directeur des Systèmes d'Information

ARTICLE 1 - OBJET
L'Éditeur concède au Licencié une licence d'utilisation non exclusive
du logiciel "MedFlow Pro" - solution de gestion des dossiers patients.

ARTICLE 2 - DURÉE
Licence perpétuelle avec maintenance obligatoire.
Contrat de maintenance : 3 ans, du 01/01/2024 au 31/12/2026.

ARTICLE 3 - CONDITIONS FINANCIÈRES
Licence perpétuelle (200 postes) : 180 000 EUR HT
Maintenance annuelle : 36 000 EUR HT/an
Formation initiale (5 jours) : 8 000 EUR HT
Total première année : 224 000 EUR HT

ARTICLE 4 - GARANTIE
L'Éditeur garantit le bon fonctionnement du logiciel pendant 12 mois.
Temps de réponse garanti : 4h pour les incidents critiques.

ARTICLE 5 - DONNÉES PERSONNELLES
Le traitement des données de santé est conforme au RGPD et à la
réglementation HDS (Hébergement de Données de Santé).

Fait à Toulouse, le 20/12/2023.
""",
    """CONTRAT DE PARTENARIAT COMMERCIAL

ENTRE :

La société LogiTrans Express, SARL au capital de 200 000 EUR
Siège : Zone Industrielle Nord, 59000 Lille
Représentée par : M. Bruno LEROY, Gérant
Ci-après "Partenaire A"

ET :

La société EcoEmballage, SAS au capital de 100 000 EUR
Siège : 67 avenue de l'Industrie, 69200 Vénissieux
Représentée par : Mme Isabelle CHABERT, Présidente
Ci-après "Partenaire B"

Article 1 - Objet du partenariat
Les Partenaires conviennent de collaborer pour proposer une offre
conjointe de logistique éco-responsable aux entreprises e-commerce.

Article 2 - Durée
Durée initiale de 2 ans à compter du 01/04/2024, renouvelable
par tacite reconduction par périodes de 1 an.

Article 3 - Engagements réciproques
Partenaire A : assure le transport et la livraison dernier kilomètre.
Partenaire B : fournit les emballages recyclables et la solution de suivi.

Article 4 - Répartition des revenus
Les revenus générés par l'offre conjointe sont répartis à hauteur de
60% pour le Partenaire A et 40% pour le Partenaire B.

Article 5 - Exclusivité
Chaque partenaire s'engage à ne pas proposer d'offre similaire
avec un concurrent direct pendant la durée du contrat.

Fait à Lille, le 15/03/2024, en deux exemplaires.
""",
    """CONTRAT DE SOUS-TRAITANCE INFORMATIQUE

ENTRE :
Le Donneur d'ordre : Banque Nationale de Développement SA
Siège : 1 place de la Bourse, 75002 Paris
Représentée par : M. Henri FONTAINE, DSI

ET :
Le Sous-traitant : CyberShield Technologies SAS
Siège : 25 rue de la Défense, 92800 Puteaux
Représentée par : Mme Sarah LEVY, Directrice Générale

Article 1 - Objet
Le Sous-traitant s'engage à assurer la surveillance et la protection
du système d'information du Donneur d'ordre (SOC managé 24/7).

Article 2 - Durée
Contrat de 3 ans, du 01/01/2024 au 31/12/2026.
Résiliation possible avec préavis de 6 mois.

Article 3 - Périmètre
- Supervision 24/7 du SI (2 500 endpoints, 150 serveurs)
- Réponse aux incidents de sécurité (CERT)
- Tests d'intrusion trimestriels
- Rapports mensuels de sécurité

Article 4 - Prix
Forfait mensuel : 45 000 EUR HT/mois
Tests d'intrusion : 12 000 EUR HT/trimestre
Total annuel : 588 000 EUR HT

Article 5 - SLA
Disponibilité du SOC : 99,9%
Temps de détection d'un incident critique : < 15 minutes
Temps de réponse initial : < 30 minutes

Article 6 - Conformité
Le Sous-traitant s'engage à respecter les normes ISO 27001,
PCI-DSS et les exigences de l'ACPR/Banque de France.

Fait à Paris, le 15/12/2023.
""",
]

# Écrire les fichiers
for i, facture in enumerate(factures, 1):
    with open(f"documents_demo/facture_{i:02d}.txt", "w", encoding="utf-8") as f:
        f.write(facture.strip())

for i, cv in enumerate(cvs, 1):
    with open(f"documents_demo/cv_{i:02d}.txt", "w", encoding="utf-8") as f:
        f.write(cv.strip())

for i, contrat in enumerate(contrats, 1):
    with open(f"documents_demo/contrat_{i:02d}.txt", "w", encoding="utf-8") as f:
        f.write(contrat.strip())

print(f"15 documents générés dans documents_demo/ :")
print(f"  - 5 factures")
print(f"  - 5 CV")
print(f"  - 5 contrats")
