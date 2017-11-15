# Possible Answer

def extract_neighbor_edges(G, node):
    neighbors = G.neighbors(node)
    newG = nx.Graph()

    for n1, n2 in G.edges():
        if (n1 == node and n2 in neighbors) or (n1 in neighbors and n2 == node):
            newG.add_edge(n1, n2)

    return newG

fig = plt.figure(0)
newG = extract_neighbor_edges(G, 19)
nx.draw(newG, with_labels=True)
