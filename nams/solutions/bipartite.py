import networkx as nx
import pandas as pd
from nams.functions import render_html


def extract_partition_nodes(G: nx.Graph, partition: str):
    nodeset = [n for n, d in G.nodes(data=True) if d["bipartite"] == partition]
    if len(nodeset) == 0:
        raise Exception(f"No nodes exist in the partition {partition}!")
    return nodeset


def bipartite_example_graph():
    bG = nx.Graph()
    bG.add_nodes_from("abcd", bipartite="letters")
    bG.add_nodes_from(range(1, 4), bipartite="numbers")
    bG.add_edges_from([("a", 1), ("b", 1), ("b", 3), ("c", 2), ("c", 3), ("d", 1)])

    return bG


def draw_bipartite_graph_example():
    """Draw an example bipartite graph and its corresponding projection."""
    import matplotlib.pyplot as plt
    import nxviz as nv
    from nxviz import annotate, plots, highlights

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
    plt.sca(ax[0])
    bG = bipartite_example_graph()
    nv.parallel(bG, group_by="bipartite", node_color_by="bipartite")
    annotate.parallel_group(bG, group_by="bipartite", y_offset=-0.5)
    highlights.parallel_edge(bG, "a", 1, group_by="bipartite")
    highlights.parallel_edge(bG, "b", 1, group_by="bipartite")

    pG = nx.bipartite.projected_graph(bG, nodes=list("abcd"))
    plt.sca(ax[1])
    nv.arc(pG)
    highlights.arc_edge(pG, "a", "b")
    return ax


def find_most_similar_crimes(cG: nx.Graph):
    """
    Find the crimes that are most similar to other crimes.
    """
    dcs = pd.Series(nx.degree_centrality(cG))
    return dcs.sort_values(ascending=False).head(10)


def find_most_similar_people(pG: nx.Graph):
    """
    Find the persons that are most similar to other persons.
    """
    dcs = pd.Series(nx.degree_centrality(pG))
    return dcs.sort_values(ascending=False).head(10)


def find_connected_persons(G, person, crime):
    """Answer to exercise on people implicated in crimes"""
    # Step 0: Check that the given "person" and "crime" are connected.
    if not G.has_edge(person, crime):
        raise ValueError(
            f"Graph does not have a connection between {person} and {crime}!"
        )

    # Step 1: calculate weighted projection for person nodes.
    person_nodes = extract_partition_nodes(G, "person")
    person_graph = nx.bipartite.weighted_projected_graph(G, person_nodes)

    # Step 2: Find neighbors of the given `person` node in projected graph.
    candidate_neighbors = set(person_graph.neighbors(person))

    # Step 3: Remove candidate neighbors from the set if they are implicated in the given crime.
    for p in G.neighbors(crime):
        if p in candidate_neighbors:
            candidate_neighbors.remove(p)

    # Step 4: Rank-order the candidate neighbors by number of shared connections.
    data = []
    for nbr in candidate_neighbors:
        data.append(dict(node=nbr, weight=person_graph.edges[person, nbr]["weight"]))
    return pd.DataFrame(data).sort_values("weight", ascending=False)


def bipartite_degree_centrality_denominator():
    """Answer to bipartite graph denominator for degree centrality."""

    ans = """
The total number of neighbors that a node can _possibly_ have
is the number of nodes in the other partition.
This comes naturally from the definition of a bipartite graph,
where nodes can _only_ be connected to nodes in the other partition.
"""
    return ans


def find_most_crime_person(G, person_nodes):
    dcs = (
        pd.Series(nx.bipartite.degree_centrality(G, person_nodes))
        .sort_values(ascending=False)
        .to_frame()
    )
    return dcs.reset_index().query("index.str.contains('p')").iloc[0]["index"]
