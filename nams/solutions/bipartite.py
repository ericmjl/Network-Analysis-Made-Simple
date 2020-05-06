import networkx as nx


def extract_partition_nodes(G: nx.Graph, partition: str):
    nodeset = [n for n, d in G.nodes(data=True) if d["bipartite"] == partition]
    if len(nodeset) == 0:
        raise Exception(f"No nodes exist in the partition {partition}!")
    return nodeset
