import networkx as nx
import matplotlib.pyplot as plt


# Vérifie si on peut attribuer une couleur à un sommet
def est_valide(G, sommet, couleur, couleurs):
    for voisin in G.neighbors(sommet):
        if couleurs.get(voisin) == couleur:
            return False
    return True


# Fonction récursive de backtracking
def backtracking(G, sommets, couleurs, k, index=0):
    if index == len(sommets):
        return True  # Tous les sommets sont colorés

    sommet = sommets[index]

    for couleur in range(k):
        if est_valide(G, sommet, couleur, couleurs):
            couleurs[sommet] = couleur

            if backtracking(G, sommets, couleurs, k, index + 1):
                return True

            # Backtrack
            del couleurs[sommet]

    return False


# Trouver le nombre chromatique
def coloration_exacte(G):
    sommets = list(G.nodes())

    for k in range(1, len(G.nodes()) + 1):
        couleurs = {}
        if backtracking(G, sommets, couleurs, k):
            return couleurs, k

    return None, None


# -------------------------
# Exemple de graphe
# -------------------------

G = nx.Graph()

G.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'E'),
    ('D', 'E')
])

# Calcul exact
couleurs, k = coloration_exacte(G)

print("Coloration exacte :", couleurs)
print("Nombre chromatique :", k)

# -------------------------
# Visualisation
# -------------------------

palette = ["red", "blue", "green", "yellow", "orange", "purple"]

node_colors = [palette[couleurs[s]] for s in G.nodes()]

pos = nx.spring_layout(G)
nx.draw(G, pos,
        with_labels=True,
        node_color=node_colors,
        node_size=1500,
        font_size=12)

plt.title(f"Coloration exacte par Backtracking (k = {k})")
plt.show()
