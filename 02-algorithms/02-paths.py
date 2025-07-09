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
#     "seaborn==0.13.2",
#     "tqdm==4.67.1",
# ]
# [tool.uv.sources]
# nams = { path = "../../", editable = true }
# ///

import marimo

__generated_with = "0.14.8"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import warnings

    warnings.filterwarnings("ignore")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Introduction""")
    return


@app.cell(hide_code=True)
def _():
    from IPython.display import YouTubeVideo

    YouTubeVideo(id="JjpbztqP9_0", width="100%")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## What makes a node important?

    In the previous notebook, we explored degree centrality as a measure of node importance.
    What other ways can we measure node importance?
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Graph traversal and node importance

    Graph traversal is akin to walking along the graph, node by node,
    constrained by the edges that connect the nodes.
    Graph traversal is particularly useful for understanding
    the local structure of certain portions of the graph
    and for finding paths that connect two nodes in the network.

    In this chapter, we are going to learn how to perform pathfinding in a graph,
    specifically by looking for _shortest paths_ via the _breadth-first search_ algorithm.
    Then, we are going to explore measures of node importance that are related to traversals on a graph!
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Breadth-First Search

    The BFS algorithm is a staple of computer science curricula,
    and for good reason:
    it teaches learners how to "think on" a graph,
    putting one in the position of
    "the dumb computer" that can't use a visual cortex to
    "_just know_" how to trace a path from one node to another.
    As a topic, learning how to do BFS
    additionally imparts algorithmic thinking to the learner.

    ### Exercise: Design the algorithm

    Try out this exercise to get some practice with algorithmic thinking.

    > 1. On a piece of paper, conjure up a graph that has 15-20 nodes. Connect them any way you like.
    > 1. Pick two nodes. Pretend that you're standing on one of the nodes, but you can't see any further beyond one neighbor away.
    > 1. Work out how you can find _a_ path from the node you're standing on to the other node, given that you can _only_ see nodes that are one neighbor away but have an infinitely good memory.

    If you are successful at designing the algorithm, you should get the answer below.
    """
    )
    return


@app.cell
def _():
    from nams import load_data as cf

    G = cf.load_sociopatterns_network()
    return (G,)


@app.cell
def _():
    from nams.solutions.paths import bfs_algorithm

    # UNCOMMENT NEXT LINE TO GET THE ANSWER.
    # bfs_algorithm()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise: Implement the algorithm

    > Now that you've seen how the algorithm works, try implementing it!
    """
    )
    return


@app.cell
def _(____, _____, _________, ___________, _____________, _________________):
    # FILL IN THE BLANKS BELOW


    def path_exists(node1, node2, G):
        """
        This function checks whether a path exists between two nodes (node1,
        node2) in graph G.
        """
        visited_nodes = _____  # should be a set
        # Initialize with starting node.
        queue = [_____]  # do NOT change to a set, trust me, order matters!

        while len(queue) > 0:
            # Pick the next node for which to check neighbors.
            node = ___________

            # Now get the neighbors of that node
            neighbors = list(_________________)

            # Check if the destination is in the neighbors
            if _____ in _________:
                print("Path exists between nodes {0} and {1}".format(node1, node2))
                return True
            else:
                # Add current node to visited nodes
                visited_nodes.___(____)
                # You want to add nodes that don't already exist in visited_
                nbrs = [_ for _ in _________ if _ not in _____________]

                # Add the neighbors to the queue.
                queue = ____ + _____

        # print('Path does not exist between nodes {0} and {1}'.format(node1, node2))
        return False
    return (path_exists,)


@app.cell
def _():
    # UNCOMMENT THE FOLLOWING TWO LINES TO SEE THE ANSWER
    from nams.solutions.paths import path_exists as path_exists_solution
    from inspect import getsource

    print(getsource(path_exists_solution))
    return


@app.cell
def _(G, path_exists):
    from random import sample
    import networkx as nx


    def test_path_exists(N):
        """
        N: The number of times to spot-check.
        """
        for i in range(N):
            n1, n2 = sample(list(G.nodes()), 2)
            assert path_exists(n1, n2, G) == bool(nx.shortest_path(G, n1, n2))
        return True


    # Uncomment the next line to check the tests.
    # assert test_path_exists(10)
    return (nx,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Visualizing Paths

    One of the objectives of that exercise before was to help you "think on graphs".
    Now that you've learned how to do so, you might be wondering,
    "How do I visualize that path through the graph?"

    Well first off, if you inspect the `test_path_exists` function above,
    you'll notice that NetworkX provides a `shortest_path()` function
    that you can use. Here's what using `nx.shortest_path()` looks like.
    """
    )
    return


@app.cell
def _(G, nx):
    path = nx.shortest_path(G, 7, 400)
    path
    return (path,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    As you can see, it returns the nodes along the shortest path,
    incidentally in the exact order that you would traverse.

    One thing to note, though!
    If there are multiple shortest paths from one node to another,
    NetworkX will only return one of them.

    So how do you draw those nodes _only_?

    You can use the `G.subgraph(nodes)`
    to return a new graph that only has nodes in `nodes`
    and only the edges that exist between them.
    After that, you can use any plotting library you like.
    We will show an example here that uses nxviz's matrix plot.

    Let's see it in action:
    """
    )
    return


@app.cell
def _(G, path, plt):
    import nxviz as nv

    g = G.subgraph(path)
    nv.matrix(g, sort_by="order")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    _Voila!_ Now we have the subgraph (1) extracted and (2) drawn to screen!
    In this case, the matrix plot is a suitable visualization for its compactness.
    The off-diagonals also show that each node is a neighbor to the next one.

    You'll also notice that if you try to modify the graph `g`, say by adding a node:

    ```python
    g.add_node(2048)
    ```

    you will get an error:

    ```python
    ---------------------------------------------------------------------------
    NetworkXError                             Traceback (most recent call last)
    <ipython-input-10-ca6aa4c26819> in <module>
    ----> 1 g.add_node(2048)

    ~/anaconda/envs/nams/lib/python3.7/site-packages/networkx/classes/function.py in frozen(*args, **kwargs)
        156 def frozen(*args, **kwargs):
        157     \"\"\"Dummy method for raising errors when trying to modify frozen graphs\"\"\"
    --> 158     raise nx.NetworkXError("Frozen graph can't be modified")
        159
        160

    NetworkXError: Frozen graph can't be modified
    ```

    From the perspective of semantics, this makes a ton of sense:
    the subgraph `g` is a perfect subset of the larger graph `G`,
    and should not be allowed to be modified
    unless the larger container graph is modified.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### (Optional) Exercise: Draw path with neighbors of the path nodes

    If there's enough time, we will work through this exercise. If not, we will simply discuss the plot.

    Try out this next puzzle 🧩:

    > Plot an arc plot, in which all nodes from G are ordered on the x-axis.
    > Make a subgraph of the path nodes + their neighbors,
    > and then plot the edges in the arc plot.
    > Finally, highlight the path in red.

    This one is advanced, and if you need to peek at the answer, please feel free to do so.
    """
    )
    return


@app.cell
def _(plt):
    from nams.solutions.paths import plot_path_with_neighbors


    def plot_path_with_neighbors_answer(G, node1, node2):
        # Your answer here
        plt.show()


    # Now execute `plot_path_with_neighbors_answer`
    return (plot_path_with_neighbors,)


@app.cell
def _(G, plot_path_with_neighbors, plt):
    plot_path_with_neighbors(G, 7, 400)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In this case, we opted for an Arc plot because we only have one grouping of nodes but have a logical way to order them.
    Because the path follows the order, the edges being highlighted automatically look like hops through the graph.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Bottleneck nodes

    We're now going to revisit the concept of an "important node",
    this time now leveraging what we know about paths.

    In the "hubs" chapter, we saw how a node that is "important"
    could be so because it is connected to many other nodes.

    Paths give us an alternative definition.
    If we imagine that we have to pass a message on a graph
    from one node to another,
    then there may be "bottleneck" nodes
    for which if they are removed,
    then messages have a harder time flowing through the graph.

    One metric that measures this form of importance
    is the "betweenness centrality" metric.
    On a graph through which a generic "message" is flowing,
    a node with a high betweenness centrality
    is one that has a high proportion of shortest paths
    flowing through it.
    In other words, it behaves like a _bottleneck_.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Betweenness centrality in NetworkX

    NetworkX provides a "betweenness centrality" function
    that behaves consistently with the "degree centrality" function,
    in that it returns a mapping from node to metric:
    """
    )
    return


@app.cell
def _(G, nx):
    import pandas as pd

    pd.Series(nx.betweenness_centrality(G))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise: compare degree and betweenness centrality

    > Make a scatterplot of degree centrality on the x-axis
    > and betweenness centrality on the y-axis.
    > Do they correlate with one another?
    """
    )
    return


@app.cell
def _():
    import matplotlib.pyplot as plt
    import seaborn as sns

    # YOUR ANSWER HERE:
    return (plt,)


@app.cell
def _(G, plt):
    from nams.solutions.paths import plot_degree_betweenness

    plot_degree_betweenness(G)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Think about it...

    ...does it make sense that degree centrality and betweenness centrality
    are not well-correlated?

    Can you think of a scenario where a node has a
    "high" betweenness centrality
    but a "low" degree centrality?
    Before peeking at the graph below,
    think about your answer for a moment.
    """
    )
    return


@app.cell
def _(nx, plt):
    nx.draw(nx.barbell_graph(10, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Recap

    In this chapter, you learned the following things:

    1. You figured out how to implement the breadth-first-search algorithm to find shortest paths.
    1. You learned how to extract subgraphs from a larger graph.
    1. You implemented visualizations of subgraphs, which should help you as you communicate with colleagues.
    1. You calculated betweenness centrality metrics for a graph, and visualized how they correlated with degree centrality.
    """
    )
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
def _():
    from nams.solutions import paths
    import inspect

    print(inspect.getsource(paths))
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
