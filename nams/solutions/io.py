"""Solutions to I/O chapter"""


def filter_graph(G, minimum_num_trips):
    """
    Filter the graph such that
    only edges that have minimum_num_trips or more
    are present.
    """
    G_filtered = G.copy()
    for u, v, d in G.edges(data=True):
        if d["num_trips"] < minimum_num_trips:
            G_filtered.remove_edge(u, v)
    return G_filtered


def test_graph_integrity(G):
    """Test integrity of raw Divvy graph."""
    assert len(G.nodes()) == 300
    assert len(G.edges()) == 44422
