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
      .nams-badge{{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border:1px solid rgba(168,85,247,0.3);background:rgba(168,85,247,0.1);border-radius:999px;color:#a855f7;font-size:0.72rem;font-weight:800;letter-spacing:0.06em;text-transform:uppercase}}
      .nams-hero h1{{margin:14px 0 8px;font-size:2.2rem;line-height:1.05;font-weight:880;letter-spacing:-0.02em;color:#f1f5f9}}
      .nams-hero h1 .nams-em{{color:#a855f7}}
      .nams-hero p.lead{{margin:0;max-width:520px;color:#94a3b8;font-size:1.02rem;line-height:1.5}}
      .nams-byline{{margin-top:16px;color:#64748b;font-size:0.88rem;line-height:1.5}}
      .nams-byline b{{color:#cbd5e1}}
      .nams-art{{display:flex;align-items:center;justify-content:center}}
    </style>
    <div class="nams-hero__grid">
      <div>
        <span class="nams-badge">Chapter 04 &middot; Advanced</span>
        <h1>Graphs &amp;<br><span class="nams-em">Linear Algebra</span></h1>
        <p class="lead">Adjacency matrices, matrix powers for path counting, message passing, and bipartite projections &mdash; the algebra that makes graph computation fast and scalable.</p>
        <div class="nams-byline">Network Analysis Made Simple &middot; <b>Eric Ma</b></div>
      </div>
      <div class="nams-art">
        <svg viewBox="0 0 140 120" style="width:100%;max-width:170px;height:auto">
          <!-- 4x4 adjacency matrix grid -->
          <rect x="10" y="10" width="50" height="50" rx="2" fill="none" stroke="#a855f7" stroke-width="0.8" opacity="0.3"/>
          <line x1="22.5" y1="10" x2="22.5" y2="60" stroke="#a855f7" stroke-width="0.4" opacity="0.15"/>
          <line x1="35" y1="10" x2="35" y2="60" stroke="#a855f7" stroke-width="0.4" opacity="0.15"/>
          <line x1="47.5" y1="10" x2="47.5" y2="60" stroke="#a855f7" stroke-width="0.4" opacity="0.15"/>
          <line x1="10" y1="22.5" x2="60" y2="22.5" stroke="#a855f7" stroke-width="0.4" opacity="0.15"/>
          <line x1="10" y1="35" x2="60" y2="35" stroke="#a855f7" stroke-width="0.4" opacity="0.15"/>
          <line x1="10" y1="47.5" x2="60" y2="47.5" stroke="#a855f7" stroke-width="0.4" opacity="0.15"/>
          <!-- filled cells representing edges -->
          <rect x="10" y="10" width="12.5" height="12.5" fill="#a855f7" opacity="0.08"/>
          <rect x="22.5" y="10" width="12.5" height="12.5" fill="#a855f7" opacity="0.7"/>
          <rect x="35" y="10" width="12.5" height="12.5" fill="#a855f7" opacity="0.08"/>
          <rect x="47.5" y="10" width="12.5" height="12.5" fill="#a855f7" opacity="0.7"/>
          <rect x="10" y="22.5" width="12.5" height="12.5" fill="#a855f7" opacity="0.7"/>
          <rect x="22.5" y="22.5" width="12.5" height="12.5" fill="#a855f7" opacity="0.08"/>
          <rect x="35" y="22.5" width="12.5" height="12.5" fill="#a855f7" opacity="0.7"/>
          <rect x="47.5" y="22.5" width="12.5" height="12.5" fill="#a855f7" opacity="0.08"/>
          <rect x="10" y="35" width="12.5" height="12.5" fill="#a855f7" opacity="0.08"/>
          <rect x="22.5" y="35" width="12.5" height="12.5" fill="#a855f7" opacity="0.7"/>
          <rect x="35" y="35" width="12.5" height="12.5" fill="#a855f7" opacity="0.08"/>
          <rect x="47.5" y="35" width="12.5" height="12.5" fill="#a855f7" opacity="0.7"/>
          <rect x="10" y="47.5" width="12.5" height="12.5" fill="#a855f7" opacity="0.7"/>
          <rect x="22.5" y="47.5" width="12.5" height="12.5" fill="#a855f7" opacity="0.08"/>
          <rect x="35" y="47.5" width="12.5" height="12.5" fill="#a855f7" opacity="0.7"/>
          <rect x="47.5" y="47.5" width="12.5" height="12.5" fill="#a855f7" opacity="0.08"/>
          <!-- arrow -->
          <path d="M 68 35 L 82 35" stroke="#a855f7" stroke-width="1.5" opacity="0.4" stroke-linecap="round"/>
          <polygon points="82,35 77,32 77,38" fill="#a855f7" opacity="0.4"/>
          <!-- small graph on right -->
          <line x1="90" y1="15" x2="125" y2="20" stroke="#a855f7" stroke-width="1.2" opacity="0.35" stroke-linecap="round"/>
          <line x1="90" y1="15" x2="105" y2="50" stroke="#a855f7" stroke-width="1.2" opacity="0.35" stroke-linecap="round"/>
          <line x1="125" y1="20" x2="105" y2="50" stroke="#a855f7" stroke-width="1.2" opacity="0.35" stroke-linecap="round"/>
          <line x1="105" y1="50" x2="130" y2="55" stroke="#a855f7" stroke-width="1" opacity="0.25" stroke-linecap="round"/>
          <line x1="125" y1="20" x2="130" y2="55" stroke="#a855f7" stroke-width="1" opacity="0.2" stroke-linecap="round"/>
          <circle cx="90" cy="15" r="4.5" fill="#a855f7" opacity="0.8"/>
          <circle cx="125" cy="20" r="4.5" fill="#a855f7" opacity="0.8"/>
          <circle cx="105" cy="50" r="4.5" fill="#9333ea" opacity="0.7"/>
          <circle cx="130" cy="55" r="4" fill="#9333ea" opacity="0.7"/>
          <text x="35" y="75" text-anchor="middle" fill="#c084fc" font-size="5.5" font-weight="600" opacity="0.5">matrix</text>
          <text x="110" y="75" text-anchor="middle" fill="#c084fc" font-size="5.5" font-weight="600" opacity="0.5">graph</text>
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
        {'cell': 0, 'title': 'Graphs & Linear Algebra', 'description': 'The deep connection between graph theory and matrix computation.'},
        {'cell': 6, 'title': 'The Adjacency Matrix', 'description': 'Convert a graph into a NumPy array — the foundation of all graph linear algebra.'},
        {'cell': 13, 'title': 'Obtaining the Matrix', 'description': 'nx.to_numpy_array gives you the adjacency matrix with a sorted nodelist.'},
        {'cell': 15, 'title': 'Matrix Powers & Path Counting', 'description': 'Raising the adjacency matrix to the k-th power counts k-step walks between every pair of nodes.'},
        {'cell': 17, 'title': 'Exercise: What Does A Squared Mean?', 'description': 'Interpret the entries of the squared adjacency matrix in terms of graph paths.'},
        {'cell': 28, 'title': 'Interactive: Power Slider', 'description': 'Slide the number of steps k and watch how path counts change in real time.'},
        {'cell': 30, 'title': 'Message Passing', 'description': 'Multiply a message vector by the adjacency matrix to propagate information across the graph.'},
        {'cell': 39, 'title': 'Bipartite Matrix Operations', 'description': 'The biadjacency matrix and its transpose reveal shared-neighbor structure via M @ M.T.'},
        {'cell': 48, 'title': 'Amazon Review Network', 'description': 'Apply sparse matrix operations to a real customer-product graph with thousands of nodes.'},
        {'cell': 67, 'title': 'Performance: Objects vs Matrices', 'description': 'Matrix computation is 10-50x faster than the equivalent object-oriented NetworkX approach.'},
        {'cell': 74, 'title': 'GPU & CPU Acceleration', 'description': 'rustworkx and cuGraph scale graph computation to millions of nodes.'},
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
def _(mo):
    mo.md(
        "Watch the [video on YouTube](https://www.youtube.com/watch?v=uTHihJiRELc)."
    )
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In this chapter, we will look at the relationship between graphs and linear algebra.

    The deep connection between these two topics is super interesting,
    and I'd like to show it to you through an exploration of three topics:

    1. Path finding
    1. Message passing
    1. Bipartite projections

    ## Preliminaries

    Before we go deep into the linear algebra piece though,
    we have to first make sure some ideas are clear.

    The most important thing that we need
    when treating graphs in linear algebra form
    is the **adjacency matrix**.
    For example, for four nodes joined in a chain:
    """)
    return




@app.cell
def _():
    import networkx as nx

    nodes = list(range(4))
    G1 = nx.Graph()
    G1.add_nodes_from(nodes)
    G1.add_edges_from(zip(nodes, nodes[1:]))
    return G1, nodes, nx




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    we can visualize the graph:
    """)
    return




@app.cell
def _(G1, nx, plt):
    nx.draw(G1, with_labels=True)
    plt.show()
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and we can visualize its adjacency matrix:
    """)
    return




@app.cell(hide_code=True)
def _(G1):
    import nxviz as nv

    nv.matrix(G1, backend="plotly")
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    and we can obtain the adjacency matrix as a NumPy array:
    """)
    return




@app.cell
def _(G1, nx):
    A1 = nx.to_numpy_array(G1, nodelist=sorted(G1.nodes()))
    A1
    return (A1,)




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Symmetry

    Remember that for an undirected graph,
    the adjacency matrix will be symmetric about the diagonal,
    while for a directed graph,
    the adjacency matrix will be _asymmetric_.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Path finding

    In the Paths chapter, we can use the breadth-first search algorithm
    _to find a shortest path between any two nodes_.

    As it turns out, using adjacency matrices, we can answer a related question,
    which is _how many paths exist of length K between two nodes_.

    To see how, we need to see the relationship between matrix powers and graph path lengths.

    Let's take the adjacency matrix above,
    raise it to the second power,
    and see what it tells us.
    """)
    return




@app.cell
def _(A1):
    import numpy as np

    np.linalg.matrix_power(A1, 2)
    return (np,)




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise: adjacency matrix power?

    > What do you think the values in the adjacency matrix are related to?
    > If studying in a group, discuss with your neighbors;
    > if working on this alone, write down your thoughts.
    """)
    return




@app.cell
def _():
    from nams.solutions.linalg import adjacency_matrix_power

    print(adjacency_matrix_power())
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Higher matrix powers

    The semantic meaning of adjacency matrix powers
    is preserved even if we go to higher powers.
    For example, if we go to the 3rd matrix power:
    """)
    return




@app.cell
def _(A1, np):
    np.linalg.matrix_power(A1, 3)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You should be able to convince yourself that:

    1. There's no way to go from a node back to itself in 3 steps, thus explaining the diagonals, and
    1. The off-diagonals take on the correct values when you think about them in terms of "ways to go from one node to another".
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### With directed graphs?

    Does the "number of steps" interpretation hold
    with directed graphs?
    Yes it does!
    Let's see it in action.
    """)
    return




@app.cell
def _(nodes, nx, plt):
    G2 = nx.DiGraph()
    G2.add_nodes_from(nodes)
    G2.add_edges_from(zip(nodes, nodes[1:]))
    nx.draw(G2, with_labels=True)
    plt.show()
    return (G2,)




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise: directed graph matrix power

    > Convince yourself that the resulting adjacency matrix power
    > contains the same semantic meaning
    > as that for an undirected graph,
    > that is,
    > _the number of ways to go from "row" node to "column" node
    > in K steps_.
    > (I have provided three different matrix powers for you.)
    """)
    return




@app.cell
def _(G2, np, nx):
    A2 = nx.to_numpy_array(G2)
    np.linalg.matrix_power(A2, 2)
    return (A2,)




@app.cell
def _(A2, np):
    np.linalg.matrix_power(A2, 3)
    return




@app.cell
def _(A2, np):
    np.linalg.matrix_power(A2, 4)
    return




@app.cell(hide_code=True)
def _(mo):
    power_slider = mo.ui.slider(start=1, stop=6, value=2, step=1, label="Matrix power k (steps)")
    power_slider
    return (power_slider,)




@app.cell
def _(A2, np, power_slider):
    np.linalg.matrix_power(A2, power_slider.value)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Message Passing

    Let's now dive into the second topic here,
    that of message passing.

    To show how message passing works on a graph,
    let's start with the directed linear chain,
    as this will make things easier to understand.

    ### "Message" representation in matrix form

    Our graph adjacency matrix contains nodes ordered in a particular fashion
    along the rows and columns.
    We can also create a "message" matrix $M$,
    using the same ordering of nodes along the rows,
    with columns instead representing a "message"
    that is intended to be "passed" from one node to another:
    """)
    return




@app.cell
def _(np):
    M = np.array([1, 0, 0, 0])
    M
    return (M,)




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Notice where the position of the value `1` is - at the first node.

    If we take M and matrix multiply it against A2, let's see what we get:
    """)
    return




@app.cell
def _(A2, M):
    M @ A2
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The message has been passed onto the next node!
    And if we pass the message one more time:
    """)
    return




@app.cell
def _(A2, M):
    M @ A2 @ A2
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now, the message lies on the 3rd node!

    We can make an animation to visualize this more clearly.
    _There are comments in the code to explain what's going on!_
    """)
    return




@app.cell
def _(nx):
    def propagate(G, msg, n_frames):
        """
        Computes the node values based on propagation.

        Intended to be used before or when being passed into the
        anim() function (defined below).

        :param G: A NetworkX Graph.
        :param msg: The initial state of the message.
        :returns: A list of 1/0 representing message status at
            each node.
        """
        msg_states = []
        new_msg = msg
        A = nx.to_numpy_array(G)
        for i in range(n_frames):
            msg_states.append(new_msg)
            new_msg = new_msg @ A
        return msg_states

    return (propagate,)




@app.cell
def _(G2, np, nx, plt, propagate):
    from IPython.display import HTML
    from matplotlib import animation

    def update_func(step, nodes, colors):
        """
        The update function for each animation time step.

        :param step: Passed in from matplotlib's FuncAnimation. Must
            be present in the function signature.
        :param nodes: Returned from nx.draw_networkx_edges(). Is an
            array of colors.
        :param colors: A list of pre-computed colors.
        """
        nodes.set_array(colors[step].ravel())
        return nodes

    def anim(G, initial_state, n_frames=4):
        """
        Animation function!
        """
        colors = propagate(G, initial_state, n_frames)
        fig = plt.figure()
        pos = nx.kamada_kawai_layout(G)
        nodes = nx.draw_networkx_nodes(
            G, pos=pos, node_color=colors[0].ravel(), node_size=20
        )
        ax = nx.draw_networkx_edges(G, pos)
        return animation.FuncAnimation(
            fig, update_func, frames=range(n_frames), fargs=(nodes, colors)
        )

    msg = np.zeros(len(G2))
    msg[0] = 1

    HTML(anim(G2, msg, n_frames=4).to_html5_video())
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Bipartite Graphs & Matrices

    The section on message passing above assumed unipartite graphs, or at least graphs for which messages can be meaningfully passed between nodes.

    In this section, we will look at bipartite graphs.

    Recall from before the definition of a bipartite graph:

    - Nodes are separated into two partitions (hence 'bi'-'partite').
    - Edges can only occur between nodes of different partitions.

    Bipartite graphs have a natural matrix representation, known as the **biadjacency matrix**. Nodes on one partition are the rows, and nodes on the other partition are the columns.

    NetworkX's `bipartite` module provides a function for computing the biadjacency matrix of a bipartite graph.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's start by looking at a toy bipartite graph, a "customer-product" purchase record graph, with 4 products and 3 customers. The matrix representation might be as follows:
    """)
    return




@app.cell
def _(np):
    cp_mat = np.array([[0, 1, 0, 0], [1, 0, 1, 0], [1, 1, 1, 1]])
    return (cp_mat,)




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    From this "bi-adjacency" matrix, one can compute the projection onto the customers, matrix multiplying the matrix with its transpose.
    """)
    return




@app.cell
def _(cp_mat):
    c_mat = cp_mat @ cp_mat.T
    c_mat
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What we get is the connectivity matrix of the customers, based on shared purchases.
    The diagonals are the degree of the customers in the original graph,
    i.e. the number of purchases they originally made,
    and the off-diagonals are the connectivity matrix, based on shared products.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To get the products matrix, we make the transposed matrix the left side of the matrix multiplication.
    """)
    return




@app.cell
def _(cp_mat):
    p_mat = cp_mat.T @ cp_mat
    p_mat
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You may now try to convince yourself that the diagonals are the number of times a customer purchased that product, and the off-diagonals are the connectivity matrix of the products, weighted by how similar two customers are.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercises

    In the following exercises, you will now play with a customer-product graph from Amazon. This dataset was downloaded from [UCSD's Julian McAuley's website](http://jmcauley.ucsd.edu/data/amazon/), and corresponds to the digital music dataset.

    This is a bipartite graph. The two partitions are:

    - `customers`: The customers that were doing the reviews.
    - `products`: The music that was being reviewed.

    In the original dataset (see the original JSON in the `datasets/` directory), they are referred to as:

    - `customers`: `reviewerID`
    - `products`: `asin`
    """)
    return




@app.cell(hide_code=True)
def _():
    from nams import load_data as cf

    G_amzn = cf.load_amazon_reviews()
    return (G_amzn,)




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Remember that with bipartite graphs, it is useful to obtain nodes from one of the partitions.
    """)
    return




@app.cell
def _():
    from nams.solutions.bipartite import extract_partition_nodes

    return (extract_partition_nodes,)




@app.cell
def _(G_amzn, extract_partition_nodes, nx):
    customer_nodes = extract_partition_nodes(G_amzn, "customer")
    mat = nx.bipartite.biadjacency_matrix(G_amzn, row_order=customer_nodes)
    return customer_nodes, mat




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    You'll notice that this matrix is extremely large! There are 5541 customers and 3568 products,
    for a total matrix size of $5541 \times 3568 = 19770288$, but it is stored in a sparse format because only 64706 elements are filled in.
    """)
    return




@app.cell
def _(mat):
    mat
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Example: finding customers who reviewed the most number of music items.

    Let's find out which customers reviewed the most number of music items.

    To do so, you can break the problem into a few steps.

    First off, we compute the customer projection using matrix operations.
    """)
    return




@app.cell
def _(mat):
    customer_mat = mat @ mat.T
    return (customer_mat,)




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Next, get the diagonals of the customer-customer matrix. Recall here that in `customer_mat`, the diagonals correspond to the degree of the customer nodes in the bipartite matrix.

    SciPy sparse matrices provide a `.diagonal()` method that returns the diagonal elements.
    """)
    return




@app.cell
def _(customer_mat):
    degrees = customer_mat.diagonal()
    return (degrees,)




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Finally, find the index of the customer that has the highest degree.
    """)
    return




@app.cell
def _(degrees, np):
    cust_idx = np.argmax(degrees)
    cust_idx
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can verify this independently by sorting the customer nodes by degree.
    """)
    return




@app.cell(hide_code=True)
def _(G_amzn, customer_nodes, nx):
    import pandas as pd
    import janitor

    deg = (
        pd.Series(dict(nx.degree(G_amzn, customer_nodes)))
        .to_frame()
        .reset_index()
        .rename_column("index", "customer")
        .rename_column(0, "num_reviews")
        .sort_values("num_reviews", ascending=False)
    )
    deg.head()
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Indeed, customer 294 was the one who had the most number of reviews!
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Example: finding similar customers

    Let's now also compute which two customers are similar, based on shared reviews. To do so involves the following steps:

    1. We construct a sparse matrix consisting of only the diagonals. `scipy.sparse.diags(elements)` will construct a sparse diagonal matrix based on the elements inside `elements`.
    1. Subtract the diagonals from the customer matrix projection. This yields the customer-customer similarity matrix, which should only consist of the off-diagonal elements of the customer matrix projection.
    1. Finally, get the indices where the weight (shared number of between the customers is highest. (*This code is provided for you.*)
    """)
    return




@app.cell
def _():
    import scipy.sparse as sp

    return (sp,)




@app.cell
def _(customer_mat, degrees, np, sp):
    _customer_diags = sp.diags(degrees)
    _off_diagonals = customer_mat - _customer_diags
    np.unravel_index(np.argmax(_off_diagonals), customer_mat.shape)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Performance: Object vs. Matrices

    Finally, to motivate why you might want to use matrices rather than graph objects to compute some of these statistics, let's time the two ways of getting to the same answer.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Objects

    Let's first use NetworkX's built-in machinery to find customers that are most similar.
    """)
    return




@app.cell
def _(G_amzn, customer_nodes, nx):
    from time import time

    _start = time()
    G_cust = nx.bipartite.weighted_projected_graph(G_amzn, customer_nodes)
    most_similar_customers = sorted(
        G_cust.edges(data=True), key=lambda x: x[2]["weight"], reverse=True
    )[0]
    _end = time()
    print(f"{_end - _start:.3f} seconds")
    print(f"Most similar customers: {most_similar_customers}")
    return (time,)




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Matrices

    Now, let's implement the same thing in matrix form.
    """)
    return




@app.cell
def _(G_amzn, customer_mat, customer_nodes, np, nx, sp, time):
    _start = time()
    mat_1 = nx.bipartite.matrix.biadjacency_matrix(G_amzn, customer_nodes)
    cust_mat = mat_1 @ mat_1.T
    degrees_1 = customer_mat.diagonal()
    _customer_diags = sp.diags(degrees_1)
    _off_diagonals = customer_mat - _customer_diags
    c1, c2 = np.unravel_index(np.argmax(_off_diagonals), customer_mat.shape)
    _end = time()
    print(f"{_end - _start:.3f} seconds")
    print(
        f"Most similar customers: {customer_nodes[c1]}, {customer_nodes[c2]}, {cust_mat[c1, c2]}"
    )
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    On a modern PC, the matrix computation should be about 10-50X faster
    using the matrix form compared to the object-oriented form.
    (The web server that is used to build the book
    might not necessarily have the software stack to do this though,
    so the time you see reported might not reflect the expected speedups.)
    I'd encourage you to fire up a Binder session or clone the book locally
    to test out the code yourself.

    You may notice that it's much easier to read the "objects" code,
    but the matrix code way outperforms the object code.
    This tradeoff is common in computing, and shouldn't surprise you.
    That said, the speed gain alone is a great reason to use matrices!
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Faster CPU alternatives

    If you're looking for even better performance but want to stick with CPU computing,
    there are some excellent alternatives that can provide significant speedups
    while maintaining compatibility with NetworkX APIs.

    [rustworkx](https://www.rustworkx.org/) is a high-performance graph library
    written in Rust with Python bindings.
    It provides many of the same algorithms as NetworkX
    but with significantly better performance for large graphs.
    The library offers both a NetworkX-compatible interface
    and its own optimized API for maximum speed.

    For cases where you need to process large graphs efficiently on CPU,
    rustworkx can be a great step up from pure NetworkX
    while still maintaining the familiar graph theory concepts you've learned.
    """)
    return




@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Acceleration on a GPU

    If your appetite has been whipped up for even more acceleration
    and you have a GPU on your daily compute,
    then you're very much in luck!

    The [RAPIDS.AI](https://rapids.ai) project has a package called [cuGraph](https://github.com/rapidsai/cugraph),
    which provides GPU-accelerated graph algorithms.
    As of release 0.16.0, all cuGraph algorithms will be able to accept NetworkX graph objects!
    This came about through online conversations on GitHub and Twitter,
    which for us, personally, speaks volumes to the power of open source projects!

    Because cuGraph does presume that you have access to a GPU,
    and because we assume most readers of this book might not have access to one easily,
    we'll delegate teaching how to install and use cuGraph to the cuGraph devs and [their documentation][docs].
    Nonetheless, if you do have the ability to install and use the RAPIDS stack,
    definitely check it out!

    [docs]: https://docs.rapids.ai/api/cugraph/stable/api.html
    """)
    return




@app.cell
def _():
    import matplotlib.pyplot as plt

    return (plt,)


if __name__ == "__main__":
    app.run()
