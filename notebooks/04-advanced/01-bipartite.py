# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ipython==9.1.0",
#     "marimo",
#     "matplotlib==3.10.1",
#     "nams==0.0.2",
#     "networkx==3.4.2",
#     "nxviz==0.7.6",
#     "pandas==2.2.3",
#     "pyarrow==20.0.0",
#     "pyprojroot==0.3.0",
#     "tqdm==4.67.1",
# ]
# [[tool.uv.index]]
# name = "ericmjl-personal-packages"
# url = "https://ericmjl--pypiserver-server.modal.run/simple/"
# explicit = true
# [tool.uv.sources]
# nams = { index = "ericmjl-personal-packages" }
# ///

import marimo

__generated_with = "0.13.0"
app = marimo.App()


@app.cell
def _():
    import warnings

    warnings.filterwarnings("ignore")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Introduction""")
    return


@app.cell
def _():
    from IPython.display import YouTubeVideo

    YouTubeVideo(id="BYOK12I9vgI", width="100%")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In this chapter, we will look at bipartite graphs and their applications.

        ## What are bipartite graphs?

        As the name suggests,
        bipartite have two (bi) node partitions (partite).
        In other words, we can assign nodes to one of the two partitions.
        (By contrast, all of the graphs that we have seen before are _unipartite_:
        they only have a single partition.)

        ### Rules for bipartite graphs

        With unipartite graphs, you might remember a few rules that apply.

        Firstly, nodes and edges belong to a _set_.
        This means the node set contains only unique members,
        i.e. no node can be duplicated.
        The same applies for the edge set.

        On top of those two basic rules, bipartite graphs add an additional rule:
        Edges can only occur between nodes of **different** partitions.
        In other words, nodes within the same partition
        are not allowed to be connected to one another.

        ### Applications of bipartite graphs

        Where do we see bipartite graphs being used?
        Here's one that is very relevant to e-commerce,
        which touches our daily lives:

        > We can model customer purchases of products using a bipartite graph.
        > Here, the two node sets are **customer** nodes and **product** nodes,
        > and edges indicate that a customer $C$ purchased a product $P$.

        On the basis of this graph, we can do interesting analyses,
        such as finding customers that are similar to one another
        on the basis of their shared product purchases.

        Can you think of other situations
        where a bipartite graph model can be useful?

        ## Dataset

        Here's another application in crime analysis,
        which is relevant to the example that we will use in this chapter:

        > This bipartite network contains persons
        > who appeared in at least one crime case
        > as either a suspect, a victim, a witness
        > or both a suspect and victim at the same time.
        > A left node represents a person and a right node represents a crime.
        > An edge between two nodes shows that
        > the left node was involved in the crime
        > represented by the right node.

        This crime dataset was also sourced from Konect.
        """
    )
    return


@app.cell
def _():
    from nams import load_data as cf

    G = cf.load_crime_network()
    for n, d in G.nodes(data=True):
        G.nodes[n]["degree"] = G.degree(n)
    return (G,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If you inspect the nodes,
        you will see that they contain a special metadata keyword: `bipartite`.
        This is a special keyword that NetworkX can use
        to identify nodes of a given partition.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Visualize the crime network

        To help us get our bearings right, let's visualize the crime network.
        """
    )
    return


@app.cell
def _(G):
    import nxviz as nv
    import matplotlib.pyplot as plt

    fig, _ax = plt.subplots(figsize=(7, 7))
    nv.circos(
        G,
        sort_by="degree",
        group_by="bipartite",
        node_color_by="bipartite",
        node_enc_kwargs={"size_scale": 3},
    )
    plt.show()
    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Exercise: Extract each node set

        A useful thing to be able to do
        is to extract each partition's node set.
        This will become handy when interacting with
        NetworkX's bipartite algorithms later on.

        > Write a function that extracts all of the nodes
        > from specified node partition.
        > It should also raise a plain Exception
        > if no nodes exist in that specified partition.
        > (as a precuation against users putting in invalid partition names).
        """
    )
    return


@app.cell
def _(_______, ____________, _____________):
    import networkx as nx
    from inspect import getsource

    def extract_partition_nodes(G: nx.Graph, partition: str):
        nodeset = [_ for _, _ in _______ if ____________]
        if _____________:
            raise Exception(f"No nodes exist in the partition {partition}!")
        return nodeset

    from nams.solutions.bipartite import extract_partition_nodes

    # Uncomment the next line to see the answer.
    print(getsource(extract_partition_nodes))
    return extract_partition_nodes, getsource, nx


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Bipartite Graph Projections

        In a bipartite graph, one task that can be useful to do
        is to calculate the projection of a graph onto one of its nodes.

        What do we mean by the "projection of a graph"?
        It is best visualized using this figure:
        """
    )
    return


@app.cell
def _(nx, plt):
    from nams.solutions.bipartite import (
        draw_bipartite_graph_example,
        bipartite_example_graph,
    )
    from nxviz import annotate

    bG = bipartite_example_graph()
    pG = nx.bipartite.projection.projected_graph(bG, "abcd")
    _ax = draw_bipartite_graph_example()
    plt.sca(_ax[0])
    annotate.parallel_labels(bG, group_by="bipartite")
    plt.sca(_ax[1])
    annotate.arc_labels(pG)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As shown in the figure above, we start first with a bipartite graph with two node sets,
        the "alphabet" set and the "numeric" set.
        The projection of this bipartite graph onto the "alphabet" node set
        is a graph that is constructed such that it only contains the "alphabet" nodes,
        and edges join the "alphabet" nodes because they share a connection to a "numeric" node.
        The red edge on the right
        is basically the red path traced on the left.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Computing graph projections

        How does one compute graph projections using NetworkX?
        Turns out, NetworkX has a `bipartite` submodule,
        which gives us all of the facilities that we need
        to interact with bipartite algorithms.

        First of all, we need to check that the graph
        is indeed a bipartite graph.
        NetworkX provides a function for us to do so:
        """
    )
    return


@app.cell
def _(G):
    from networkx.algorithms import bipartite

    bipartite.is_bipartite(G)
    return (bipartite,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now that we've confirmed that the graph is indeed bipartite,
        we can use the NetworkX bipartite submodule functions
        to generate the bipartite projection onto one of the node partitions.

        First off, we need to extract nodes from a particular partition.
        """
    )
    return


@app.cell
def _(G, extract_partition_nodes):
    person_nodes = extract_partition_nodes(G, "person")
    crime_nodes = extract_partition_nodes(G, "crime")
    return crime_nodes, person_nodes


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Next, we can compute the projection:""")
    return


@app.cell
def _(G, bipartite, crime_nodes, person_nodes):
    person_graph = bipartite.projected_graph(G, person_nodes)
    crime_graph = bipartite.projected_graph(G, crime_nodes)
    return crime_graph, person_graph


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        And with that, we have our projected graphs!

        Go ahead and inspect them:
        """
    )
    return


@app.cell
def _(person_graph):
    list(person_graph.edges(data=True))[0:5]
    return


@app.cell
def _(crime_graph):
    list(crime_graph.edges(data=True))[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now, what is the _interpretation_ of these projected graphs?

        - For `person_graph`, we have found _individuals who are linked by shared participation (whether witness or suspect) in a crime._
        - For `crime_graph`, we have found _crimes that are linked by shared involvement by people._

        Just by this graph, we already can find out pretty useful information.
        Let's use an exercise that leverages what you already know
        to extract useful information from the projected graph.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Exercise: find the crime(s) that have the most shared connections with other crimes

        > Find crimes that are most similar to one another
        > on the basis of the number of shared connections to individuals.

        _Hint: This is a degree centrality problem!_
        """
    )
    return


@app.cell
def _(______________, ___________________, crime_graph, nx):
    import pandas as pd

    def find_most_similar_crimes(cG: nx.Graph):
        """
        Find the crimes that are most similar to other crimes.
        """
        dcs = ______________
        return ___________________

    from nams.solutions.bipartite import find_most_similar_crimes

    find_most_similar_crimes(crime_graph)
    return (pd,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Exercise: find the individual(s) that have the most shared connections with other individuals

        > Now do the analogous thing for individuals!
        """
    )
    return


@app.cell
def _(______________, ___________________, nx, person_graph):
    def find_most_similar_people(pG: nx.Graph):
        """
        Find the persons that are most similar to other persons.
        """
        dcs = ______________
        return ___________________

    from nams.solutions.bipartite import find_most_similar_people

    find_most_similar_people(person_graph)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Weighted Projection

        Though we were able to find out which graphs were connected with one another,
        we did not record in the resulting projected graph
        the **strength** by which the two nodes were connected.
        To preserve this information, we need another function:
        """
    )
    return


@app.cell
def _(G, bipartite, person_nodes):
    weighted_person_graph = bipartite.weighted_projected_graph(G, person_nodes)
    list(weighted_person_graph.edges(data=True))[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Exercise: Find the people that can help with investigating a `crime`'s `person`.

        Let's pretend that we are a detective trying to solve a crime,
        and that we right now need to find other individuals
        who were not implicated in the same _exact_ crime as an individual was,
        but who might be able to give us information about that individual
        because they were implicated in other crimes with that individual.

        > Implement a function that takes in a bipartite graph `G`, a string `person` and a string `crime`,
        > and returns a list of other `person`s that were **not** implicated in the `crime`,
        > but were connected to the `person` via other crimes.
        > It should return a _ranked list_,
        > based on the **number of shared crimes** (from highest to lowest)
        > because the ranking will help with triage.
        """
    )
    return


@app.cell
def _(G):
    list(G.neighbors("p1"))
    return


@app.cell
def _(
    G,
    __________,
    ____________,
    ________________________,
    _____________________________,
    ___________________________________,
    ____________________________________,
    bipartite,
    pd,
):
    def find_connected_persons(G, person, crime):
        # Step 0: Check that the given "person" and "crime" are connected.
        if _____________________________:
            raise ValueError(
                f"Graph does not have a connection between {person} and {crime}!"
            )

        # Step 1: calculate weighted projection for person nodes.
        person_nodes = ____________________________________
        person_graph = bipartite.________________________(_, ____________)

        # Step 2: Find neighbors of the given `person` node in projected graph.
        candidate_neighbors = ___________________________________

        # Step 3: Remove candidate neighbors from the set if they are implicated in the given crime.
        for p in G.neighbors(crime):
            if ________________________:
                _____________________________

        # Step 4: Rank-order the candidate neighbors by number of shared connections.
        _________ = []
        ## You might need a for-loop here
        return pd.DataFrame(__________).sort_values("________", ascending=False)

    from nams.solutions.bipartite import find_connected_persons

    find_connected_persons(G, "p2", "c10")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Degree Centrality

        The degree centrality metric is something we can calculate for bipartite graphs.
        Recall that the degree centrality metric is the number of neighbors of a node
        divided by the total number of _possible_ neighbors.

        In a unipartite graph, the denominator can be the total number of nodes less one
        (if self-loops are not allowed)
        or simply the total number of nodes (if self loops _are_ allowed).

        ### Exercise: What is the denominator for bipartite graphs?

        Think about it for a moment, then write down your answer.
        """
    )
    return


@app.cell
def _():
    from nams.solutions.bipartite import bipartite_degree_centrality_denominator
    from nams.functions import render_html

    render_html(bipartite_degree_centrality_denominator())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Exercise: Which `persons` are implicated in the most number of crimes?

        > Find the `persons` (singular or plural) who are connected to the most number of crimes.

        To do so, you will need to use `nx.bipartite.degree_centrality`,
        rather than the regular `nx.degree_centrality` function.

        `nx.bipartite.degree_centrality` requires that you pass in
        a node set from one of the partitions
        so that it can correctly partition nodes on the other set.
        What is returned, though, is the degree centrality
        for nodes in both sets.
        Here is an example to show you how the function is used:

        ```python
        dcs = nx.bipartite.degree_centrality(my_graph, nodes_from_one_partition)
        ```
        """
    )
    return


@app.cell
def _(
    G,
    __________________________,
    ___________________________,
    person_nodes,
):
    def find_most_crime_person(G, person_nodes):
        dcs = __________________________
        return ___________________________

    from nams.solutions.bipartite import find_most_crime_person

    find_most_crime_person(G, person_nodes)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Solutions

        Here are the solutions to the exercises above.
        """
    )
    return


@app.cell
def _(getsource):
    from nams.solutions import bipartite as bipartite_nams

    print(getsource(bipartite_nams))
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
