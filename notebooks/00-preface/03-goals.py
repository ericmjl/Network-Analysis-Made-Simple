import marimo

__generated_with = "0.23.9"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def _(mo):
    mo.Html(f"""
    <div class="nams-hero">
    <style>
      .nams-hero{{color:#e2e8f0;margin:0;font-family:inherit}}
      .nams-hero__grid{{display:grid;gap:22px;grid-template-columns:minmax(0,1.25fr) minmax(200px,0.85fr);padding:32px 28px;border-radius:14px;background:linear-gradient(135deg,#0f172a 0%,#1e293b 100%)}}
      @media(max-width:760px){{.nams-hero__grid{{grid-template-columns:1fr;padding:22px 16px}}}}
      .nams-badge{{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border:1px solid rgba(167,139,250,0.3);background:rgba(167,139,250,0.1);border-radius:999px;color:#a78bfa;font-size:0.72rem;font-weight:800;letter-spacing:0.06em;text-transform:uppercase}}
      .nams-hero h1{{margin:14px 0 8px;font-size:2.2rem;line-height:1.05;font-weight:880;letter-spacing:-0.02em;color:#f1f5f9}}
      .nams-hero h1 .nams-em{{color:#a78bfa}}
      .nams-hero p.lead{{margin:0;max-width:520px;color:#94a3b8;font-size:1.02rem;line-height:1.5}}
      .nams-byline{{margin-top:16px;color:#64748b;font-size:0.88rem;line-height:1.5}}
      .nams-byline b{{color:#cbd5e1}}
      .nams-art{{display:flex;align-items:center;justify-content:center}}
    </style>
    <div class="nams-hero__grid">
      <div>
        <span class="nams-badge">Chapter 00 &middot; Preface</span>
        <h1>Learning<br><span class="nams-em">Goals</span></h1>
        <p class="lead">Two kinds of takeaways await: <b>technical</b> skills with NetworkX, nxviz, and graph algorithms, and <b>intellectual</b> habits &mdash; relational thinking and algorithmic reasoning that outlast any library.</p>
        <div class="nams-byline">Network Analysis Made Simple &middot; <b>Eric Ma</b></div>
      </div>
      <div class="nams-art">
        <svg viewBox="0 0 140 140" style="width:100%;max-width:160px;height:auto">
          <circle cx="70" cy="70" r="45" fill="none" stroke="#a78bfa" stroke-width="1.5" opacity="0.2"/>
          <circle cx="70" cy="70" r="32" fill="none" stroke="#a78bfa" stroke-width="1.5" opacity="0.35"/>
          <circle cx="70" cy="70" r="19" fill="none" stroke="#a78bfa" stroke-width="1.5" opacity="0.55"/>
          <circle cx="70" cy="70" r="7" fill="#a78bfa" opacity="0.9"/>
          <line x1="70" y1="70" x2="112" y2="30" stroke="#c4b5fd" stroke-width="2.5" stroke-linecap="round"/>
          <polygon points="112,30 104,32 108,38" fill="#c4b5fd"/>
          <line x1="70" y1="70" x2="42" y2="108" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" opacity="0.5"/>
          <polygon points="42,108 46,100 50,106" fill="#8b5cf6" opacity="0.5"/>
          <line x1="70" y1="70" x2="105" y2="95" stroke="#8b5cf6" stroke-width="2" stroke-linecap="round" opacity="0.4"/>
          <polygon points="105,95 97,93 99,100" fill="#8b5cf6" opacity="0.4"/>
        </svg>
      </div>
    </div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our learning goals for you with this book
    can be split into the technical and the intellectual.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Technical Takeaways

    Firstly, we would like to equip you to be familiar
    with the NetworkX application programming interface (API).
    The reason for choosing NetworkX is because
    it is extremely beginner-friendly,
    and has an API that matches graph theory concepts very closely.

    Secondly, we would like to show you how you can visualize graph data
    in a fashion that doesn't involve showing mere hairballs.
    Throughout the book, you will see examples of what we call
    _rational graph visualizations_.
    One of our authors, Eric Ma, has developed a companion package, `nxviz`,
    that provides a declarative and convenient API
    (in other words an attempt at a "grammar")
    for graph visualization.

    Thirdly, in this book, you will be introduced to basic graph algorithms,
    such as finding special graph structures,
    or finding paths in a graph.
    Graph algorithms will show you how to "think on graphs",
    and knowing how to do so will broaden your ability to interact with
    graph data structures.

    Fourthly, you will also be equipped with the connection between graph theory
    and other areas of math and computing,
    such as statistical inference and linear algebra.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Intellectual Goals

    Beyond the technical takeaways,
    we hope to broaden how you think about data.

    The first idea we hope to give you
    the ability to think about your data
    in terms of "relationships".
    As you will learn,
    relationships are what give rise to the interestingness of graphs.
    That's where _relational insights_ can come to fore.

    The second idea we hope to give you
    is the ability to "think on graphs".
    This comes with practice.
    Once you master it, though,
    you will find yourself becoming more and more familiar
    with **algorithmic thinking**.
    which is where you look at a problem
    in terms of the **algorithm** that solves it.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    import wigglystuff

    tour = wigglystuff.CellTour(
        steps=[
        {'cell': 0, 'title': 'Learning Goals', 'description': 'Technical and intellectual takeaways from this tutorial.'},
        {'cell': 2, 'title': 'Technical Takeaways', 'description': 'NetworkX, nxviz, graph algorithms, linear algebra connections.'},
        {'cell': 3, 'title': 'Intellectual Goals', 'description': 'Relational thinking and algorithmic thinking.'},
    ],
        auto_start=False,
        show_progress=True,
    )
    mo.ui.anywidget(tour)
    return


if __name__ == "__main__":
    app.run()
