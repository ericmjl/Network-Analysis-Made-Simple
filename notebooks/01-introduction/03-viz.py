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
      .nams-badge{{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border:1px solid rgba(56,189,248,0.3);background:rgba(56,189,248,0.1);border-radius:999px;color:#38bdf8;font-size:0.72rem;font-weight:800;letter-spacing:0.06em;text-transform:uppercase}}
      .nams-hero h1{{margin:14px 0 8px;font-size:2.2rem;line-height:1.05;font-weight:880;letter-spacing:-0.02em;color:#f1f5f9}}
      .nams-hero h1 .nams-em{{color:#38bdf8}}
      .nams-hero p.lead{{margin:0;max-width:520px;color:#94a3b8;font-size:1.02rem;line-height:1.5}}
      .nams-byline{{margin-top:16px;color:#64748b;font-size:0.88rem;line-height:1.5}}
      .nams-byline b{{color:#cbd5e1}}
      .nams-art{{display:flex;align-items:center;justify-content:center}}
    </style>
    <div class="nams-hero__grid">
      <div>
        <span class="nams-badge">Chapter 01 &middot; Introduction</span>
        <h1>Graph<br><span class="nams-em">Visualization</span></h1>
        <p class="lead">Hairballs are the default &mdash; but they don't have to be. Matrix, arc, and circos plots transform the chaos into structured, rational visualizations that actually communicate insight.</p>
        <div class="nams-byline">Network Analysis Made Simple &middot; <b>Eric Ma</b></div>
      </div>
      <div class="nams-art">
        <svg viewBox="0 0 160 90" style="width:100%;max-width:200px;height:auto">
          <!-- Matrix: adjacency grid 6x6, grouped (2 groups of 3) -->
          <rect x="8" y="8" width="38" height="38" rx="2" fill="none" stroke="#38bdf8" stroke-width="0.8" opacity="0.3"/>
          <!-- cells: each 5.5px, offset from x=10,y=10 -->
          <!-- row 0 -->
          <rect x="10" y="10" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="16" y="10" width="5" height="5" fill="#38bdf8" opacity="0.7"/>
          <rect x="22" y="10" width="5" height="5" fill="#38bdf8" opacity="0.7"/>
          <rect x="28" y="10" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="34" y="10" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="40" y="10" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <!-- row 1 -->
          <rect x="10" y="16" width="5" height="5" fill="#38bdf8" opacity="0.7"/>
          <rect x="16" y="16" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="22" y="16" width="5" height="5" fill="#38bdf8" opacity="0.7"/>
          <rect x="28" y="16" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="34" y="16" width="5" height="5" fill="#38bdf8" opacity="0.4"/>
          <rect x="40" y="16" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <!-- row 2 -->
          <rect x="10" y="22" width="5" height="5" fill="#38bdf8" opacity="0.7"/>
          <rect x="16" y="22" width="5" height="5" fill="#38bdf8" opacity="0.7"/>
          <rect x="22" y="22" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="28" y="22" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="34" y="22" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="40" y="22" width="5" height="5" fill="#38bdf8" opacity="0.4"/>
          <!-- row 3 -->
          <rect x="10" y="28" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="16" y="28" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="22" y="28" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="28" y="28" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="34" y="28" width="5" height="5" fill="#38bdf8" opacity="0.7"/>
          <rect x="40" y="28" width="5" height="5" fill="#38bdf8" opacity="0.7"/>
          <!-- row 4 -->
          <rect x="10" y="34" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="16" y="34" width="5" height="5" fill="#38bdf8" opacity="0.4"/>
          <rect x="22" y="34" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="28" y="34" width="5" height="5" fill="#38bdf8" opacity="0.7"/>
          <rect x="34" y="34" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="40" y="34" width="5" height="5" fill="#38bdf8" opacity="0.7"/>
          <!-- row 5 -->
          <rect x="10" y="40" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="16" y="40" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <rect x="22" y="40" width="5" height="5" fill="#38bdf8" opacity="0.4"/>
          <rect x="28" y="40" width="5" height="5" fill="#38bdf8" opacity="0.7"/>
          <rect x="34" y="40" width="5" height="5" fill="#38bdf8" opacity="0.7"/>
          <rect x="40" y="40" width="5" height="5" fill="#38bdf8" opacity="0.08"/>
          <text x="28" y="56" text-anchor="middle" fill="#7dd3fc" font-size="6" font-weight="600" opacity="0.6">matrix</text>

          <!-- Arc: nodes on a horizontal line, arcs above connecting pairs -->
          <line x1="58" y1="44" x2="108" y2="44" stroke="#38bdf8" stroke-width="0.8" opacity="0.2"/>
          <!-- arcs: quadratic bezier Q controlX controlY, bowing upward. Height ~ proportional to distance -->
          <path d="M 60 44 Q 67 32 74 44" stroke="#38bdf8" stroke-width="1" fill="none" opacity="0.5"/>
          <path d="M 60 44 Q 77 24 94 44" stroke="#38bdf8" stroke-width="1" fill="none" opacity="0.45"/>
          <path d="M 74 44 Q 84 34 94 44" stroke="#38bdf8" stroke-width="1" fill="none" opacity="0.5"/>
          <path d="M 67 44 Q 80 28 93 44" stroke="#38bdf8" stroke-width="1" fill="none" opacity="0.35"/>
          <path d="M 80 44 Q 87 36 94 44" stroke="#38bdf8" stroke-width="1" fill="none" opacity="0.4"/>
          <path d="M 87 44 Q 97 30 107 44" stroke="#38bdf8" stroke-width="1" fill="none" opacity="0.45"/>
          <!-- nodes on the line -->
          <circle cx="60" cy="44" r="2.5" fill="#38bdf8" opacity="0.8"/>
          <circle cx="67" cy="44" r="2.5" fill="#38bdf8" opacity="0.7"/>
          <circle cx="74" cy="44" r="2.5" fill="#38bdf8" opacity="0.8"/>
          <circle cx="80" cy="44" r="2.5" fill="#38bdf8" opacity="0.7"/>
          <circle cx="87" cy="44" r="2.5" fill="#38bdf8" opacity="0.8"/>
          <circle cx="94" cy="44" r="2.5" fill="#38bdf8" opacity="0.7"/>
          <circle cx="100" cy="44" r="2.5" fill="#38bdf8" opacity="0.6"/>
          <circle cx="107" cy="44" r="2.5" fill="#38bdf8" opacity="0.6"/>
          <text x="83" y="56" text-anchor="middle" fill="#7dd3fc" font-size="6" font-weight="600" opacity="0.6">arc</text>

          <!-- Circos: nodes on a circle, edges as inward-bowing bezier curves -->
          <!-- circle center: (135, 27), radius: 16 -->
          <!-- 8 nodes at 45° intervals -->
          <circle cx="135" cy="27" r="16" fill="none" stroke="#38bdf8" stroke-width="0.6" opacity="0.15"/>
          <!-- edges: bezier with control point at center (135,27) -->
          <path d="M 151 27 Q 135 27 135 11" stroke="#38bdf8" stroke-width="0.9" fill="none" opacity="0.4"/>
          <path d="M 151 27 Q 135 27 119 27" stroke="#38bdf8" stroke-width="0.9" fill="none" opacity="0.3"/>
          <path d="M 135 11 Q 135 27 119 27" stroke="#38bdf8" stroke-width="0.9" fill="none" opacity="0.35"/>
          <path d="M 146 38 Q 135 27 124 16" stroke="#38bdf8" stroke-width="0.9" fill="none" opacity="0.4"/>
          <path d="M 146 38 Q 135 27 135 43" stroke="#38bdf8" stroke-width="0.9" fill="none" opacity="0.3"/>
          <path d="M 124 16 Q 135 27 124 38" stroke="#38bdf8" stroke-width="0.9" fill="none" opacity="0.35"/>
          <!-- nodes -->
          <circle cx="151" cy="27" r="2" fill="#38bdf8" opacity="0.8"/>
          <circle cx="146" cy="38" r="2" fill="#38bdf8" opacity="0.7"/>
          <circle cx="135" cy="43" r="2" fill="#38bdf8" opacity="0.7"/>
          <circle cx="124" cy="38" r="2" fill="#38bdf8" opacity="0.7"/>
          <circle cx="119" cy="27" r="2" fill="#38bdf8" opacity="0.8"/>
          <circle cx="124" cy="16" r="2" fill="#38bdf8" opacity="0.7"/>
          <circle cx="135" cy="11" r="2" fill="#38bdf8" opacity="0.7"/>
          <circle cx="146" cy="16" r="2" fill="#38bdf8" opacity="0.7"/>
          <text x="135" y="56" text-anchor="middle" fill="#7dd3fc" font-size="6" font-weight="600" opacity="0.6">circos</text>
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
        {'cell': 0, 'title': 'Graph Visualization', 'description': 'From hairballs to rational visualizations.'},
        {'cell': 13, 'title': 'The hairball problem', 'description': 'Node-link diagrams become unreadable for large graphs.'},
        {'cell': 14, 'title': 'Matrix Plot', 'description': 'Adjacency matrix view with nxviz.'},
        {'cell': 16, 'title': 'Arc Plot', 'description': 'Nodes on a line with arcs for edges.'},
        {'cell': 19, 'title': 'Circos Plot', 'description': 'Arc plot wrapped into a circle.'},
        {'cell': 22, 'title': 'Hive Plot', 'description': 'Radial axes for grouped nodes.'},
        {'cell': 25, 'title': 'Interactive comparison', 'description': 'Switch between all four viz types with a dropdown.'},
    ],
        auto_start=False,
        show_progress=True,
    )
    mo.ui.anywidget(tour)
    return




@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)




@app.cell(hide_code=True)
def _():
    import warnings

    warnings.filterwarnings("ignore")
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Introduction
    """)
    return




@app.cell(hide_code=True)
def _():
    from IPython.display import YouTubeVideo

    YouTubeVideo(id="v9HrR_AF5Zc", width="100%")
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In this chapter, we want to introduce you to the wonderful world of graph visualization.

    You probably have seen graphs that are visualized as hairballs.
    Apart from communicating how complex the graph is,
    hairballs don't really communicate much else.
    As such, my goal by the end of this chapter is
    to introduce you to what I call _rational graph visualization_.

    But before we can do that, let's first make sure we understand
    how to use NetworkX's drawing facilities to draw graphs to the screen.
    In a pinch, and for small graphs, it's very handy to have.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hairballs

    The node-link diagram is the canonical diagram we will see in publications.
    Nodes are commonly drawn as circles, while edges are drawn as lines.

    Node-link diagrams are common,
    and there's a good reason for this: it's convenient to draw!
    In NetworkX, we can draw node-link diagrams using:
    """)
    return




@app.cell(hide_code=True)
def _():
    from nams import load_data as cf
    import networkx as nx
    import matplotlib.pyplot as plt

    G = cf.load_seventh_grader_network()
    return G, nx, plt




@app.cell
def _(G, nx, plt):
    nx.draw(G)
    plt.show()
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Nodes more tightly connected with one another are clustered together.
    Initial node placement is done typically at random,
    so really it's tough to deterministically generate the same figure.
    If the network is small enough to visualize,
    and the node labels are small enough to fit in a circle,
    then you can use the `with_labels=True` argument
    to bring some degree of informativeness to the drawing:
    """)
    return




@app.cell
def _(G):
    G.is_directed()
    return




@app.cell
def _(G, nx, plt):
    nx.draw(G, with_labels=True)
    plt.show()
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The downside to drawing graphs this way is that
    large graphs end up looking like hairballs.
    Can you imagine a graph with more than the 28 nodes that we have?
    As you probably can imagine, the default `nx.draw(G)`
    is probably not suitable for generating visual insights.

    ## Matrix Plot

    A different way that we can visualize a graph is by visualizing it in its matrix form.
    The nodes are on the x- and y- axes, and a filled square represent an edge between the nodes.

    We can draw a graph's matrix form conveniently by using `nxviz.MatrixPlot`:
    """)
    return




@app.cell(hide_code=True)
def _(G):
    import nxviz as nv

    nv.matrix(G, group_by="gender", node_color_by="gender", backend="plotly")
    return (nv,)




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What can you tell from the graph visualization?
    A few things are immediately obvious:

    - The diagonal is empty: no student voted for themselves as their favourite.
    - The matrix is asymmetric about the diagonal: this is a directed graph!

    (An undirected graph would be symmetric about the diagonal.)

    You might go on to suggest that there is some clustering happening,
    but without applying a proper clustering algorithm on the adjacency matrix,
    we would be hard-pressed to know for sure.
    After all, we can simply re-order the node ordering along the axes
    to produce a seemingly-random matrix.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Arc Plot

    The Arc Plot is another rational graph visualization.
    Here, we line up the nodes along a horizontal axis,
    and draw _arcs_ between nodes if they are connected by an edge.
    We can also optionally group and colour them by some metadata.
    In the case of this student graph,
    we group and colour them by "gender".
    """)
    return




@app.cell
def _(G, nv):
    nv.arc(G, node_color_by="gender", group_by="gender", backend="plotly")
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Arc Plot forms the basis of the next visualization,
    the highly popular Circos plot.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Circos Plot

    The Circos Plot was developed by [Martin Krzywinski][bccrc] at the BC Cancer Research Center. The `nxviz.CircosPlot` takes inspiration from the original by joining the two ends of the Arc Plot into a circle. Likewise, we can colour and order nodes by node metadata:

    [bccrc]: http://circos.ca/
    """)
    return




@app.cell
def _(G, nv):
    nv.circos(G, group_by="gender", node_color_by="gender", backend="plotly")
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Generally speaking, you can think of a Circos Plot as being
    a more compact and aesthetically pleasing version of Arc Plots.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Hive Plot

    The final plot we'll show is, Hive Plots.
    """)
    return




@app.cell
def _(G, nv):
    nv.hive(G, group_by="gender", node_color_by="gender", backend="plotly")
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As you can see, with Hive Plots,
    we first group nodes along two or three radial axes.
    In this case, we have the boys along one radial axis
    and the girls along the other.
    We can also order the nodes along each axis if we so choose to.
    In this case, no particular ordering is chosen.

    Next, we draw edges.
    We start first with edges _between_ groups.
    That is shown on the left side of the figure,
    joining nodes in the "yellow" and "green" (boys/girls) groups.
    We then proceed to edges _within_ groups.
    This is done by cloning the node radial axis
    before drawing edges.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Compare Visualization Types Interactively

    Now that you have seen all four rational visualizations,
    use the dropdown below to switch between them and compare side by side.
    Think about which visualization best communicates the structure of the graph.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    viz_selector = mo.ui.dropdown(
        options=["matrix", "arc", "circos", "hive"],
        value="circos",
        label="Visualization Type",
    )
    viz_selector
    return (viz_selector,)




@app.cell
def _(G, nv, viz_selector):
    viz_fn = getattr(nv, viz_selector.value)
    viz_fn(G, group_by="gender", node_color_by="gender", backend="plotly")
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Principles of Rational Graph Viz

    While I was implementing these visualizations in [`nxviz`](https://github.com/ericmjl/nxviz),
    I learned an important lesson in implementing graph visualizations in general:

    > To be most informative and communicative,
    > a graph visualization should first prioritize node placement
    > in a fashion that makes sense.

    In some ways, this makes a ton of sense.
    The nodes are the "entities" in a graph,
    corresponding to people, proteins, and ports.
    For "entities", we have natural ways to group, order and summarize (reduce).
    (An example of a "reduction" is counting the number of things.)
    Prioritizing node placement allows us
    to appeal to our audience's natural sense of grouping, ordering and reduction.

    So the next time you see a hairball,
    I hope you're able to critique it for what it doesn't communicate,
    and possibly use the same principle to design a better visualization!
    """)
    return


if __name__ == "__main__":
    app.run()
