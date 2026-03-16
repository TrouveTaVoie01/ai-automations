#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script 5 — Appel à l'API Claude (Anthropic).
Envoie une question à Claude et affiche la réponse proprement.
"""
import sys
import io
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import anthropic  # le SDK officiel d'Anthropic


def poser_question_claude(question, modele="claude-sonnet-4-20250514"):
    """
    Envoie une question à l'API Claude et retourne la réponse.

    Paramètres :
        question : str → le texte à envoyer à Claude
        modele   : str → le modèle à utiliser

    Retourne :
        dict avec la réponse, le modèle utilisé, et les tokens consommés
    """
    # La clé API est lue depuis la variable d'environnement ANTHROPIC_API_KEY
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError(
            "Variable d'environnement ANTHROPIC_API_KEY non définie.\n"
            "Définissez-la avec : export ANTHROPIC_API_KEY='votre-clé'"
        )

    client = anthropic.Anthropic(api_key=api_key)

    # Appel à l'API
    message = client.messages.create(
        model=modele,
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    # On extrait la réponse textuelle
    reponse_texte = message.content[0].text

    return {
        "reponse": reponse_texte,
        "modele": message.model,
        "tokens_entree": message.usage.input_tokens,
        "tokens_sortie": message.usage.output_tokens,
        "tokens_total": message.usage.input_tokens + message.usage.output_tokens
    }


def afficher_reponse(question, resultat):
    """Affiche la question et la réponse de manière formatée."""
    print("=" * 60)
    print(f"QUESTION : {question}")
    print("-" * 60)
    print(f"RÉPONSE  :\n{resultat['reponse']}")
    print("-" * 60)
    print(f"Modèle   : {resultat['modele']}")
    print(f"Tokens   : {resultat['tokens_entree']} (entrée) + "
          f"{resultat['tokens_sortie']} (sortie) = "
          f"{resultat['tokens_total']} (total)")
    print("=" * 60)


def demo_sans_api():
    """Mode démo quand la clé API n'est pas disponible."""
    print("=" * 60)
    print("MODE DÉMO — Pas de clé API valide détectée")
    print("=" * 60)
    print()
    print("Ce script appelle l'API Claude pour :")
    print("  1. Envoyer une question en langage naturel")
    print("  2. Recevoir une réponse structurée")
    print("  3. Afficher les métriques (tokens, modèle)")
    print()
    print("--- Exemple de sortie avec une clé valide ---")
    print()
    print("QUESTION : Explique en 3 phrases simples ce qu'est")
    print("           l'automatisation par IA.")
    print("-" * 60)
    print("RÉPONSE  :")
    print("L'automatisation par IA consiste à utiliser l'intelligence")
    print("artificielle pour exécuter des tâches répétitives sans")
    print("intervention humaine. Les entreprises l'utilisent pour")
    print("traiter des emails, analyser des documents et qualifier")
    print("des leads automatiquement. Cela permet de gagner du temps")
    print("et de réduire les erreurs sur les processus routiniers.")
    print("-" * 60)
    print("Modèle   : claude-sonnet-4-20250514")
    print("Tokens   : 35 (entrée) + 89 (sortie) = 124 (total)")
    print("=" * 60)
    print()
    print("Pour utiliser ce script en mode réel :")
    print("  export ANTHROPIC_API_KEY='sk-ant-api03-...'")
    print("  python api_claude.py")


# === EXÉCUTION ===

if __name__ == "__main__":
    question = (
        "Explique en 3 phrases simples ce qu'est l'automatisation par IA "
        "et pourquoi c'est utile pour les entreprises."
    )

    api_key = os.environ.get("ANTHROPIC_API_KEY")

    if api_key:
        print("Envoi de la question à Claude...\n")
        try:
            resultat = poser_question_claude(question)
            afficher_reponse(question, resultat)
        except anthropic.AuthenticationError:
            print("✗ Clé API invalide ou expirée.\n")
            demo_sans_api()
        except Exception as e:
            print(f"✗ Erreur : {e}\n")
            demo_sans_api()
    else:
        demo_sans_api()

    print("\nScript terminé avec succès.")
