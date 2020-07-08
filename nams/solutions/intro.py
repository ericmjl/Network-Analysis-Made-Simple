"""
Solutions to Intro Chapter.
"""


def node_metadata(G):
    """Counts of students of each gender."""
    from collections import Counter

    mf_counts = Counter([d["gender"] for n, d in G.nodes(data=True)])
    return mf_counts


def edge_metadata(G):
    """Maximum number of times that a student rated another student."""
    counts = [d["count"] for n1, n2, d in G.edges(data=True)]
    maxcount = max(counts)
    return maxcount


def adding_students(G):
    """How to nodes and edges to a graph."""
    G = G.copy()
    G.add_node(30, gender="male")
    G.add_node(31, gender="female")
    G.add_edge(30, 31, count=3)
    G.add_edge(31, 30, count=3)  # reverse is optional in undirected network
    G.add_edge(30, 7, count=3)  # but this network is directed
    G.add_edge(7, 30, count=3)
    G.add_edge(31, 7, count=3)
    G.add_edge(7, 31, count=3)
    return G


def unrequitted_friendships_v1(G):
    """Answer to unrequitted friendships problem."""
    unrequitted_friendships = []
    for n1, n2 in G.edges():
        if not G.has_edge(n2, n1):
            unrequitted_friendships.append((n1, n2))
    return unrequitted_friendships


def unrequitted_friendships_v2(G):
    """Alternative answer to unrequitted friendships problem. By @schwanne."""
    return len([(n1, n2) for n1, n2 in G.edges() if not G.has_edge(n2, n1)])


def unrequitted_friendships_v3(G):
    """Alternative answer to unrequitted friendships problem. By @end0."""
    links = ((n1, n2) for n1, n2, d in G.edges(data=True))
    reverse_links = ((n2, n1) for n1, n2, d in G.edges(data=True))

    return len(list(set(links) - set(reverse_links)))
