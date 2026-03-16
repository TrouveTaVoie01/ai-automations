#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script 4 — Fonctions : créer et utiliser des fonctions réutilisables.
3 fonctions utiles : compter les mots, inverser un texte, calculer une moyenne.
"""
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def compter_mots(texte):
    """
    Compte le nombre de mots dans un texte.
    Un mot = tout ce qui est séparé par des espaces.
    """
    mots = texte.strip().split()
    return len(mots)


def inverser_texte(texte):
    """
    Inverse un texte caractère par caractère.
    Utilise le slicing Python : [::-1] parcourt le texte à l'envers.
    """
    return texte[::-1]


def calculer_moyenne(nombres):
    """
    Calcule la moyenne d'une liste de nombres.
    Retourne None si la liste est vide.
    """
    if not nombres:
        return None
    return sum(nombres) / len(nombres)


def analyser_texte(texte):
    """Analyse complète d'un texte : combine plusieurs métriques."""
    nb_mots = compter_mots(texte)
    nb_caracteres = len(texte)
    nb_phrases = texte.count('.') + texte.count('!') + texte.count('?')
    mots_par_phrase = round(nb_mots / nb_phrases, 1) if nb_phrases > 0 else nb_mots

    return {
        "mots": nb_mots,
        "caractères": nb_caracteres,
        "phrases": nb_phrases,
        "mots_par_phrase": mots_par_phrase
    }


def formater_nombre(n, decimales=2):
    """Formate un nombre avec séparateur de milliers et décimales."""
    return f"{n:,.{decimales}f}".replace(",", " ").replace(".", ",")


# === TESTS ===

if __name__ == "__main__":

    print("=== Test : compter_mots() ===")
    phrases_test = [
        "Bonjour le monde",
        "L'intelligence artificielle transforme le business en 2025",
        "",
        "Un",
        "  Des espaces   partout   dans   ce   texte  "
    ]
    for phrase in phrases_test:
        nb = compter_mots(phrase)
        print(f'  "{phrase}" → {nb} mot(s)')

    print("\n=== Test : inverser_texte() ===")
    textes_test = ["Python", "Bonjour", "AI Automation", "radar"]
    for texte in textes_test:
        inverse = inverser_texte(texte)
        est_palindrome = texte.lower() == inverse.lower()
        palindrome_tag = " ← palindrome !" if est_palindrome else ""
        print(f'  "{texte}" → "{inverse}"{palindrome_tag}')

    print("\n=== Test : calculer_moyenne() ===")
    listes_test = [
        [10, 15, 20],
        [100],
        [8, 12, 15, 9, 11, 14, 10, 13],
        [],
        [1.5, 2.5, 3.5, 4.5]
    ]
    for liste in listes_test:
        moy = calculer_moyenne(liste)
        if moy is not None:
            print(f"  {liste} → moyenne = {moy:.2f}")
        else:
            print(f"  {liste} → liste vide, pas de moyenne")

    print("\n=== Test : analyser_texte() ===")
    texte_demo = (
        "L'automatisation par IA révolutionne les entreprises. "
        "Les tâches répétitives sont éliminées. "
        "Les équipes se concentrent sur la stratégie !"
    )
    print(f'  Texte : "{texte_demo}"')
    analyse = analyser_texte(texte_demo)
    for cle, valeur in analyse.items():
        print(f"    {cle:20s} : {valeur}")

    print("\n=== Test : formater_nombre() ===")
    nombres_test = [1234567.89, 42, 0.5, 1000000, 3.14159]
    for n in nombres_test:
        print(f"  {n} → {formater_nombre(n)}")
    print(f"  1500000 (0 déc.) → {formater_nombre(1500000, decimales=0)}")

    print("\n=== Résumé ===")
    print("✓ def nom_fonction(params): → définir une fonction")
    print("✓ return → renvoyer un résultat")
    print("✓ Paramètres par défaut : def f(x, y=10)")
    print("✓ Docstrings → documenter ce que fait la fonction")
    print("✓ if __name__ == '__main__': → exécuter seulement en direct")
    print("\nScript terminé avec succès.")
