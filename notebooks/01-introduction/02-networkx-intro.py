# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ipython==9.1.0",
#     "marimo",
#     "matplotlib==3.10.1",
#     "nams==0.0.2",
#     "networkx==3.4.2",
#     "numpy==2.2.5",
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

__generated_with = "0.12.2"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""# Introduction""")
    return


@app.cell(hide_code=True)
def _():
    from IPython.display import YouTubeVideo

    YouTubeVideo(id="sdF0uJo2KdU", width="100%")
    return (YouTubeVideo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In this chapter, we will introduce you to the NetworkX API.
        This will allow you to create and manipulate graphs in your computer memory,
        thus giving you a language
        to more concretely explore graph theory ideas.

        Throughout the book, we will be using different graph datasets
        to help us anchor ideas.
        In this section, we will work with a social network of seventh graders.
        Here, nodes are individual students,
        and edges represent their relationships.
        Edges between individuals show how often
        the seventh graders indicated other seventh graders as their favourite.

        The data are taken from the [Konect] graph data repository

        [Konect]: http://konect.cc/networks/moreno_seventh
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Data Model

        In NetworkX, graph data are stored in a dictionary-like fashion.
        They are placed under a `Graph` object,
        canonically instantiated with the variable `G` as follows:

        ```python
        G = nx.Graph()
        ```

        Of course, you are free to name the graph anything you want!

        Nodes are part of the attribute `G.nodes`.
        There, the node data are housed in a dictionary-like container,
        where the key is the node itself
        and the values are a dictionary of attributes.
        Node data are accessible using syntax that looks like:

        ```python
        G.nodes[node1]
        ```

        Edges are part of the attribute `G.edges`,
        which is also stored in a dictionary-like container.
        Edge data are accessible using syntax that looks like:

        ```python
        G.edges[node1, node2]
        ```
        Because of the dictionary-like implementation of the graph,
        any hashable object can be a node.
        This means strings and tuples, but not lists and sets.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Load Data

        Let's load some real network data to get a feel for the NetworkX API. This [dataset](http://konect.cc/networks/moreno_seventh) comes from a study of 7th grade students.

        > This directed network contains proximity ratings between students
        > from 29 seventh grade students from a school in Victoria.
        > Among other questions the students were asked
        > to nominate their preferred classmates for three different activities.
        > A node represents a student.
        > An edge between two nodes shows that
        > the left student picked the right student as his or her answer.
        > The edge weights are between 1 and 3
        > and show how often the left student chose the right student as his/her favourite.

        In the original dataset, students were from an all-boys school.
        However, I have modified the dataset to instead be a mixed-gender school.
        """
    )
    return


@app.cell
def _():
    import networkx as nx
    from datetime import datetime
    import matplotlib.pyplot as plt
    import numpy as np
    import warnings
    from nams import load_data as cf

    warnings.filterwarnings("ignore")
    return cf, datetime, np, nx, plt, warnings


@app.cell
def _(cf):
    G = cf.load_seventh_grader_network()
    return (G,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Understanding a graph's basic statistics

        When you get graph data,
        one of the first things you'll want to do is to
        check its basic graph statistics:
        the number of nodes
        and the number of edges
        that are represented in the graph.
        This is a basic sanity-check on your data
        that you don't want to skip out on.

        ### Querying graph type

        The first thing you need to know is the `type` of the graph:
        """
    )
    return


@app.cell
def _(G):
    type(G)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Because the graph is a `DiGraph`,
        this tells us that the graph is a **directed** one.

        If it were undirected, the type would change:
        """
    )
    return


@app.cell
def _(nx):
    H = nx.Graph()
    type(H)
    return (H,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Querying node information

        Let's now query for the nodeset:
        """
    )
    return


@app.cell
def _(G):
    list(G.nodes())[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        `G.nodes()` returns a "view" on the nodes.
        We can't actually slice into the view and grab out a sub-selection,
        but we can _at least_ see what nodes are present.
        For brevity, we have sliced into `G.nodes()` passed into a `list()` constructor,
        so that we don't pollute the output.
        Because a `NodeView` is iterable, though,
        we can query it for its length:
        """
    )
    return


@app.cell
def _(G):
    len(G.nodes())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        If our nodes have metadata attached to them,
        we can view the metadata at the same time
        by passing in `data=True`:
        """
    )
    return


@app.cell
def _(G):
    list(G.nodes(data=True))[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        G.nodes(data=True) returns a `NodeDataView`,
        which you can see is dictionary-like.

        Additionally, we can select out individual nodes:
        """
    )
    return


@app.cell
def _(G):
    G.nodes[1]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Now, because a `NodeDataView` is dictionary-like,
        looping over `G.nodes(data=True)`
        is very much like looping over key-value pairs of a dictionary.
        As such, we can write things like:

        ```python
        for n, d in G.nodes(data=True):
            # n is the node
            # d is the metadata dictionary
            ...
        ```

        This is analogous to how we would loop over a dictionary:

        ```python
        for k, v in dictionary.items():
            # do stuff in the loop
        ```

        Naturally, this leads us to our first exercise.

        ### Exercise: Summarizing node metadata

        > Can you count how many males and females are represented in the graph?
        """
    )
    return


@app.cell
def _(G):
    from nams.solutions.intro import node_metadata

    #### REPLACE THE NEXT LINE WITH YOUR ANSWER
    mf_counts = node_metadata(G)
    return mf_counts, node_metadata


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""Test your implementation by checking it against the `test_answer` function below."""
    )
    return


@app.cell
def _(mf_counts):
    from typing import Dict

    def test_answer(mf_counts: Dict):
        assert mf_counts["female"] == 17
        assert mf_counts["male"] == 12

    test_answer(mf_counts)
    return Dict, test_answer


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        With this dictionary-like syntax,
        we can query back the metadata that's associated with any node.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Querying edge information

        Now that you've learned how to query for node information,
        let's now see how to query for all of the edges in the graph:
        """
    )
    return


@app.cell
def _(G):
    list(G.edges())[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        Similar to the `NodeView`, `G.edges()` returns an `EdgeView` that is also iterable.
        As with above, we have abbreviated the output inside a sliced list
        to keep things readable.
        Because `G.edges()` is iterable, we can get its length to see the number of edges
        that are present in a graph.
        """
    )
    return


@app.cell
def _(G):
    len(G.edges())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Likewise, we can also query for all of the edge's metadata:""")
    return


@app.cell
def _(G):
    list(G.edges(data=True))[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""Additionally, it is possible for us to select out individual edges, as long as they exist in the graph:"""
    )
    return


@app.cell
def _(G):
    G.edges[15, 10]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        This yields the metadata dictionary for that edge.

        If the edge does not exist, then we get an error:

        ```python
        >>> G.edges[15, 16]
        ```

        ```python
        ---------------------------------------------------------------------------
        KeyError                                  Traceback (most recent call last)
        <ipython-input-21-ce014cab875a> in <module>
        ----> 1 G.edges[15, 16]

        ~/anaconda/envs/nams/lib/python3.7/site-packages/networkx/classes/reportviews.py in __getitem__(self, e)
            928     def __getitem__(self, e):
            929         u, v = e
        --> 930         return self._adjdict[u][v]
            931
            932     # EdgeDataView methods

        KeyError: 16
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        As with the `NodeDataView`, the `EdgeDataView` is dictionary-like,
        with the difference being that the keys are 2-tuple-like
        instead of being single hashable objects.
        Thus, we can write syntax like the following to loop over the edgelist:

        ```python
        for n1, n2, d in G.edges(data=True):
            # n1, n2 are the nodes
            # d is the metadata dictionary
            ...
        ```

        Naturally, this leads us to our next exercise.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Exercise: Summarizing edge metadata

        > Can you write code to verify
        > that the maximum times any student rated another student as their favourite
        > is 3 times?
        """
    )
    return


@app.cell
def _(G):
    from nams.solutions.intro import edge_metadata

    #### REPLACE THE NEXT LINE WITH YOUR ANSWER
    maxcount = edge_metadata(G)
    return edge_metadata, maxcount


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Likewise, you can test your answer using the test function below:""")
    return


@app.cell
def _(maxcount):
    def test_maxcount(maxcount):
        assert maxcount == 3

    test_maxcount(maxcount)
    return (test_maxcount,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Manipulating the graph

        Great stuff! You now know how to query a graph for:

        - its node set, optionally including metadata
        - individual node metadata
        - its edge set, optionally including metadata, and
        - individual edges' metadata

        Now, let's learn how to manipulate the graph.
        Specifically, we'll learn how to add nodes and edges to a graph.

        ### Adding Nodes

        The NetworkX graph API lets you add a node easily:

        ```python
        G.add_node(node, node_data1=some_value, node_data2=some_value)
        ```

        ### Adding Edges

        It also allows you to add an edge easily:

        ```python
        G.add_edge(node1, node2, edge_data1=some_value, edge_data2=some_value)
        ```

        ### Metadata by Keyword Arguments

        In both cases, the keyword arguments that are passed into `.add_node()`
        are automatically collected into the metadata dictionary.

        Knowing this gives you enough knowledge to tackle the next exercise.

        ### Exercise: adding students to the graph

        > We found out that there are two students that we left out of the network,
        > student no. 30 and 31.
        > They are one male (30) and one female (31),
        > and they are a pair that just love hanging out with one another
        > and with individual 7 (i.e. `count=3`), in both directions per pair.
        > Add this information to the graph.
        """
    )
    return


@app.cell
def _(G):
    from nams.solutions.intro import adding_students

    G_1 = adding_students(G)
    return G_1, adding_students


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        You can verify that the graph has been correctly created
        by executing the test function below.
        """
    )
    return


@app.cell
def _(G_1):
    def test_graph_integrity(G):
        assert 30 in G.nodes()
        assert 31 in G.nodes()
        assert G.nodes[30]["gender"] == "male"
        assert G.nodes[31]["gender"] == "female"
        assert G.has_edge(30, 31)
        assert G.has_edge(30, 7)
        assert G.has_edge(31, 7)
        assert G.edges[30, 7]["count"] == 3
        assert G.edges[7, 30]["count"] == 3
        assert G.edges[31, 7]["count"] == 3
        assert G.edges[7, 31]["count"] == 3
        assert G.edges[30, 31]["count"] == 3
        assert G.edges[31, 30]["count"] == 3
        print("All tests passed.")

    test_graph_integrity(G_1)
    return (test_graph_integrity,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Coding Patterns

        These are some recommended coding patterns when doing network analysis using NetworkX,
        which stem from my personal experience with the package.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Iterating using List Comprehensions
        I would recommend that you use the following for compactness:

        ```python
        [d['attr'] for n, d in G.nodes(data=True)]
        ```

        And if the node is unimportant, you can do:

        ```python
        [d['attr'] for _, d in G.nodes(data=True)]
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Iterating over Edges using List Comprehensions

        A similar pattern can be used for edges:

        ```python
        [n2 for n1, n2, d in G.edges(data=True)]
        ```

        or

        ```python
        [n2 for _, n2, d in G.edges(data=True)]
        ```

        If the graph you are constructing is a directed graph,
        with a "source" and "sink" available,
        then I would recommend the following naming of variables instead:

        ```python
        [(sc, sk) for sc, sk, d in G.edges(data=True)]
        ```

        or

        ```python
        [d['attr'] for sc, sk, d in G.edges(data=True)]
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Further Reading

        For a deeper look at the NetworkX API,
        be sure to check out the [NetworkX docs][nxdocs].

        [nxdocs]: https://networkx.readthedocs.io
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Further Exercises

        Here's some further exercises that you can use to get some practice.

        ### Exercise: Unrequited Friendships

        > Try figuring out which students have "unrequited" friendships, that is,
        > they have rated another student as their favourite at least once,
        > but that other student has not rated them as their favourite at least once.

        _Hint: the goal here is to get a list of edges for which the reverse edge is not present._

        _Hint: You may need the class method `G.has_edge(n1, n2)`. This returns whether a graph has an edge between the nodes `n1` and `n2`._
        """
    )
    return


@app.cell
def _(G_1):
    from nams.solutions.intro import unrequitted_friendships_v1

    unrequitted_friendships = unrequitted_friendships_v1(G_1)
    assert len(unrequitted_friendships) == 124
    return unrequitted_friendships, unrequitted_friendships_v1


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In a previous session at ODSC East 2018, a few other class participants provided the following solutions,
        which you can take a look at by uncommenting the following cells.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""This first one by [@schwanne](https://github.com/schwanne) is the list comprehension version of the above solution:"""
    )
    return


@app.cell
def _():
    from nams.solutions.intro import unrequitted_friendships_v2
    from inspect import getsource

    # print(getsource(unrequitted_friendships_v2))
    return getsource, unrequitted_friendships_v2


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""This one by [@end0](https://github.com/end0) is a unique one involving sets."""
    )
    return


@app.cell
def _():
    from nams.solutions.intro import unrequitted_friendships_v3

    # print(getsource(unrequitted_friendships_v3))
    return (unrequitted_friendships_v3,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Solution Answers

        Here are the answers to the exercises above.
        """
    )
    return


@app.cell
def _():
    import nams.solutions.intro as solutions
    import inspect

    # print(inspect.getsource(solutions))
    return inspect, solutions


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
