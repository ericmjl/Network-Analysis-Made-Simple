import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def hero(mo):
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
def cell_tour(mo):
    import wigglystuff

    tour = wigglystuff.CellTour(
        steps=[
        {'cell': 0, 'title': 'What is a Graph?', 'description': 'Nodes and edges — the two atomic ingredients of every network.'},
        {'cell': 2, 'title': 'Introduction', 'description': 'Networks as a data modelling tool for complex relational problems.'},
        {'cell': 5, 'title': 'Formal Definition', 'description': 'A graph is formally defined as a node set and an edge set of pairs.'},
        {'cell': 6, 'title': 'Examples of Networks', 'description': 'Protein interactions, air transport, and social networks share the same building blocks.'},
        {'cell': 7, 'title': 'Types of Graphs', 'description': 'Directed graphs like Twitter vs undirected graphs like LinkedIn.'},
        {'cell': 8, 'title': 'Edges Matter Most', 'description': 'The heart of a graph lies in its edges, not its nodes — relational insight comes from connections.'},
    ],
        auto_start=False,
        show_progress=True,
    )
    mo.ui.anywidget(tour)
    return


@app.cell(hide_code=True)
def intro():
    import marimo as mo

    mo.md(r"""
    # Introduction
    """)
    return (mo,)


@app.cell(hide_code=True)
def video(mo):
    mo.md("""
    Watch the [video introduction on YouTube](https://www.youtube.com/watch?v=k4KHoLC7TFE).
    """)
    return


@app.cell(hide_code=True)
def networks_motivation(mo):
    mo.md(r"""
    In our world, networks are an immensely useful _data modelling tool_
    to model complex _relational_ problems.
    Building on top of a network-oriented data model,
    they have been put to great use in a wide variety of settings.
    """)
    return


@app.cell(hide_code=True)
def formal_definition(mo):
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
def examples(mo):
    mo.vstack(
        [
            mo.md("""
    ## Examples of Networks

    Now that we have a proper definition of a graph,
    let's move on to explore examples of graphs.

    One example I (Eric Ma) am fond of, based on my background as a biologist,
    is a **protein-protein interaction network**.
    A more colloquial example is an **air transportation network**.
    And another even more relatable example would be our ever-prevalent
    **social networks** like Twitter.

    Hover each card below to see how each system maps onto nodes and edges.
    """),
            mo.Html("""
    <style>
    .nams-cards{display:flex;gap:16px;flex-wrap:wrap;justify-content:center;margin:8px 0}
    .nams-card{width:180px;height:200px;perspective:800px;cursor:pointer}
    .nams-card-inner{position:relative;width:100%;height:100%;transition:transform 0.6s;transform-style:preserve-3d}
    .nams-card:hover .nams-card-inner{transform:rotateY(180deg)}
    .nams-card-face{position:absolute;inset:0;border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;backface-visibility:hidden;padding:14px;box-sizing:border-box}
    .nams-card-front{background:linear-gradient(135deg,#0f172a,#1e293b);border:1px solid rgba(148,163,184,0.15)}
    .nams-card-back{background:linear-gradient(135deg,#0f172a,#1e293b);border:1px solid rgba(148,163,184,0.15);transform:rotateY(180deg)}
    .nams-card-back h4{color:#e2e8f0;margin:0 0 8px;font-size:0.95rem}
    .nams-card-back p{color:#94a3b8;margin:0;font-size:0.82rem;line-height:1.4;text-align:center}
    .nams-card-back .accent{color:#22d3ee;font-weight:700}
    .nams-card-front svg{margin-bottom:8px}
    .nams-card-front .label{color:#cbd5e1;font-size:0.82rem;font-weight:600;text-align:center}
    </style>
    <div class="nams-cards">

    <div class="nams-card">
      <div class="nams-card-inner">
        <div class="nams-card-face nams-card-front">
          <svg viewBox="0 0 80 70" width="90" height="80">
            <line x1="20" y1="18" x2="55" y2="12" stroke="#34d399" stroke-width="1.2" opacity="0.4"/>
            <line x1="20" y1="18" x2="40" y2="50" stroke="#34d399" stroke-width="1.2" opacity="0.4"/>
            <line x1="55" y1="12" x2="65" y2="40" stroke="#34d399" stroke-width="1.2" opacity="0.3"/>
            <line x1="40" y1="50" x2="65" y2="40" stroke="#34d399" stroke-width="1" opacity="0.25"/>
            <circle cx="20" cy="18" r="6" fill="#34d399" opacity="0.85"/>
            <circle cx="55" cy="12" r="5" fill="#34d399" opacity="0.8"/>
            <circle cx="40" cy="50" r="5.5" fill="#10b981" opacity="0.75"/>
            <circle cx="65" cy="40" r="4.5" fill="#10b981" opacity="0.7"/>
          </svg>
          <div class="label">Protein Interactions</div>
        </div>
        <div class="nams-card-face nams-card-back">
          <h4>Protein-Protein Interaction</h4>
          <p><span class="accent">Nodes</span> = proteins<br><span class="accent">Edges</span> = one protein binds with another</p>
        </div>
      </div>
    </div>

    <div class="nams-card">
      <div class="nams-card-inner">
        <div class="nams-card-face nams-card-front">
          <svg viewBox="0 0 90 70" width="100" height="80">
            <line x1="15" y1="50" x2="45" y2="20" stroke="#fbbf24" stroke-width="1" opacity="0.25" stroke-linecap="round"/>
            <line x1="45" y1="20" x2="75" y2="30" stroke="#fbbf24" stroke-width="1.2" opacity="0.3" stroke-linecap="round"/>
            <line x1="15" y1="50" x2="75" y2="30" stroke="#fbbf24" stroke-width="0.8" opacity="0.15" stroke-linecap="round"/>
            <line x1="45" y1="20" x2="60" y2="55" stroke="#fbbf24" stroke-width="1" opacity="0.2" stroke-linecap="round"/>
            <circle cx="15" cy="50" r="4" fill="#fbbf24" opacity="0.7"/>
            <circle cx="45" cy="20" r="5" fill="#fbbf24" opacity="0.85"/>
            <circle cx="75" cy="30" r="4.5" fill="#fbbf24" opacity="0.8"/>
            <circle cx="60" cy="55" r="3.5" fill="#f59e0b" opacity="0.6"/>
          </svg>
          <div class="label">Air Transportation</div>
        </div>
        <div class="nams-card-face nams-card-back">
          <h4>Air Transport Network</h4>
          <p><span class="accent">Nodes</span> = airports<br><span class="accent">Edges</span> = a carrier flies between them</p>
        </div>
      </div>
    </div>

    <div class="nams-card">
      <div class="nams-card-inner">
        <div class="nams-card-face nams-card-front">
          <svg viewBox="0 0 90 70" width="100" height="80">
            <line x1="20" y1="35" x2="50" y2="20" stroke="#f472b6" stroke-width="1.2" opacity="0.35" stroke-linecap="round"/>
            <line x1="20" y1="35" x2="50" y2="50" stroke="#f472b6" stroke-width="1.2" opacity="0.35" stroke-linecap="round"/>
            <line x1="50" y1="20" x2="70" y2="40" stroke="#f472b6" stroke-width="1" opacity="0.25" stroke-linecap="round"/>
            <line x1="50" y1="50" x2="70" y2="40" stroke="#f472b6" stroke-width="1" opacity="0.25" stroke-linecap="round"/>
            <polygon points="48,22 52,19 51,24" fill="#f472b6" opacity="0.5"/>
            <polygon points="48,48 52,51 51,46" fill="#f472b6" opacity="0.5"/>
            <circle cx="20" cy="35" r="6" fill="#f472b6" opacity="0.85"/>
            <circle cx="50" cy="20" r="5" fill="#ec4899" opacity="0.75"/>
            <circle cx="50" cy="50" r="5" fill="#ec4899" opacity="0.75"/>
            <circle cx="70" cy="40" r="5" fill="#ec4899" opacity="0.75"/>
          </svg>
          <div class="label">Social Network</div>
        </div>
        <div class="nams-card-face nams-card-back">
          <h4>Social Network (Twitter)</h4>
          <p><span class="accent">Nodes</span> = users<br><span class="accent">Edges</span> = one user follows another</p>
        </div>
      </div>
    </div>

    </div>
    """),
            mo.md("""
    Now that you've seen the framework for defining a graph,
    we'd like to invite you to answer the following question:
    **What examples of networks have _you_ seen before in your profession?**

    Go ahead and list it out.
    """),
        ]
    )
    return


@app.cell(hide_code=True)
def types_of_graphs(mo):
    directed_toggle = mo.ui.switch(
        value=True, label="Directed graph (Twitter)"
    )
    mo.vstack(
        [
            mo.md("""
    ## Types of Graphs

    If you are a member of both LinkedIn and Twitter,
    you might intuitively think that there's a _slight_ difference
    in the structure of the two "social graphs".
    You'd be absolutely correct!

    **Twitter** is a **directed** graph &mdash; one user can follow another
    without the other following back. There is a _directionality_ to the relationship.

    **LinkedIn** is an **undirected** graph &mdash; connections are automatically
    bidirectional, so we collapse the two directions into a single edge.

    Toggle the switch below and watch how the same network changes
    when you go from directed (Twitter) to undirected (LinkedIn).
    """),
            directed_toggle,
        ]
    )
    return (directed_toggle,)


@app.cell(hide_code=True)
def types_of_graphs_viz(directed_toggle, mo):
    is_directed = directed_toggle.value

    if is_directed:
        out = mo.Html("""
    <div style="display:flex;justify-content:center;padding:12px 0">
      <svg viewBox="0 0 200 160" style="max-width:340px;width:100%;height:auto">
        <defs>
          <marker id="arrow-pink" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
            <path d="M 0 0 L 10 5 L 0 10 z" fill="#f472b6"/>
          </marker>
        </defs>
        <line x1="100" y1="80" x2="40"  y2="30"  stroke="#f472b6" stroke-width="2"   opacity="0.6" marker-end="url(#arrow-pink)"/>
        <line x1="40"  y1="30" x2="100" y2="80"  stroke="#f472b6" stroke-width="0.8" opacity="0.15" stroke-dasharray="3 3"/>
        <line x1="100" y1="80" x2="160" y2="30"  stroke="#f472b6" stroke-width="2"   opacity="0.6" marker-end="url(#arrow-pink)"/>
        <line x1="160" y1="30" x2="100" y2="80"  stroke="#f472b6" stroke-width="0.8" opacity="0.15" stroke-dasharray="3 3"/>
        <line x1="100" y1="80" x2="50"  y2="135" stroke="#f472b6" stroke-width="2"   opacity="0.5" marker-end="url(#arrow-pink)"/>
        <line x1="100" y1="80" x2="150" y2="135" stroke="#f472b6" stroke-width="2"   opacity="0.6" marker-end="url(#arrow-pink)"/>
        <line x1="150" y1="135" x2="100" y2="80" stroke="#f472b6" stroke-width="2"   opacity="0.6" marker-end="url(#arrow-pink)"/>
        <line x1="40"  y1="30" x2="160" y2="30"  stroke="#f472b6" stroke-width="1.5" opacity="0.35" marker-end="url(#arrow-pink)"/>
        <circle cx="100" cy="80"  r="10" fill="#f472b6" opacity="0.9"/>
        <text x="100" y="84" text-anchor="middle" fill="#1e293b" font-size="8" font-weight="700">A</text>
        <circle cx="40"  cy="30"  r="8"  fill="#ec4899" opacity="0.8"/>
        <text x="40" y="34" text-anchor="middle" fill="#fce7f3" font-size="7" font-weight="700">B</text>
        <circle cx="160" cy="30"  r="8"  fill="#ec4899" opacity="0.8"/>
        <text x="160" y="34" text-anchor="middle" fill="#fce7f3" font-size="7" font-weight="700">C</text>
        <circle cx="50"  cy="135" r="7"  fill="#db2777" opacity="0.7"/>
        <text x="50" y="139" text-anchor="middle" fill="#fce7f3" font-size="6" font-weight="700">D</text>
        <circle cx="150" cy="135" r="8"  fill="#ec4899" opacity="0.8"/>
        <text x="150" y="139" text-anchor="middle" fill="#fce7f3" font-size="7" font-weight="700">E</text>
        <text x="100" y="155" text-anchor="middle" fill="#94a3b8" font-size="8" font-weight="600">Twitter: directed &#8212; some follows are unrequited (dashed)</text>
      </svg>
    </div>
    """)
    else:
        out = mo.Html("""
    <div style="display:flex;justify-content:center;padding:12px 0">
      <svg viewBox="0 0 200 160" style="max-width:340px;width:100%;height:auto">
        <line x1="100" y1="80" x2="40"  y2="30"  stroke="#34d399" stroke-width="2.5" opacity="0.6" stroke-linecap="round"/>
        <line x1="100" y1="80" x2="160" y2="30"  stroke="#34d399" stroke-width="2.5" opacity="0.6" stroke-linecap="round"/>
        <line x1="100" y1="80" x2="50"  y2="135" stroke="#34d399" stroke-width="2.5" opacity="0.5" stroke-linecap="round"/>
        <line x1="100" y1="80" x2="150" y2="135" stroke="#34d399" stroke-width="2.5" opacity="0.6" stroke-linecap="round"/>
        <line x1="40"  y1="30" x2="160" y2="30"  stroke="#34d399" stroke-width="2"   opacity="0.4" stroke-linecap="round"/>
        <circle cx="100" cy="80"  r="10" fill="#34d399" opacity="0.9"/>
        <text x="100" y="84" text-anchor="middle" fill="#1e293b" font-size="8" font-weight="700">A</text>
        <circle cx="40"  cy="30"  r="8"  fill="#10b981" opacity="0.8"/>
        <text x="40" y="34" text-anchor="middle" fill="#d1fae5" font-size="7" font-weight="700">B</text>
        <circle cx="160" cy="30"  r="8"  fill="#10b981" opacity="0.8"/>
        <text x="160" y="34" text-anchor="middle" fill="#d1fae5" font-size="7" font-weight="700">C</text>
        <circle cx="50"  cy="135" r="7"  fill="#059669" opacity="0.7"/>
        <text x="50" y="139" text-anchor="middle" fill="#d1fae5" font-size="6" font-weight="700">D</text>
        <circle cx="150" cy="135" r="8"  fill="#10b981" opacity="0.8"/>
        <text x="150" y="139" text-anchor="middle" fill="#d1fae5" font-size="7" font-weight="700">E</text>
        <text x="100" y="155" text-anchor="middle" fill="#94a3b8" font-size="8" font-weight="600">LinkedIn: undirected &#8212; all connections are mutual</text>
      </svg>
    </div>
    """)
    out
    return


@app.cell(hide_code=True)
def edges_matter(mo):
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
