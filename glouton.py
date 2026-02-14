import networkx as nx
import matplotlib.pyplot as plt


def coloration_glouton(G):
    # Dictionnaire des couleurs
    couleurs = {}

    # Ordre des sommets (ordre naturel)
    for sommet in G.nodes():

        # Couleurs déjà utilisées par les voisins
        couleurs_voisins = set()
        for voisin in G.neighbors(sommet):
            if voisin in couleurs:
                couleurs_voisins.add(couleurs[voisin])

        # Trouver la plus petite couleur disponible
        couleur = 0
        while couleur in couleurs_voisins:
            couleur += 1

        couleurs[sommet] = couleur

    return couleurs


# -------------------------
# Exemple de graphe
# -------------------------

G = nx.Graph()

# Ajout des arêtes
G.add_edges_from([
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'C'),
    ('B', 'D'),
    ('C', 'E'),
    ('D', 'E')
])

# Appliquer l’algorithme glouton
couleurs = coloration_glouton(G)

print("Coloration obtenue :", couleurs)

# -------------------------
# Visualisation
# -------------------------

# Palette de couleurs
palette = ["red", "blue", "green", "yellow", "orange", "purple"]

# Associer chaque sommet à une couleur réelle
node_colors = [palette[couleurs[s]] for s in G.nodes()]

# Dessin
pos = nx.spring_layout(G)  # position automatique
nx.draw(G, pos, with_labels=True, node_color=node_colors,
        node_size=1500, font_size=12)

plt.title("Coloration gloutonne du graphe")
plt.show()
