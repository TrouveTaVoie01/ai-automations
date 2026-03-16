#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Génère un CSV de 50 faux emails réalistes pour la démo.
"""
import csv
import random

emails = [
    # SUPPORT (10)
    {"email": "Bonjour, je n'arrive pas à me connecter à mon compte depuis ce matin. J'ai essayé de réinitialiser mon mot de passe mais je ne reçois pas l'email. Pouvez-vous m'aider ? Cordialement, Marie Dupont"},
    {"email": "Mon application plante à chaque fois que j'essaie d'exporter un rapport PDF. C'est urgent car j'ai une présentation demain. Version 3.2.1 sur Windows 11."},
    {"email": "J'ai un problème avec la synchronisation de mes données entre l'app mobile et le site web. Les modifications faites sur mobile ne remontent pas. Merci de votre aide."},
    {"email": "Le bouton 'Sauvegarder' ne fonctionne plus sur la page de paramètres. Bug apparu après la dernière mise à jour. Plusieurs collègues ont le même souci."},
    {"email": "Bonjour l'équipe technique, notre intégration API renvoie des erreurs 500 depuis 14h. Nos clients ne peuvent plus passer de commandes. C'est critique."},
    {"email": "Comment faire pour ajouter un deuxième utilisateur admin sur notre compte entreprise ? Je ne trouve pas l'option dans les paramètres. Merci."},
    {"email": "Suite à votre mise à jour de la semaine dernière, les temps de chargement sont passés de 2 à 15 secondes. C'est devenu inutilisable pour notre équipe de 30 personnes."},
    {"email": "Je souhaite supprimer définitivement mon compte et toutes mes données personnelles conformément au RGPD. Merci de me confirmer la procédure."},
    {"email": "L'authentification à deux facteurs ne fonctionne pas avec mon nouveau téléphone. Je suis bloqué hors de mon compte. Aidez-moi SVP."},
    {"email": "Bonjour, est-ce que votre plateforme est compatible avec Safari sur Mac ? J'ai des problèmes d'affichage sur la page d'accueil."},

    # COMMERCIAL (9)
    {"email": "Bonjour, nous sommes une PME de 50 salariés et nous cherchons une solution de gestion de projet. Pourriez-vous nous envoyer une démo et vos tarifs ? Contact : Pierre Martin, DSI."},
    {"email": "Suite à notre échange téléphonique d'hier, je confirme notre intérêt pour votre offre Enterprise. Pouvez-vous nous faire parvenir un devis pour 200 licences ?"},
    {"email": "Nous utilisons actuellement un concurrent et souhaitons migrer vers votre solution. Quelles sont les conditions de reprise et y a-t-il une offre de migration ?"},
    {"email": "Bonjour, je suis responsable achats chez Carrefour Digital. Nous envisageons un déploiement à grande échelle. Disponible pour un call cette semaine ?"},
    {"email": "Notre période d'essai gratuit se termine dans 5 jours. Avant de passer à la version payante, j'aimerais savoir s'il y a une remise pour un engagement annuel."},
    {"email": "Je voudrais comprendre la différence entre votre offre Pro et Enterprise. Nous sommes 15 utilisateurs avec des besoins de reporting avancé."},
    {"email": "Bonjour, nous organisons un appel d'offres pour un outil CRM. Pourriez-vous remplir notre grille de réponse technique ci-jointe avant le 30 mars ?"},
    {"email": "Suite à la conférence VivaTech, j'ai trouvé votre stand très intéressant. Pouvons-nous planifier une démo pour notre équipe commerciale de 25 personnes ?"},
    {"email": "Nous représentons un groupe de 12 cliniques vétérinaires. Proposez-vous des tarifs groupe ? Notre budget est de 500 EUR/mois maximum."},

    # FACTURATION (8)
    {"email": "Bonjour, je n'ai pas reçu ma facture du mois de février. Notre comptabilité en a besoin pour la clôture mensuelle. Merci de me l'envoyer au plus vite."},
    {"email": "Nous avons été prélevés deux fois ce mois-ci (le 3 et le 15 mars). Merci de rembourser le prélèvement en double. Réf client : CLI-2847."},
    {"email": "Je souhaite modifier l'adresse de facturation de notre compte. Nouvelle adresse : 45 rue de la Paix, 75002 Paris. SIRET : 123 456 789 00012."},
    {"email": "Notre carte bancaire a expiré. Comment mettre à jour nos coordonnées de paiement ? Je ne veux pas que notre abonnement soit interrompu."},
    {"email": "Bonjour, pouvez-vous me fournir un avoir pour la facture FAC-2024-0891 ? Le service n'a pas été livré conformément au contrat."},
    {"email": "Nous passons en paiement par virement bancaire à partir du mois prochain. Merci de nous envoyer vos coordonnées bancaires et un échéancier."},
    {"email": "Je n'ai pas reçu de facture pour notre période d'essai mais j'ai été débité de 49 EUR. Est-ce normal ? Je pensais que l'essai était gratuit."},
    {"email": "Pouvez-vous émettre nos factures avec un numéro de bon de commande ? C'est obligatoire pour notre service comptable. N° BC : PO-2024-3291."},

    # RH (8)
    {"email": "Bonjour, je suis en poste depuis 8 ans dans l'automatisation IA. Je serais intéressé par un poste chez vous en full remote. Voici mon CV en pièce jointe."},
    {"email": "Je souhaite postuler au poste de développeur Python publié sur LinkedIn. J'ai 5 ans d'expérience en data engineering. Quand puis-je passer un entretien ?"},
    {"email": "Suite à notre entretien de lundi, je voulais confirmer ma disponibilité pour commencer dès le 1er avril. J'attends votre retour sur la proposition salariale."},
    {"email": "Bonjour, je suis DRH chez TechCorp. Nous cherchons à externaliser notre recrutement IT. Proposez-vous ce type de service ?"},
    {"email": "Je suis actuellement en stage de fin d'études et j'aimerais savoir si vous proposez des postes en alternance pour septembre 2026 dans le domaine IA."},
    {"email": "Nous avons un programme de partenariat avec les écoles d'ingénieurs. Seriez-vous intéressés pour accueillir nos étudiants en stage technique ?"},
    {"email": "Bonjour, je fais suite à ma candidature envoyée il y a 3 semaines pour le poste de Product Manager. Pourriez-vous me donner un statut ?"},
    {"email": "Nous organisons un job dating le 20 mars à Lyon. Seriez-vous intéressés pour y participer en tant qu'entreprise recruteuse ?"},

    # SPAM (8)
    {"email": "FÉLICITATIONS !!! Vous avez gagné un iPhone 16 Pro !!! Cliquez ici pour réclamer votre prix MAINTENANT. Offre limitée à 24h seulement !!!!"},
    {"email": "Investissez dans le Bitcoin et gagnez 10 000 EUR par jour depuis chez vous. Aucune compétence requise. Formation gratuite. Cliquez sur le lien."},
    {"email": "Votre compte Netflix a été suspendu. Veuillez mettre à jour vos informations bancaires immédiatement en cliquant sur ce lien sécurisé."},
    {"email": "Bonjour cher ami, je suis le prince du Nigeria et j'ai besoin de votre aide pour transférer 15 millions de dollars. Vous recevrez 30% de commission."},
    {"email": "TRAVAILLEZ DE CHEZ VOUS ! Gagnez 5000 EUR/semaine en envoyant des emails. Inscrivez-vous GRATUITEMENT. Places limitées !!!!!"},
    {"email": "Dernière chance ! Votre assurance auto à -80%. Devis gratuit en 2 minutes. Ne ratez pas cette offre exceptionnelle. Répondez OUI pour en profiter."},
    {"email": "Pilules minceur approuvées par les médecins ! Perdez 20kg en 2 semaines sans effort. Résultats GARANTIS ou remboursé. Commandez maintenant."},
    {"email": "Votre ordinateur est infecté par 47 virus ! Téléchargez notre antivirus premium GRATUIT pour vous protéger. Cliquez ici avant qu'il ne soit trop tard."},

    # URGENT (7)
    {"email": "URGENT : Fuite de données détectée sur notre serveur principal. 3000 comptes clients potentiellement exposés. Besoin d'une réponse immédiate de votre équipe sécurité."},
    {"email": "CRITIQUE — Notre site e-commerce est down depuis 30 minutes. Nous perdons environ 2000 EUR par heure. Intervention immédiate requise."},
    {"email": "Alerte sécurité : tentative de connexion suspecte depuis la Russie sur 15 comptes admin. J'ai bloqué les IP mais il faut investiguer d'urgence."},
    {"email": "Notre plus gros client (30% du CA) menace de résilier son contrat demain si le bug de facturation n'est pas corrigé aujourd'hui. Priorité absolue."},
    {"email": "URGENT : La démo pour le client Airbus est dans 2 heures et l'environnement de staging est cassé. On a besoin d'aide immédiatement."},
    {"email": "Incident majeur : le système de paiement renvoie des erreurs sur toutes les transactions depuis 8h ce matin. Aucun client ne peut payer."},
    {"email": "SOS — J'ai accidentellement supprimé la base de données de production. Les backups les plus récents datent d'hier soir. Comment restaurer ?"},
]

# Mélanger pour que le CSV soit réaliste
random.seed(42)
random.shuffle(emails)

# Écrire le CSV
with open("emails_demo.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["email"])
    writer.writeheader()
    writer.writerows(emails)

print(f"Fichier emails_demo.csv généré avec {len(emails)} emails.")
