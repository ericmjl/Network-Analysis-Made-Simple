# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ipython==9.1.0",
#     "marimo",
#     "matplotlib==3.10.1",
#     "nams==0.0.2",
#     "networkx==3.4.2",
#     "nxviz==0.7.6",
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

__generated_with = "0.14.9"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import warnings
    from inspect import getsource

    warnings.filterwarnings("ignore")
    return (getsource,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Introduction""")
    return


@app.cell
def _():
    from IPython.display import YouTubeVideo

    YouTubeVideo(id="3DWSRCbPPJs", width="100%")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    If you remember, at the beginning of this book,
    we saw a quote from John Quackenbush that essentially said
    that the reason a graph is interesting is because of its edges.
    In this chapter, we'll see this in action once again,
    as we are going to figure out how to leverage the edges
    to find special _structures_ in a graph.

    ## Triangles

    The first structure that we are going to learn about is **triangles**.
    Triangles are super interesting!
    They are what one might consider to be
    "the simplest complex structure" in a graph.
    Triangles can also have semantically-rich meaning depending on the application.
    To borrow a bad example, love triangles in social networks are generally frowned upon,
    while on the other hand, when we connect two people that we know together,
    we instead _complete_ a triangle.

    ### Load Data

    To learn about triangles,
    we are going to leverage a physician trust network.
    Here's the data description:

    > This directed network captures innovation spread among 246 physicians
    > for towns in Illinois, Peoria, Bloomington, Quincy and Galesburg.
    > The data was collected in 1966.
    > A node represents a physician and an edge between two physicians
    > shows that the left physician told that the right physician is his friend
    > or that he turns to the right physician if he needs advice
    > or is interested in a discussion.
    > There always only exists one edge between two nodes
    > even if more than one of the listed conditions are true.
    """
    )
    return


@app.cell
def _():
    from nams import load_data as cf

    G = cf.load_physicians_network()
    return (G,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise: Finding triangles in a graph

    This exercise is going to flex your ability
    to "think on a graph", just as you did in the previous chapters.

    > Leveraging what you know, can you think of a few strategies
    > to find triangles in a graph?
    """
    )
    return


@app.cell
def _():
    from nams.solutions.structures import triangle_finding_strategies

    # triangle_finding_strategies()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise: Identify whether a node is in a triangle relationship or not

    Let's now get down to implementing this next piece of code.

    > Write a function that identifies whether a node is or is not in a triangle relationship.
    > It should take in a graph `G` and a node `n`,
    > and return a boolean True if the node `n` is in any triangle relationship
    > and boolean False if the node `n` is not in any triangle relationship.

    A hint that may help you:

    > Every graph object `G` has a `G.has_edge(n1, n2)` method that you can use to identify whether a graph has an edge between `n1` and `n2`.

    Also:

    > `itertools.combinations` lets you iterate over every _K-combination_ of items in an iterable.
    """
    )
    return


@app.cell
def _():
    def in_triangle(G, node):
        # Your answer here
        pass


    # COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER
    from nams.solutions.structures import in_triangle

    # UNCOMMENT THE NEXT LINE TO SEE MY ANSWER
    # print(getsource(in_triangle))
    return (in_triangle,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Now, test your implementation below!
    The code cell will not error out if your answer is correct.
    """
    )
    return


@app.cell
def _(G, in_triangle):
    from random import sample
    import networkx as nx


    def test_in_triangle():
        nodes = sample(list(G.nodes()), 10)
        for node in nodes:
            assert in_triangle(G, 3) == bool(nx.triangles(G, 3))


    test_in_triangle()
    return (nx,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    As you can see from the test function above,
    NetworkX provides an `nx.triangles(G, node)` function.
    It returns the number of triangles that a node is involved in.
    We convert it to boolean as a hack to check whether or not
    a node is involved in a triangle relationship
    because 0 is equivalent to boolean `False`,
    while any non-zero number is equivalent to boolean `True`.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise: Extract triangles for plotting

    We're going to leverage another piece of knowledge that you already have:
    the ability to extract subgraphs.
    We'll be plotting all of the triangles that a node is involved in.

    > Given a node, write a function that extracts out
    > all of the neighbors that it is in a triangle relationship with.
    > Then, in a new function,
    > implement code that plots only the subgraph
    > that contains those nodes.
    """
    )
    return


@app.cell
def _(getsource):
    def get_triangle_neighbors(G, n):
        # Your answer here
        pass


    # COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER
    from nams.solutions.structures import get_triangle_neighbors

    # UNCOMMENT THE NEXT LINE TO SEE MY ANSWER
    print(getsource(get_triangle_neighbors))
    return


@app.cell
def _(G, plt):
    def plot_triangle_relations(G, n):
        # Your answer here
        pass


    # COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER
    from nams.solutions.structures import plot_triangle_relations

    plot_triangle_relations(G, 3)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Triadic Closure

    In professional circles, making connections between two people
    is one of the most valuable things you can do professionally.
    What you do in that moment is what we would call
    **triadic closure**.
    Algorithmically, we can do the same thing
    if we maintain a graph of connections!

    Essentially, what we are looking for
    are "open" or "unfinished" triangles".

    In this section, we'll try our hand at implementing
    a rudimentary triadic closure system.

    ### Exercise: Design the algorithm

    > What graph logic would you use to identify triadic closure opportunities?
    > Try writing out your general strategy, or discuss it with someone.
    """
    )
    return


@app.cell
def _():
    from nams.solutions.structures import triadic_closure_algorithm

    # UNCOMMENT FOR MY ANSWER
    # triadic_closure_algorithm()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise: Implement triadic closure.

    Now, try your hand at implementing triadic closure.

    > Write a function that takes in a graph `G` and a node `n`,
    > and returns all of the neighbors that are potential triadic closures
    > with `n` being the center node.
    """
    )
    return


@app.cell
def _():
    def get_open_triangles_neighbors(G, n):
        # Your answer here
        pass


    # COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER
    from nams.solutions.structures import get_open_triangles_neighbors

    # UNCOMMENT THE NEXT LINE TO SEE MY ANSWER
    # get_open_triangles_neighbors??
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise: Plot the open triangles

    > Now, write a function that takes in a graph `G` and a node `n`,
    > and plots out that node `n` and all of the neighbors
    > that it could help close triangles with.
    """
    )
    return


@app.cell
def _(G, plt):
    def plot_open_triangle_relations(G, n):
        # Your answer here
        pass


    # COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER
    from nams.solutions.structures import plot_open_triangle_relations

    plot_open_triangle_relations(G, 3)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Cliques

    Triangles are interesting in a graph theoretic setting
    because triangles are the simplest complex clique that exist.

    But wait!
    What is the definition of a "clique"?

    > A "clique" is a set of nodes in a graph
    > that are fully connected with one another
    > by edges between them.

    ### Exercise: Simplest cliques

    Given this definition, what is the simplest "clique" possible?
    """
    )
    return


@app.cell
def _():
    from nams.solutions.structures import simplest_clique

    # UNCOMMENT THE NEXT LINE TO SEE MY ANSWER
    # simplest_clique()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### $k$-Cliques

    Cliques are identified by their size $k$,
    which is the number of nodes that are present in the clique.

    A triangle is what we would consider to be a $k$-clique where $k=3$.

    A square with cross-diagonal connections is what we would consider to be
    a $k$-clique where $k=4$.

    By now, you should get the gist of the idea.

    ### Maximal Cliques

    Related to this idea of a $k$-clique is another idea called "maximal cliques".

    Maximal cliques are defined as follows:

    > A maximal clique is a subgraph of nodes in a graph
    >
    > 1. to which no other node can be added to it and
    > 2. still remain a clique.

    NetworkX provides a way to find all maximal cliques:
    """
    )
    return


@app.cell
def _(G, nx):
    # I have truncated the output to the first 5 maximal cliques.
    list(nx.find_cliques(G))[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise: finding sized-$k$ maximal cliques

    > Write a generator function that yields all maximal cliques of size $k$.

    I'm requesting a generator as a matter of good practice;
    you never know when the list you return might explode in memory consumption,
    so generators are a cheap and easy way to reduce memory usage.
    """
    )
    return


@app.cell
def _():
    def size_k_maximal_cliques(G, k):
        # Your answer here
        pass


    # COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER
    from nams.solutions.structures import size_k_maximal_cliques
    return (size_k_maximal_cliques,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Now, test your implementation against the test function below.""")
    return


@app.cell
def _(G, size_k_maximal_cliques):
    def test_size_k_maximal_cliques(G, k):
        clique_generator = size_k_maximal_cliques(G, k)
        for clique in clique_generator:
            assert len(clique) == k


    test_size_k_maximal_cliques(G, 5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Clique Decomposition

    One _super_ neat property of cliques
    is that every clique of size $k$
    can be decomposed to the set of cliques of size $k-1$.

    Does this make sense to you?
    If not, think about triangles (3-cliques).
    They can be decomposed to three edges (2-cliques).

    Think again about 4-cliques.
    Housed within 4-cliques are four 3-cliques.
    _Draw it out if you're still not convinced!_
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise: finding all $k$-cliques in a graph

    > Knowing this property of $k$-cliques,
    > write a generator function that yields all $k$-cliques in a graph,
    > leveraging the `nx.find_cliques(G)` function.

    Some hints to help you along:

    > If a $k$-clique can be decomposed to its $k-1$ cliques,
    > it follows that the $k-1$ cliques can be decomposed into $k-2$ cliques,
    > and so on until you hit 2-cliques.
    > This implies that all cliques of size $k$
    > house cliques of size $n < k$, where $n >= 2$.
    """
    )
    return


@app.cell
def _(G):
    def find_k_cliques(G, k):
        # your answer here
        pass


    # COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER
    from nams.solutions.structures import find_k_cliques


    def test_find_k_cliques(G, k):
        for clique in find_k_cliques(G, k):
            assert len(clique) == k


    test_find_k_cliques(G, 3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Connected Components

    Now that we've explored a lot around cliques,
    we're now going to explore this idea of "connected components".
    To do so, I am going to have you draw the graph
    that we are working with.
    """
    )
    return


@app.cell
def _(G):
    import nxviz as nv

    nv.arc(G)
    return (nv,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise: Visual insights

    From this rendering of the CircosPlot,
    what visual insights do you have about the structure of the graph?
    """
    )
    return


@app.cell
def _():
    from nams.solutions.structures import visual_insights

    # UNCOMMENT TO SEE MY ANSWER
    # visual_insights()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Defining connected components

    From [Wikipedia](https://en.wikipedia.org/wiki/Connected_component_%28graph_theory%29):

    > In graph theory, a connected component (or just component) of an undirected graph is a subgraph in which any two vertices are connected to each other by paths, and which is connected to no additional vertices in the supergraph.

    NetworkX provides a function to let us find all of the connected components:
    """
    )
    return


@app.cell
def _(G, nx):
    ccsubgraph_nodes = list(nx.connected_components(G))
    return (ccsubgraph_nodes,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Let's see how many connected component subgraphs are present:""")
    return


@app.cell
def _(ccsubgraph_nodes):
    len(ccsubgraph_nodes)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise: visualizing connected component subgraphs

    In this exercise, we're going to draw a circos plot of the graph,
    but colour and order the nodes by their connected component subgraph.

    Recall Circos API:

    ```python
    c = CircosPlot(G, node_order='node_attribute', node_color='node_attribute')
    c.draw()
    plt.show()  # or plt.savefig(...)
    ```

    Follow the steps along here to accomplish this.

    > Firstly, label the nodes with a unique identifier for connected component subgraph
    > that it resides in.
    > Use `subgraph` to store this piece of metadata.
    """
    )
    return


@app.cell
def _(G):
    def label_connected_component_subgraphs(G):
        # Your answer here
        return G


    # COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER
    from nams.solutions.structures import label_connected_component_subgraphs

    G_labelled = label_connected_component_subgraphs(G)

    # UNCOMMENT TO SEE THE ANSWER
    # print(getsource(label_connected_component_subgraphs))
    return (G_labelled,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    > Now, draw a CircosPlot with the node order and colouring
    > dictated by the `subgraph` key.
    """
    )
    return


@app.cell
def _(G_labelled):
    import matplotlib.pyplot as plt


    def plot_cc_subgraph(G):
        # Your answer here
        pass


    # COMMENT OUT THE IMPORT LINE TO TEST YOUR ANSWER
    from nams.solutions.structures import plot_cc_subgraph
    from nxviz import annotate

    plot_cc_subgraph(G_labelled)
    annotate.circos_group(G_labelled, group_by="subgraph")
    plt.show()
    return annotate, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Using an arc plot will also clearly illuminate for us
    that there are no inter-group connections.
    """
    )
    return


@app.cell
def _(G_labelled, annotate, nv, plt):
    nv.arc(G_labelled, group_by="subgraph", node_color_by="subgraph")
    annotate.arc_group(G_labelled, group_by="subgraph", rotation=0)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""_Voila!_ It looks quite clear that there are indeed four disjoint group of physicians."""
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Discussion question

    This was from an innovation graph from 1960s. What would you expect the structure to look like in 2025?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Solutions""")
    return


@app.cell
def _(getsource):
    from nams.solutions import structures

    print(getsource(structures))
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
