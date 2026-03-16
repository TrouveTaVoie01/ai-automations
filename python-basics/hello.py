#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script 1 — Variables, types, affichage et calculs simples.
Ce script montre les bases absolues de Python.
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# --- Variables et types ---

# Une variable, c'est juste un nom qu'on colle sur une valeur.
prenom = "Lenny"          # str  → du texte (chaîne de caractères)
age = 22                   # int  → un nombre entier
taille = 1.78              # float → un nombre à virgule
est_disponible = True      # bool → vrai ou faux

# On affiche chaque variable avec son type pour bien comprendre
print("=== Variables et types ===")
print(f"Prénom       : {prenom} (type: {type(prenom).__name__})")
print(f"Âge          : {age} (type: {type(age).__name__})")
print(f"Taille       : {taille} (type: {type(taille).__name__})")
print(f"Disponible   : {est_disponible} (type: {type(est_disponible).__name__})")

# --- Calculs simples ---

print("\n=== Calculs simples ===")

a = 15
b = 4

addition       = a + b      # 19
soustraction   = a - b      # 11
multiplication = a * b      # 60
division       = a / b      # 3.75  → toujours un float
division_entiere = a // b   # 3     → partie entière seulement
modulo         = a % b      # 3     → le reste de la division
puissance      = a ** b     # 50625 → 15 exposant 4

print(f"{a} + {b}  = {addition}")
print(f"{a} - {b}  = {soustraction}")
print(f"{a} × {b}  = {multiplication}")
print(f"{a} / {b}  = {division}")
print(f"{a} // {b} = {division_entiere}")
print(f"{a} % {b}  = {modulo}")
print(f"{a} ** {b} = {puissance}")

# --- Concaténation et f-strings ---

print("\n=== Affichage avancé ===")

# Méthode 1 : concaténation avec +
message1 = "Je m'appelle " + prenom + " et j'ai " + str(age) + " ans."
print(message1)

# Méthode 2 : f-string (la meilleure, retiens celle-là)
message2 = f"Je m'appelle {prenom}, j'ai {age} ans et je mesure {taille}m."
print(message2)

# --- Listes et dictionnaires (aperçu) ---

print("\n=== Collections ===")

# Une liste = plusieurs valeurs dans l'ordre
competences = ["Python", "N8N", "Claude API", "Streamlit"]
print(f"Compétences : {competences}")
print(f"Nombre      : {len(competences)}")
print(f"Première    : {competences[0]}")   # l'index commence à 0
print(f"Dernière    : {competences[-1]}")  # -1 = le dernier élément

# Un dictionnaire = des paires clé → valeur
profil = {
    "nom": prenom,
    "age": age,
    "role": "AI Orchestrator",
    "stack": competences
}
print(f"\nProfil complet : {profil}")
print(f"Rôle           : {profil['role']}")

# --- Résumé ---

print("\n=== Résumé ===")
print("✓ Variables : str, int, float, bool")
print("✓ Calculs   : +, -, *, /, //, %, **")
print("✓ Affichage : print() avec f-strings")
print("✓ Listes    : [], len(), indexation")
print("✓ Dicos     : {clé: valeur}")
print("\nScript terminé avec succès.")
