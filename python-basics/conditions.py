#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script 2 — Conditions : if, elif, else.
On teste la majorité selon l'âge, puis d'autres cas pratiques.
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def verifier_age(age):
    """Vérifie si une personne est majeure ou mineure et donne des détails."""
    print(f"\n--- Test avec âge = {age} ---")

    if age >= 18:
        print(f"  ✓ {age} ans → Majeur(e)")
    else:
        print(f"  ✗ {age} ans → Mineur(e)")
        ans_restantes = 18 - age
        print(f"    Encore {ans_restantes} an(s) avant la majorité.")

    # Catégorisation plus fine avec elif
    if age < 0:
        categorie = "Invalide (âge négatif)"
    elif age < 3:
        categorie = "Bébé"
    elif age < 12:
        categorie = "Enfant"
    elif age < 18:
        categorie = "Adolescent"
    elif age < 25:
        categorie = "Jeune adulte"
    elif age < 65:
        categorie = "Adulte"
    else:
        categorie = "Senior"

    print(f"  Catégorie : {categorie}")
    return categorie


# --- Tests avec plusieurs âges ---

print("=== Test de majorité / catégorisation ===")

ages_a_tester = [2, 8, 15, 17, 18, 22, 35, 70, -1]

for age in ages_a_tester:
    verifier_age(age)


# --- Conditions combinées avec and, or, not ---

print("\n=== Conditions combinées ===")

age = 22
a_experience = True
cherche_emploi = True

if age >= 18 and cherche_emploi:
    print(f"✓ Majeur ET en recherche d'emploi → profil actif")

if a_experience or age > 30:
    print(f"✓ A de l'expérience OU a plus de 30 ans → profil intéressant")

if not (age < 18):
    print(f"✓ N'est PAS mineur → peut travailler à temps plein")


# --- Opérateur ternaire ---

print("\n=== Opérateur ternaire ===")

statut = "majeur" if age >= 18 else "mineur"
print(f"Âge {age} → statut : {statut}")

niveau = "junior" if age < 25 else ("senior" if age > 40 else "confirmé")
print(f"Âge {age} → niveau estimé : {niveau}")


# --- Vérification de contenu ---

print("\n=== Vérification de contenu ===")

email = "lenny@example.com"

if "@" in email and "." in email:
    print(f"✓ '{email}' ressemble à un email valide")
else:
    print(f"✗ '{email}' n'est pas un email valide")

competences = ["Python", "N8N", "Claude API"]

if "Python" in competences:
    print(f"✓ Python est dans la liste des compétences")

if "Java" not in competences:
    print(f"✓ Java n'est pas dans la liste (et c'est très bien)")


# --- Résumé ---

print("\n=== Résumé ===")
print("✓ if / elif / else pour les branches de décision")
print("✓ and, or, not pour combiner les conditions")
print("✓ Opérateur ternaire : valeur_si_vrai if condition else valeur_si_faux")
print("✓ 'in' pour vérifier la présence dans une liste ou un texte")
print("\nScript terminé avec succès.")
