#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script 3 — Boucles : for et while.
Affiche 1 à 10, calcule la somme, et montre les deux types de boucles.
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# === BOUCLE FOR ===

print("=== Boucle FOR : afficher 1 à 10 ===")

# range(1, 11) génère les nombres de 1 à 10 (11 est exclu)
for i in range(1, 11):
    print(f"  {i}", end="")
print()


# --- Calculer la somme de 1 à 10 avec for ---

print("\n=== Somme de 1 à 10 (avec for) ===")

somme = 0

for nombre in range(1, 11):
    somme += nombre
    print(f"  + {nombre} → somme = {somme}")

print(f"  Résultat final : {somme}")


# === BOUCLE WHILE ===

print("\n=== Boucle WHILE : afficher 1 à 10 ===")

compteur = 1

while compteur <= 10:
    print(f"  {compteur}", end="")
    compteur += 1
print()


# --- Somme avec while ---

print("\n=== Somme de 1 à 10 (avec while) ===")

somme = 0
n = 1

while n <= 10:
    somme += n
    n += 1

print(f"  Résultat : {somme}")


# === ITÉRER SUR UNE LISTE ===

print("\n=== Itérer sur une liste ===")

outils = ["Python", "N8N", "Claude API", "Streamlit", "Airtable"]

for outil in outils:
    print(f"  - {outil}")

print("\n  Avec numérotation :")
for i, outil in enumerate(outils, start=1):
    print(f"  {i}. {outil}")


# === BREAK ET CONTINUE ===

print("\n=== Break et Continue ===")

print("Cherche le premier nombre divisible par 7 entre 50 et 100 :")
for n in range(50, 101):
    if n % 7 == 0:
        print(f"  Trouvé : {n}")
        break

print("\nNombres pairs de 1 à 20 (on saute les impairs avec continue) :")
pairs = []
for n in range(1, 21):
    if n % 2 != 0:
        continue
    pairs.append(n)
print(f"  {pairs}")


# === LIST COMPREHENSION ===

print("\n=== List Comprehension ===")

carres = [n**2 for n in range(1, 11)]
print(f"  Carrés de 1 à 10 : {carres}")

carres_pairs = [n**2 for n in range(1, 11) if n**2 % 2 == 0]
print(f"  Carrés pairs      : {carres_pairs}")

mots = ["python", "streamlit", "claude"]
mots_maj = [mot.upper() for mot in mots]
print(f"  En majuscules     : {mots_maj}")


# === BOUCLE IMBRIQUÉE ===

print("\n=== Table de multiplication (1 à 5) ===")

for i in range(1, 6):
    ligne = ""
    for j in range(1, 6):
        ligne += f"{i*j:4d}"
    print(f"  {ligne}")


# --- Résumé ---

print("\n=== Résumé ===")
print("✓ for   → quand on connaît le nombre d'itérations (range, liste)")
print("✓ while → quand on ne sait pas combien de tours (condition)")
print("✓ break → sortir de la boucle")
print("✓ continue → sauter au tour suivant")
print("✓ List comprehension → boucle en une ligne pour créer des listes")
print(f"✓ Somme de 1 à 10 = {sum(range(1, 11))}")
print("\nScript terminé avec succès.")
