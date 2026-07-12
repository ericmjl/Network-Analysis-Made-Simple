import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def _(mo):
    mo.Html(f"""
    <div class="nams-hero">
    <style>
      .nams-hero{{color:#e2e8f0;margin:0;font-family:inherit}}
      .nams-hero__grid{{display:grid;gap:22px;grid-template-columns:minmax(0,1.25fr) minmax(200px,0.85fr);padding:32px 28px;border-radius:14px;background:linear-gradient(135deg,#0f172a 0%,#1e293b 100%)}}
      @media(max-width:760px){{.nams-hero__grid{{grid-template-columns:1fr;padding:22px 16px}}}}
      .nams-badge{{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border:1px solid rgba(52,211,153,0.3);background:rgba(52,211,153,0.1);border-radius:999px;color:#34d399;font-size:0.72rem;font-weight:800;letter-spacing:0.06em;text-transform:uppercase}}
      .nams-hero h1{{margin:14px 0 8px;font-size:2.2rem;line-height:1.05;font-weight:880;letter-spacing:-0.02em;color:#f1f5f9}}
      .nams-hero h1 .nams-em{{color:#34d399}}
      .nams-hero p.lead{{margin:0;max-width:520px;color:#94a3b8;font-size:1.02rem;line-height:1.5}}
      .nams-byline{{margin-top:16px;color:#64748b;font-size:0.88rem;line-height:1.5}}
      .nams-byline b{{color:#cbd5e1}}
      .nams-art{{display:flex;align-items:center;justify-content:center}}
    </style>
    <div class="nams-hero__grid">
      <div>
        <span class="nams-badge">Chapter 01 &middot; Introduction</span>
        <h1>What is a<br><span class="nams-em">Graph?</span></h1>
        <p class="lead">Nodes and edges &mdash; the two atomic ingredients of every network. From protein interactions to Twitter feeds, the same simple building blocks model an astonishing range of real-world systems.</p>
        <div class="nams-byline">Network Analysis Made Simple &middot; <b>Eric Ma</b></div>
      </div>
      <div class="nams-art">
        <svg viewBox="0 0 140 140" style="width:100%;max-width:160px;height:auto">
          <line x1="35" y1="45" x2="100" y2="35" stroke="#34d399" stroke-width="2" opacity="0.35" stroke-linecap="round"/>
          <line x1="35" y1="45" x2="50" y2="100" stroke="#34d399" stroke-width="2" opacity="0.35" stroke-linecap="round"/>
          <line x1="100" y1="35" x2="105" y2="95" stroke="#34d399" stroke-width="2" opacity="0.25" stroke-linecap="round"/>
          <line x1="50" y1="100" x2="105" y2="95" stroke="#34d399" stroke-width="1.5" opacity="0.2" stroke-linecap="round"/>
          <line x1="35" y1="45" x2="105" y2="95" stroke="#34d399" stroke-width="1.5" opacity="0.15" stroke-linecap="round"/>
          <circle cx="35" cy="45" r="9" fill="#34d399" opacity="0.9"/>
          <text x="35" y="28" text-anchor="middle" fill="#6ee7b7" font-size="8" font-weight="700">node</text>
          <circle cx="100" cy="35" r="8" fill="#34d399" opacity="0.8"/>
          <circle cx="50" cy="100" r="7" fill="#10b981" opacity="0.8"/>
          <circle cx="105" cy="95" r="6" fill="#10b981" opacity="0.7"/>
          <text x="68" y="35" text-anchor="middle" fill="#6ee7b7" font-size="7" font-weight="600" opacity="0.8">edge</text>
        </svg>
      </div>
    </div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    import wigglystuff

    tour = wigglystuff.CellTour(
        steps=[
        {'cell': 0, 'title': 'What is a Graph?', 'description': 'The formal definition: nodes and edges.'},
        {'cell': 3, 'title': 'Examples', 'description': 'Protein interactions, air transport, social networks.'},
        {'cell': 4, 'title': 'Types of Graphs', 'description': 'Directed vs undirected: Twitter vs LinkedIn.'},
        {'cell': 5, 'title': 'Edges matter', 'description': 'The heart of a graph lies in its edges, not its nodes.'},
    ],
        auto_start=False,
        show_progress=True,
    )
    mo.ui.anywidget(tour)
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo

    mo.md(r"""
    # Introduction
    """)
    return (mo,)


@app.cell(hide_code=True)
def _():
    from IPython.display import YouTubeVideo

    YouTubeVideo(id="k4KHoLC7TFE", width="100%")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In our world, networks are an immensely useful _data modelling tool_
    to model complex _relational_ problems.
    Building on top of a network-oriented data model,
    they have been put to great use in a wide variety of settings.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
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
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
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
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
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
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
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
    """)
    return


if __name__ == "__main__":
    app.run()
