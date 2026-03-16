#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génère un CSV de 50 faux leads réalistes pour la démo.
"""
import csv
import random

leads = [
    # HOT LEADS (15)
    {"entreprise": "DataFlow Industries", "email": "sophie.durand@dataflow.fr", "message": "Bonjour, nous sommes une PME de 120 personnes dans la logistique. Nous cherchons une solution d'automatisation IA pour traiter nos 500 emails de support quotidiens. Budget de 2000 EUR/mois. Démarrage souhaité avant fin avril. Disponible pour une démo cette semaine ?"},
    {"entreprise": "MediTech Solutions", "email": "dr.garnier@meditech.fr", "message": "Nous gérons 15 cliniques et avons besoin d'automatiser le tri des dossiers patients. Nous avons déjà testé un concurrent mais les résultats ne sont pas satisfaisants. Budget validé par la direction. Pouvez-vous nous faire une proposition commerciale ?"},
    {"entreprise": "LogiPrime Express", "email": "marc.leroy@logiprime.fr", "message": "Urgent : notre service client est débordé depuis le Black Friday. 800 emails non traités. Nous avons besoin d'une solution opérationnelle sous 2 semaines. Budget : pas de limite pour résoudre ce problème. Appelez-moi au 06 12 34 56 78."},
    {"entreprise": "FinanceGuard SA", "email": "isabelle.petit@financeguard.fr", "message": "Suite à notre réunion de vendredi avec votre commercial, nous confirmons notre intérêt pour la licence Enterprise. 200 utilisateurs. Pouvez-vous nous envoyer le contrat ? Notre juriste est disponible lundi."},
    {"entreprise": "EcoPackaging SAS", "email": "thomas.martin@ecopack.fr", "message": "Nous automatisons notre chaîne de production et cherchons un partenaire IA pour le contrôle qualité visuel. 3000 images par jour à analyser. RFP en cours, deadline de réponse le 25 mars. Budget annuel : 50K EUR."},
    {"entreprise": "RetailMax Group", "email": "claire.moreau@retailmax.fr", "message": "DG de RetailMax, 45 magasins en France. Je veux automatiser l'analyse des avis clients Google (2000 avis/mois). J'ai vu votre démo à VivaTech. Budget disponible immédiatement. Quand peut-on signer ?"},
    {"entreprise": "CyberDefense Pro", "email": "henri.fontaine@cyberdef.fr", "message": "Nous cherchons une solution d'analyse automatique des rapports de sécurité. 50 rapports par semaine. Notre RSSI a validé le budget. Besoin d'une démo technique avec notre équipe SOC cette semaine."},
    {"entreprise": "TourismDigital", "email": "samia.benali@tourism-digital.fr", "message": "Agence de voyage en ligne, 500K clients/an. Nous voulons automatiser les réponses aux demandes de devis (300/jour). Notre période haute commence en mai. Budget : 3000 EUR/mois. Pouvez-vous déployer avant le 15 avril ?"},
    {"entreprise": "AgriTech Innovations", "email": "paul.rousseau@agritech-innov.fr", "message": "Coopérative agricole, 800 membres. Nous avons besoin d'un système de classification automatique des réclamations. Appel d'offres en cours. Votre solution est shortlistée avec 2 autres. Présentation au comité le 20 mars."},
    {"entreprise": "EdTech Academy", "email": "julie.lambert@edtech-academy.fr", "message": "Plateforme de formation en ligne avec 50 000 étudiants. Nous voulons un chatbot IA pour le support étudiant. POC validé en interne. Budget R&D de 100K EUR pour 2024. Rencontrons-nous cette semaine."},
    {"entreprise": "InsurTech Plus", "email": "david.chen@insurtech-plus.fr", "message": "Assureur digital, 200 employés. Automatisation du traitement des sinistres (500/mois). Le CEO a donné le feu vert ce matin. On peut commencer quand vous voulez. Budget illimité si le ROI est prouvé en 3 mois."},
    {"entreprise": "LegalFlow", "email": "maitre.dubois@legalflow.fr", "message": "Cabinet d'avocats, 30 associés. Nous cherchons une IA pour analyser les contrats (due diligence). Volume : 200 contrats/mois. Budget de 5000 EUR/mois validé par le managing partner."},
    {"entreprise": "SmartCity Nantes", "email": "maire-adjoint@nantes-smartcity.fr", "message": "Projet smart city : analyse automatique des réclamations citoyennes (800/semaine). Marché public en cours, notre cahier des charges est prêt. Budget municipal alloué : 80K EUR. Réunion de cadrage possible jeudi."},
    {"entreprise": "BioPharm Research", "email": "dr.martin@biopharm-research.fr", "message": "Laboratoire pharmaceutique, 400 employés. Automatisation de la veille scientifique (1000 articles/semaine). Le directeur R&D veut une démo avant la fin du mois. Budget département : non limité."},
    {"entreprise": "TransportElite", "email": "direction@transport-elite.fr", "message": "Groupe de transport, 2000 chauffeurs. Besoin d'IA pour optimiser la planification. Notre DSI vous contacte demain pour organiser un POC de 2 semaines. Budget IT annuel : 500K EUR."},

    # WARM LEADS (20)
    {"entreprise": "StartupVerte", "email": "julien@startupverte.io", "message": "Hello, je suis CEO d'une startup cleantech (série A). On explore les solutions d'automatisation pour notre support client. Pas de budget défini encore mais on lève des fonds en mai. Pouvez-vous m'envoyer de la doc ?"},
    {"entreprise": "ComptaPro", "email": "info@comptapro.fr", "message": "Nous sommes un cabinet comptable de 15 personnes. L'automatisation du tri des factures nous intéresse. Pouvez-vous nous expliquer comment ça marche concrètement et quel serait le coût ?"},
    {"entreprise": "WebAgency42", "email": "contact@webagency42.fr", "message": "Agence web, 25 personnes. On cherche des outils IA pour nos clients. Pas un besoin immédiat mais on veut se positionner sur ce marché. Un call de 30 min serait possible ?"},
    {"entreprise": "Mairie de Bordeaux", "email": "dsi@mairie-bordeaux.fr", "message": "Nous étudions la possibilité d'intégrer l'IA dans le traitement des courriers administratifs. C'est exploratoire à ce stade. Pouvez-vous nous envoyer un dossier de présentation ?"},
    {"entreprise": "FoodTech Express", "email": "alice.martin@foodtech-express.fr", "message": "Startup foodtech, 40 employés. On a vu votre article sur Medium. L'automatisation des commandes nous intéresse. On en est au stade de la réflexion. Quel serait le coût approximatif pour 100 commandes/jour ?"},
    {"entreprise": "DesignStudio Paris", "email": "creative@designstudio-paris.fr", "message": "Studio de design, 8 personnes. On cherche à automatiser la gestion de nos briefs clients. C'est possible avec votre outil ? On a un petit budget mais on est motivés."},
    {"entreprise": "RH Conseil", "email": "recrutement@rhconseil.fr", "message": "Cabinet RH, 20 consultants. L'automatisation du tri des CV nous intéresse beaucoup. On traite 500 CV par mois. Quel ROI peut-on attendre ? Avez-vous des références dans notre secteur ?"},
    {"entreprise": "ImmoGroup", "email": "directeur@immogroup.fr", "message": "Groupe immobilier, 10 agences. On reçoit 200 demandes par semaine. L'automatisation des réponses serait un vrai plus. On en discute en comité de direction la semaine prochaine."},
    {"entreprise": "SportClub Premium", "email": "manager@sportclub-premium.fr", "message": "Chaîne de salles de sport, 12 clubs. On veut améliorer notre rétention membres avec de l'IA. On a vu que vous faisiez de l'analyse de données. C'est dans votre périmètre ?"},
    {"entreprise": "CleanTech Solutions", "email": "cto@cleantech-sol.fr", "message": "On développe une solution IoT pour le traitement de l'eau. On cherche à intégrer de l'IA prédictive. C'est encore en phase de R&D mais on cherche des partenaires techniques."},
    {"entreprise": "MediaGroup France", "email": "innovation@mediagroup.fr", "message": "Groupe média, 500 employés. Notre directeur innovation m'a demandé de me renseigner sur l'automatisation de la modération de commentaires. 10 000 commentaires/jour. Pouvez-vous faire un benchmark ?"},
    {"entreprise": "ArtisanDigital", "email": "pierre@artisan-digital.fr", "message": "Marketplace d'artisans, 3000 vendeurs. On veut automatiser la catégorisation des produits. C'est faisable ? On lance un projet pilote en Q3."},
    {"entreprise": "PharmaDistrib", "email": "achats@pharmadistrib.fr", "message": "Distributeur pharmaceutique. On s'intéresse à l'automatisation de la gestion des commandes. Pouvez-vous nous envoyer un cas client dans notre secteur ?"},
    {"entreprise": "TechFormation", "email": "responsable@techformation.fr", "message": "Organisme de formation, 5000 apprenants/an. On veut automatiser la correction des QCM et la génération de feedbacks personnalisés. Budget en cours de validation pour septembre."},
    {"entreprise": "GreenEnergy Corp", "email": "projets@greenenergy-corp.fr", "message": "Producteur d'énergie renouvelable. On explore l'IA pour la maintenance prédictive de nos éoliennes. 150 turbines à surveiller. Le projet est dans notre roadmap 2025."},
    {"entreprise": "LuxeHotels", "email": "concierge@luxehotels.fr", "message": "Chaîne d'hôtels 5 étoiles, 8 établissements. L'automatisation de la conciergerie par IA nous intéresse. Nos clients sont exigeants. Est-ce que la qualité est au rendez-vous ?"},
    {"entreprise": "AutoParts France", "email": "si@autoparts-france.fr", "message": "Distributeur de pièces auto, catalogue de 500 000 références. On cherche une IA pour améliorer notre moteur de recherche produit. Intéressant mais pas prioritaire avant juin."},
    {"entreprise": "LabAnalyse", "email": "directeur@labanalyse.fr", "message": "Laboratoire d'analyses, 60 employés. Automatisation de l'interprétation des résultats d'analyses. Réglementairement complexe. On en est à l'étude de faisabilité."},
    {"entreprise": "EventPro Agency", "email": "hello@eventpro-agency.fr", "message": "Agence événementielle. On organise 200 événements/an. L'IA pour la gestion des invitations et le matching networking, c'est possible ? Notre prochain gros event est en septembre."},
    {"entreprise": "ConseilStrategie", "email": "partner@conseil-strategie.fr", "message": "Cabinet de conseil en stratégie. On veut proposer des solutions IA à nos clients. Partenariat possible ? On a 50 clients actifs dans le CAC40."},

    # COLD LEADS (15)
    {"entreprise": "N/A", "email": "jean.dupont@gmail.com", "message": "Bonjour, je suis étudiant en informatique et je fais un mémoire sur l'IA en entreprise. Pourriez-vous répondre à quelques questions sur votre solution ?"},
    {"entreprise": "Freelance", "email": "marie.dev@outlook.com", "message": "Hello, je suis développeuse freelance. Je cherche des outils IA gratuits pour mes projets perso. Vous avez un plan gratuit ?"},
    {"entreprise": "Association Locale", "email": "asso.quartier@yahoo.fr", "message": "Bonjour, notre association de quartier cherche un outil pour gérer nos 50 adhérents. On n'a pas de budget mais on peut vous faire de la pub."},
    {"entreprise": "N/A", "email": "curieux123@hotmail.fr", "message": "C'est quoi exactement votre produit ? J'ai vu une pub sur Instagram."},
    {"entreprise": "PME inconnue", "email": "info@petite-boite.fr", "message": "On cherche un stagiaire en IA. Vous connaissez quelqu'un ?"},
    {"entreprise": "Blog Tech", "email": "redacteur@blog-tech.fr", "message": "Je suis journaliste tech. Je prépare un article comparatif sur les outils IA. Pouvez-vous me fournir des infos et des visuels ?"},
    {"entreprise": "Concurrent Direct", "email": "veille@concurrent-ia.com", "message": "Bonjour, je suis intéressé par vos tarifs et les détails techniques de votre solution. Pouvez-vous m'envoyer votre documentation complète ?"},
    {"entreprise": "Université Lyon 3", "email": "prof.recherche@univ-lyon3.fr", "message": "Dans le cadre de nos recherches sur l'IA en entreprise, nous souhaiterions accéder à votre API pour des tests académiques. Est-ce possible gratuitement ?"},
    {"entreprise": "Micro-entreprise", "email": "kevin.auto@gmail.com", "message": "salut, je suis auto-entrepreneur en plomberie. j'ai entendu parler de chatgpt et tout ça. c'est pareil votre truc ?"},
    {"entreprise": "N/A", "email": "testeur@proton.me", "message": "Je teste toutes les solutions IA du marché. Pouvez-vous me donner un accès gratuit de 30 jours pour faire mon évaluation ?"},
    {"entreprise": "ONG Humanitaire", "email": "projets@ong-aide.org", "message": "Nous sommes une ONG. L'IA pourrait nous aider mais nous n'avons aucun budget. Offrez-vous des licences gratuites pour les associations ?"},
    {"entreprise": "N/A", "email": "spam@newsletter-ai.com", "message": "OPPORTUNITÉ : Gagnez 10 000 EUR/mois avec notre programme d'affiliation IA. Inscrivez-vous maintenant !"},
    {"entreprise": "Retraité", "email": "papy.tech@orange.fr", "message": "Bonjour, mon petit-fils m'a parlé de l'intelligence artificielle. J'aimerais comprendre ce que vous faites. C'est gratuit ?"},
    {"entreprise": "Lycée Victor Hugo", "email": "prof.info@lycee-hugo.fr", "message": "Professeur d'informatique. Je cherche des outils IA pour montrer à mes élèves de terminale. Avez-vous des offres éducation ?"},
    {"entreprise": "Startup en création", "email": "founder@stealth-mode.com", "message": "Je n'ai pas encore lancé ma boîte mais j'y réfléchis. L'IA sera centrale dans mon business model. Je reviendrai vers vous dans 6 mois quand j'aurai levé des fonds."},
]

random.seed(42)
random.shuffle(leads)

with open("leads_demo.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["entreprise", "email", "message"])
    writer.writeheader()
    writer.writerows(leads)

print(f"Fichier leads_demo.csv généré avec {len(leads)} leads.")
print(f"  - ~15 Hot, ~20 Warm, ~15 Cold")
