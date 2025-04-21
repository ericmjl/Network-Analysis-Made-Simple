# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ipython==9.1.0",
#     "marimo",
# ]
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

    YouTubeVideo(id="k4KHoLC7TFE", width="100%")
    return (YouTubeVideo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In our world, networks are an immensely useful _data modelling tool_
        to model complex _relational_ problems.
        Building on top of a network-oriented data model,
        they have been put to great use in a wide variety of settings.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## A _formal_ definition of networks

        Before we explore examples of networks,
        we want to first give you a more formal definition
        of what networks are.
        The reason is that knowing a _formal_ definition
        helps us refine our application of networks.
        So bear with me for a moment.

        In the slightly more academic literature,
        networks are more formally referred to as **graphs**.

        Graphs are comprised of two _sets_ of objects:

        - A **node set**: the "entities" in a graph.
        - An **edge set**: the record of "relationships" between the entities in the graph.

        For example, if a **node set** $n$ is comprised of elements:

        $$n = \{a, b, c, d, ...\}$$

        Then, the **edge set** $e$ would be represented as tuples of _pairs_ of elements:

        $$e = \{(a, b), (a, c), (c, d), ...\}$$

        If you extracted every node from the edge set $e$,
        it should form _at least a subset_ of the node set $n$.
        (It is at least a subset because not every node in $n$ might participate in an edge.)

        If you draw out a network, the "nodes" are commonly represented as shapes, such as circles,
        while the "edges" are the lines between the shapes.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Examples of Networks

        Now that we have a proper definition of a graph,
        let's move on to explore examples of graphs.

        One example I (Eric Ma) am fond of, based on my background as a biologist,
        is a protein-protein interaction network.
        Here, the graph can be defined in the following way:

        - nodes/entities are the proteins,
        - edges/relationships are defined as "one protein is known to bind with another".

        A more colloquial example of networks is an air transportation network.
        Here, the graph can be defined in the following way:

        - nodes/entities are airports
        - edges/relationships are defined as "at least one flight carrier flies between the airports".

        And another even more relatable example would be our ever-prevalent social networks!
        With Twitter, the graph can be defined in the following way:

        - nodes/entities are individual users
        - edges/relationships are defined as "one user has decided to follow another".

        Now that you've seen the framework for defining a graph,
        we'd like to invite you to answer the following question:
        **What examples of networks have _you_ seen before in your profession?**

        Go ahead and list it out.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Types of Graphs

        As you probably can see, graphs are a really flexible data model
        for modelling the world,
        as long as the nodes and edges are strictly defined.
        (If the nodes and edges are _sloppily_ defined,
        well, we run into a lot of interpretability problems later on.)

        If you are a member of both LinkedIn and Twitter,
        you might intuitively think that there's a _slight_ difference
        in the structure of the two "social graphs".
        You'd be absolutely correct on that count!

        Twitter is an example of what we would intuitively call a **directed** graph.
        Why is this so?
        The key here lies in how interactions are modelled.
        One user can follow another, but the other need not necessarily follow back.
        As such, there is a _directionality_ to the relationship.

        LinkedIn is an example of what we would intuitively call an **undirected** graph.
        Why is this so?
        The key here is that when two users are LinkedIn connections,
        we _automatically_ assign a bi-directional edge between them.
        As such, for convenience, we can collapse the bi-directional edge
        into an _undirected_ edge,
        thus yielding an undirected graph.

        If we wanted to turn LinkedIn into a directed graph,
        we might want to keep information on who initiated the invitation.
        In that way, the relationship is automatically bi-directional.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Edges define the interesting part of a graph

        While in graduate school, I (Eric Ma) once sat in a seminar
        organized by one of the professors on my thesis committee.
        The speaker that day was John Quackenbush,
        a faculty member of the Harvard School of Public Health.
        While the topic of the day remained fuzzy in my memory,
        one quote stood out:

        > The heart of a graph lies in its edges, not in its nodes.
        > (John Quackenbush, Harvard School of Public Health)

        Indeed, this is a key point to remember!
        Without edges, the nodes are merely collections of entities.
        In a data table, they would correspond to the rows.
        That alone can be interesting,
        but doesn't yield _relational insights_ between the entities.
        """
    )
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
