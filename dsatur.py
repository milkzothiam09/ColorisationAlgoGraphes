import networkx as nx
import matplotlib.pyplot as plt


def dsatur(G):
    couleurs = {}

    # Degré de chaque sommet
    degres = dict(G.degree())

    # Degré de saturation (initialement 0)
    saturation = {sommet: 0 for sommet in G.nodes()}

    # 1️⃣ Choisir le sommet de plus grand degré
    premier = max(degres, key=degres.get)
    couleurs[premier] = 0

    while len(couleurs) < len(G.nodes()):

        # Mettre à jour les degrés de saturation
        for sommet in G.nodes():
            if sommet not in couleurs:
                couleurs_voisins = {
                    couleurs[voisin]
                    for voisin in G.neighbors(sommet)
                    if voisin in couleurs
                }
                saturation[sommet] = len(couleurs_voisins)

        # 2️⃣ Choisir sommet non coloré avec saturation maximale
        non_colores = [s for s in G.nodes() if s not in couleurs]

        sommet_choisi = max(
            non_colores,
            key=lambda s: (saturation[s], degres[s])
        )

        # 4️⃣ Attribuer la plus petite couleur disponible
        couleurs_voisins = {
            couleurs[voisin]
            for voisin in G.neighbors(sommet_choisi)
            if voisin in couleurs
        }

        couleur = 0
        while couleur in couleurs_voisins:
            couleur += 1

        couleurs[sommet_choisi] = couleur

    return couleurs


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
    ('D', 'E'),
    ('D', 'F'),
    ('E', 'F')
])

# Appliquer DSATUR
couleurs = dsatur(G)

print("Coloration DSATUR :", couleurs)
print("Nombre de couleurs utilisées :", len(set(couleurs.values())))

# -------------------------
# Visualisation
# -------------------------

palette = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]

node_colors = [palette[couleurs[s]] for s in G.nodes()]

pos = nx.spring_layout(G)
nx.draw(G, pos,
        with_labels=True,
        node_color=node_colors,
        node_size=1500,
        font_size=12)

plt.title("Coloration avec l'algorithme DSATUR")
plt.show()
