def extract_path_edges(G, source, target):
    # Check to make sure that a path does exists between source and target.
    if nx.has_path(G, source, target):
        nodes = nx.shortest_path(G, source, target)
        newG = G.subgraph(nodes)
        return newG

    else:
        raise Exception('Path does not exist between nodes {0} and {1}.'.format(source, target))

newG = extract_path_edges(G, 4, 400)
nx.draw(newG, with_labels=True)
