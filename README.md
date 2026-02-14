Graph Coloring Algorithms

Ce projet implémente plusieurs algorithmes de coloration de graphes en Python.

La coloration consiste à attribuer une couleur à chaque sommet d’un graphe de manière à ce que deux sommets adjacents n’aient pas la même couleur.

📌 Algorithmes implémentés
1️⃣ Glouton (Greedy Coloring)

Algorithme simple et rapide.

Principe :

Parcourt les sommets dans un ordre donné

Attribue à chaque sommet la plus petite couleur disponible

Ne revient jamais en arrière

Avantages :

Rapide (≈ O(n + m))

Facile à implémenter

Inconvénient :

Ne garantit pas le nombre chromatique minimal

2️⃣ DSATUR (Degree of Saturation)

Version améliorée du glouton.

Principe :

Choisit à chaque étape le sommet ayant le plus grand degré de saturation

En cas d’égalité → sommet de plus grand degré

Attribue la plus petite couleur disponible

Avantages :

Très bonnes solutions en pratique

Souvent proche de l’optimal

Exact pour certains graphes (bipartis, cycles impairs)

Complexité :

Environ O(n²)

3️⃣ Backtracking (Recherche exhaustive)

Méthode exacte.

Principe :

Fixe un nombre de couleurs k

Explore toutes les combinaisons possibles

Revient en arrière en cas de conflit

Avantages :

Garantit le nombre chromatique exact

Inconvénients :

Complexité exponentielle O(kⁿ)

Impraticable pour les grands graphes
