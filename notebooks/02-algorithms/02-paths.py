import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def startup():
    import inspect
    import json
    import warnings
    from collections import deque
    from random import sample

    warnings.filterwarnings("ignore")

    import anywidget
    import marimo as mo
    import matplotlib.pyplot as plt
    import networkx as nx
    import nxviz as nv
    import pandas as pd
    import traitlets
    import wigglystuff

    from nams import load_data as cf
    from nams.solutions import paths
    from nams.solutions.paths import (
        bfs_algorithm,
        path_exists as path_exists_solution,
        plot_degree_betweenness,
        plot_path_with_neighbors,
    )

    return (
        anywidget,
        cf,
        deque,
        inspect,
        json,
        mo,
        nv,
        nx,
        paths,
        pd,
        plot_degree_betweenness,
        plot_path_with_neighbors,
        plt,
        sample,
        traitlets,
        wigglystuff,
    )


@app.cell(hide_code=True)
def hero(mo):
    mo.Html(f"""
    <div class="nams-hero">
    <style>
      .nams-hero{{color:#e2e8f0;margin:0;font-family:inherit}}
      .nams-hero__grid{{display:grid;gap:22px;grid-template-columns:minmax(0,1.25fr) minmax(200px,0.85fr);padding:32px 28px;border-radius:14px;background:linear-gradient(135deg,#0f172a 0%,#1e293b 100%)}}
      @media(max-width:760px){{.nams-hero__grid{{grid-template-columns:1fr;padding:22px 16px}}}}
      .nams-badge{{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border:1px solid rgba(251,146,60,0.3);background:rgba(251,146,60,0.1);border-radius:999px;color:#fb923c;font-size:0.72rem;font-weight:800;letter-spacing:0.06em;text-transform:uppercase}}
      .nams-hero h1{{margin:14px 0 8px;font-size:2.2rem;line-height:1.05;font-weight:880;letter-spacing:-0.02em;color:#f1f5f9}}
      .nams-hero h1 .nams-em{{color:#fb923c}}
      .nams-hero p.lead{{margin:0;max-width:520px;color:#94a3b8;font-size:1.02rem;line-height:1.5}}
      .nams-byline{{margin-top:16px;color:#64748b;font-size:0.88rem;line-height:1.5}}
      .nams-byline b{{color:#cbd5e1}}
      .nams-art{{display:flex;align-items:center;justify-content:center}}
    </style>
    <div class="nams-hero__grid">
      <div>
        <span class="nams-badge">Chapter 02 &middot; Algorithms</span>
        <h1>Paths &amp;<br><span class="nams-em">Traversal</span></h1>
        <p class="lead">How do you get from node A to node B? Breadth-first search explores outward layer by layer, finding shortest paths and revealing the bottleneck nodes that hold a network together.</p>
        <div class="nams-byline">Network Analysis Made Simple &middot; <b>Eric Ma</b></div>
      </div>
      <div class="nams-art">
        <svg viewBox="0 0 150 120" style="width:100%;max-width:180px;height:auto">
          <!-- dimmed background edges -->
          <line x1="25" y1="25" x2="60" y2="50" stroke="#fb923c" stroke-width="1" opacity="0.15" stroke-linecap="round"/>
          <line x1="60" y1="50" x2="95" y2="30" stroke="#fb923c" stroke-width="1" opacity="0.15" stroke-linecap="round"/>
          <line x1="95" y1="30" x2="125" y2="55" stroke="#fb923c" stroke-width="1" opacity="0.15" stroke-linecap="round"/>
          <line x1="60" y1="50" x2="80" y2="85" stroke="#fb923c" stroke-width="1" opacity="0.15" stroke-linecap="round"/>
          <line x1="80" y1="85" x2="125" y2="95" stroke="#fb923c" stroke-width="1" opacity="0.15" stroke-linecap="round"/>
          <line x1="25" y1="25" x2="50" y2="90" stroke="#fb923c" stroke-width="1" opacity="0.12" stroke-linecap="round"/>
          <line x1="50" y1="90" x2="80" y2="85" stroke="#fb923c" stroke-width="1" opacity="0.12" stroke-linecap="round"/>
          <!-- highlighted path edges: start -> mid -> mid -> end -->
          <line x1="25" y1="25" x2="60" y2="50" stroke="#fb923c" stroke-width="2.5" opacity="0.8" stroke-linecap="round"/>
          <line x1="60" y1="50" x2="80" y2="85" stroke="#fb923c" stroke-width="2.5" opacity="0.8" stroke-linecap="round"/>
          <line x1="80" y1="85" x2="125" y2="95" stroke="#fb923c" stroke-width="2.5" opacity="0.8" stroke-linecap="round"/>
          <!-- dimmed off-path nodes -->
          <circle cx="95" cy="30" r="4" fill="#c2410c" opacity="0.35"/>
          <circle cx="125" cy="55" r="4" fill="#c2410c" opacity="0.35"/>
          <circle cx="50" cy="90" r="3.5" fill="#c2410c" opacity="0.3"/>
          <!-- highlighted path nodes -->
          <circle cx="25" cy="25" r="6" fill="#fb923c" opacity="0.9"/>
          <circle cx="60" cy="50" r="5" fill="#fb923c" opacity="0.85"/>
          <circle cx="80" cy="85" r="5" fill="#fb923c" opacity="0.85"/>
          <circle cx="125" cy="95" r="6" fill="#fb923c" opacity="0.9"/>
          <!-- start/end labels -->
          <text x="25" y="14" text-anchor="middle" fill="#fdba74" font-size="7" font-weight="700">start</text>
          <text x="125" y="110" text-anchor="middle" fill="#fdba74" font-size="7" font-weight="700">end</text>
        </svg>
      </div>
    </div>
    </div>
    """)
    return


@app.cell(hide_code=True)
def cell_tour(mo, wigglystuff):

    tour = wigglystuff.CellTour(
        steps=[
        {'cell': 0, 'title': 'Paths & Traversal', 'description': 'How do you get from node A to node B? Breadth-first search explores outward layer by layer.'},
        {'cell': 7, 'title': 'Graph Traversal', 'description': 'Walking along edges node by node to explore local structure and find paths.'},
        {'cell': 8, 'title': 'Breadth-First Search', 'description': 'The BFS algorithm teaches you to think on a graph — exploring one neighbor at a time.'},
        {'cell': 12, 'title': 'Exercise: Implement BFS', 'description': 'Fill in the blanks to check whether a path exists between two nodes using a queue.'},
        {'cell': 15, 'title': 'Visualizing Paths', 'description': 'Use nx.shortest_path and subgraph extraction to draw the route through the graph.'},
        {'cell': 20, 'title': 'Path with Neighbors', 'description': 'An optional exercise to plot a shortest path alongside its neighboring nodes in an arc plot.'},
        {'cell': 24, 'title': 'Bottleneck Nodes', 'description': 'Betweenness centrality identifies nodes through which most shortest paths flow.'},
        {'cell': 27, 'title': 'Exercise: Degree vs Betweenness', 'description': 'Scatter-plot the two centrality measures to see whether they correlate.'},
        {'cell': 31, 'title': 'Why They Differ', 'description': 'A barbell graph illustrates how a low-degree node can have extremely high betweenness.'},
        {'cell': 32, 'title': 'Recap', 'description': 'Summary of BFS, subgraph extraction, and betweenness centrality.'},
    ],
        auto_start=False,
        show_progress=True,
    )
    mo.ui.anywidget(tour)
    return


@app.cell(hide_code=True)
def introduction(mo):
    mo.md(r"""
    ## Introduction
    """)
    return


@app.cell(hide_code=True)
def video_link(mo):
    mo.md("""
    Watch the [video on YouTube](https://www.youtube.com/watch?v=JjpbztqP9_0).
    """)
    return


@app.cell(hide_code=True)
def node_importance(mo):
    mo.md(r"""
    ## What makes a node important?

    In the previous notebook, we explored degree centrality as a measure of node importance.
    What other ways can we measure node importance?
    """)
    return


@app.cell(hide_code=True)
def graph_traversal(mo):
    mo.md(r"""
    ## Graph traversal and node importance

    Graph traversal is akin to walking along the graph, node by node,
    constrained by the edges that connect the nodes.
    Graph traversal is particularly useful for understanding
    the local structure of certain portions of the graph
    and for finding paths that connect two nodes in the network.

    In this chapter, we are going to learn how to perform pathfinding in a graph,
    specifically by looking for _shortest paths_ via the _breadth-first search_ algorithm.
    Then, we are going to explore measures of node importance that are related to traversals on a graph!
    """)
    return


@app.cell(hide_code=True)
def bfs_intro(mo):
    mo.md(r"""
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
    """)
    return


@app.cell(hide_code=True)
def bfs_animation_intro(mo):
    mo.md(r"""
    ### Watch BFS in action

    Before you implement it yourself, watch breadth-first search sweep outward from the source node **S**.
    Press **Play** (or step through manually) and notice two things:

    1. Nodes light up in **rings** — each ring is exactly one edge further from **S** than the last.
    2. The small badge on each node is its **shortest-path distance** from **S**. Because BFS explores in order of distance, that number is guaranteed to be the minimum number of hops.

    The queue is the algorithm's "to-do list"; it pops from the front (FIFO), which is exactly what produces the layer-by-layer wavefront.
    """)
    return


@app.cell(hide_code=True)
def bfs_animation(anywidget, deque, json, traitlets):

    def _compute_bfs_animation_steps(adj, start, target=None, mode="path_exists"):
        """Precompute discrete BFS steps for playback.

        Two modes mirror what students actually write:
          * "path_exists"  — terminate the moment *target* appears in the
            NEIGHBORS of the node being visited (mirrors the path_exists()
            exercise: ``if node2 in neighbors: return True``).  The target is
            never enqueued or visited.
          * "shortest_path" — terminate when *target* is dequeued; reconstruct
            and reveal the shortest path via parent pointers.
        """
        queue = deque()
        visited = set()
        seen = {start}
        dist = {start: 0}
        parent = {start: None}
        queue.append(start)
        steps = [
            {
                "current": None,
                "queue": list(queue),
                "visited": [],
                "frontier": [],
                "dist": dict(dist),
                "message": "Initialize \u2192 enqueue source '{}' (distance 0)".format(
                    start
                ),
                "path": None,
                "path_edges": [],
                "detect_edge": None,
            }
        ]
        found = False
        detector = None
        while queue:
            node = queue.popleft()
            visited.add(node)
            new_nbrs = []
            target_in_neighbors = False
            for nbr in adj[node]:
                if target is not None and nbr == target:
                    target_in_neighbors = True
                if nbr not in seen:
                    queue.append(nbr)
                    seen.add(nbr)
                    dist[nbr] = dist[node] + 1
                    parent[nbr] = node
                    new_nbrs.append(nbr)
            if mode == "path_exists" and target_in_neighbors:
                msg = "Visit '{}' (d={}) \u2192 '{}' is a neighbor \u2192 Path exists!".format(
                    node, dist[node], target
                )
            elif new_nbrs:
                msg = "Visit '{}' (d={}) \u2192 enqueue: {}".format(
                    node, dist[node], ", ".join(new_nbrs)
                )
            else:
                msg = "Visit '{}' (d={}) \u2192 no new neighbors".format(
                    node, dist[node]
                )
            step = {
                "current": node,
                "queue": list(queue),
                "visited": sorted(visited),
                "frontier": new_nbrs,
                "dist": dict(dist),
                "message": msg,
                "path": None,
                "path_edges": [],
                "detect_edge": None,
            }
            steps.append(step)
            if mode == "path_exists" and target_in_neighbors and target is not None:
                found = True
                detector = node
                step["detect_edge"] = [node, target]
                break
            if mode == "shortest_path" and target is not None and node == target:
                found = True
                step["message"] = "\u2713 Found '{}' (d={}) \u2014 terminating early!".format(
                    node, dist[node]
                )
                break
        if found:
            if mode == "path_exists":
                steps.append(
                    {
                        "current": None,
                        "queue": [],
                        "visited": sorted(visited),
                        "frontier": [],
                        "dist": dict(dist),
                        "message": "\u2713 path_exists(S, {}) \u2192 True  (spotted from '{}', never dequeued)".format(
                            target, detector
                        ),
                        "path": None,
                        "path_edges": [[detector, target]],
                        "detect_edge": [detector, target],
                    }
                )
            else:
                path = []
                cur = target
                while cur is not None:
                    path.append(cur)
                    cur = parent[cur]
                path.reverse()
                path_edges = [list(p) for p in zip(path[:-1], path[1:])]
                steps.append(
                    {
                        "current": None,
                        "queue": [],
                        "visited": sorted(visited),
                        "frontier": [],
                        "dist": dict(dist),
                        "message": "Shortest path {} ({} edges)".format(
                            " \u2192 ".join(path), len(path_edges)
                        ),
                        "path": path,
                        "path_edges": path_edges,
                        "detect_edge": None,
                    }
                )
        else:
            steps.append(
                {
                    "current": None,
                    "queue": [],
                    "visited": sorted(visited),
                    "frontier": [],
                    "dist": dict(dist),
                    "message": "\u2713 Queue empty \u2014 target unreachable!",
                    "path": None,
                    "path_edges": [],
                    "detect_edge": None,
                }
            )
        return steps

    # 15-node teaching graph: 4 neighbors at distance 1 from S,
    # a dense middle layer, and terminal leaves. T4 is our target.
    _anim_nodes = [
        {"id": "S", "x": 50, "y": 170, "label": "S"},
        {"id": "A", "x": 205, "y": 45, "label": "A"},
        {"id": "B", "x": 205, "y": 125, "label": "B"},
        {"id": "C", "x": 205, "y": 215, "label": "C"},
        {"id": "D", "x": 205, "y": 295, "label": "D"},
        {"id": "E", "x": 395, "y": 85, "label": "E"},
        {"id": "F", "x": 395, "y": 170, "label": "F"},
        {"id": "G", "x": 395, "y": 255, "label": "G"},
        {"id": "T1", "x": 580, "y": 40, "label": "T1"},
        {"id": "T2", "x": 580, "y": 110, "label": "T2"},
        {"id": "T3", "x": 580, "y": 180, "label": "T3"},
        {"id": "T4", "x": 580, "y": 255, "label": "T4"},
        {"id": "T5", "x": 580, "y": 315, "label": "T5"},
        {"id": "T6", "x": 690, "y": 75, "label": "T6"},
        {"id": "T7", "x": 690, "y": 245, "label": "T7"},
    ]
    _anim_edges = [
        ["S", "A"], ["S", "B"], ["S", "C"], ["S", "D"],
        ["A", "E"], ["A", "F"],
        ["B", "E"], ["B", "F"],
        ["C", "F"], ["C", "G"],
        ["D", "G"],
        ["E", "T1"], ["E", "T6"],
        ["F", "T2"], ["F", "T3"],
        ["G", "T4"], ["G", "T5"],
        ["T6", "T7"],
    ]
    _anim_adj = {n["id"]: [] for n in _anim_nodes}
    for _a, _b in _anim_edges:
        _anim_adj[_a].append(_b)
        _anim_adj[_b].append(_a)
    _anim_steps_exists = _compute_bfs_animation_steps(_anim_adj, "S", target="T4", mode="path_exists")
    _anim_steps_path = _compute_bfs_animation_steps(_anim_adj, "S", target="T4", mode="shortest_path")

    class BFSAnimation(anywidget.AnyWidget):
        """Auto-playing breadth-first search walkthrough on a minimal graph."""

        _esm = r"""
        function render({ model, el }) {
            const nodes = JSON.parse(model.get("nodes_json"));
            const edges = JSON.parse(model.get("edges_json"));
            const stepsExists = JSON.parse(model.get("steps_exists_json"));
            const stepsPath = JSON.parse(model.get("steps_path_json"));
            let delay = model.get("speed_ms") || 900;
            const SVGNS = "http://www.w3.org/2000/svg";
            const LAYER = ["#3b82f6", "#06b6d4", "#22c55e", "#eab308", "#a855f7", "#ec4899"];

            let mode = "exists";
            let steps = stepsExists;
            let stepIdx = 0;
            let timer = null;
            let playing = false;

            el.className = "bfsa";

            el.innerHTML = `
                <div class="bfsa-header">
                    <span class="bfsa-title">Breadth-First Search</span>
                    <span class="bfsa-subtitle">target: T4 \u00b7 terminate when spotted in neighbors</span>
                </div>
                <div class="bfsa-modes">
                    <button class="bfsa-btn bfsa-mode is-active" data-mode="exists">path_exists</button>
                    <button class="bfsa-btn bfsa-mode" data-mode="path">shortest path</button>
                </div>
                <svg viewBox="0 0 740 340" class="bfsa-svg"></svg>
                <div class="bfsa-message"></div>
                <div class="bfsa-queues">
                    <div class="bfsa-qbox">
                        <span class="bfsa-qlabel">queue (FIFO)</span>
                        <span class="bfsa-qval bfsa-queue"></span>
                    </div>
                    <div class="bfsa-qbox">
                        <span class="bfsa-qlabel">visited</span>
                        <span class="bfsa-qval bfsa-visited"></span>
                    </div>
                </div>
                <div class="bfsa-legend">
                    <span class="bfsa-leg"><span class="bfsa-dot bfsa-unvisited"></span>unvisited</span>
                    <span class="bfsa-leg"><span class="bfsa-dot bfsa-queued"></span>queued</span>
                    <span class="bfsa-leg"><span class="bfsa-dot bfsa-current"></span>current</span>
                    <span class="bfsa-leg"><span class="bfsa-dot bfsa-layer"></span>visited &middot; by distance</span>
                    <span class="bfsa-leg"><span class="bfsa-dot bfsa-detect"></span>discovery edge</span>
                    <span class="bfsa-leg"><span class="bfsa-dot bfsa-pathdot"></span>shortest path</span>
                </div>
                <div class="bfsa-controls">
                    <button class="bfsa-btn bfsa-play">\u25B6 Play</button>
                    <button class="bfsa-btn bfsa-step">Step \u25B8</button>
                    <button class="bfsa-btn bfsa-reset">Reset \u21BA</button>
                    <span class="bfsa-spacer"></span>
                    <span class="bfsa-speeds">
                        <button class="bfsa-btn bfsa-speed" data-delay="1400">Slow</button>
                        <button class="bfsa-btn bfsa-speed is-active" data-delay="900">Normal</button>
                        <button class="bfsa-btn bfsa-speed" data-delay="400">Fast</button>
                    </span>
                </div>
                <div class="bfsa-counter"></div>
            `;

            const svg = el.querySelector(".bfsa-svg");
            const msgEl = el.querySelector(".bfsa-message");
            const queueEl = el.querySelector(".bfsa-queue");
            const visitedEl = el.querySelector(".bfsa-visited");
            const counterEl = el.querySelector(".bfsa-counter");
            const subtitleEl = el.querySelector(".bfsa-subtitle");
            const playBtn = el.querySelector(".bfsa-play");
            const stepBtn = el.querySelector(".bfsa-step");
            const resetBtn = el.querySelector(".bfsa-reset");

            const nodeCircles = {};
            const nodeBadges = {};

            // draw edges
            edges.forEach(([a, b]) => {
                const na = nodes.find(n => n.id === a);
                const nb = nodes.find(n => n.id === b);
                const line = document.createElementNS(SVGNS, "line");
                line.setAttribute("x1", na.x);
                line.setAttribute("y1", na.y);
                line.setAttribute("x2", nb.x);
                line.setAttribute("y2", nb.y);
                line.setAttribute("class", "bfsa-edge");
                line.setAttribute("data-edge", [a, b].sort().join("-"));
                svg.appendChild(line);
            });

            // draw nodes + distance badges
            nodes.forEach(n => {
                const g = document.createElementNS(SVGNS, "g");
                g.setAttribute("transform", `translate(${n.x},${n.y})`);
                const circle = document.createElementNS(SVGNS, "circle");
                circle.setAttribute("r", 20);
                circle.setAttribute("class", "bfsa-node");
                const text = document.createElementNS(SVGNS, "text");
                text.setAttribute("text-anchor", "middle");
                text.setAttribute("dy", "0.35em");
                text.setAttribute("class", "bfsa-label");
                text.textContent = n.label;
                const badgeG = document.createElementNS(SVGNS, "g");
                badgeG.setAttribute("transform", "translate(16,-16)");
                badgeG.setAttribute("class", "bfsa-badge");
                const bg = document.createElementNS(SVGNS, "circle");
                bg.setAttribute("r", 8);
                bg.setAttribute("class", "bfsa-badge-bg");
                const bt = document.createElementNS(SVGNS, "text");
                bt.setAttribute("text-anchor", "middle");
                bt.setAttribute("dy", "0.35em");
                bt.setAttribute("class", "bfsa-badge-txt");
                badgeG.appendChild(bg);
                badgeG.appendChild(bt);
                badgeG.style.display = "none";
                g.appendChild(circle);
                g.appendChild(text);
                g.appendChild(badgeG);
                svg.appendChild(g);
                nodeCircles[n.id] = circle;
                nodeBadges[n.id] = { g: badgeG, txt: bt };
            });

            function layerColor(d) { return LAYER[d % LAYER.length]; }

            function update() {
                const step = steps[stepIdx];
                const visitedSet = new Set(step.visited);
                const queueSet = new Set(step.queue);
                const pathSet = new Set(step.path || []);
                const showingPath = !!(step.path && step.path.length);
                const showingDetect = !!step.detect_edge;
                const reveal = showingPath || showingDetect;
                nodes.forEach(n => {
                    const c = nodeCircles[n.id];
                    const b = nodeBadges[n.id];
                    c.classList.remove("is-current", "is-path");
                    let fill, stroke, sw = 3;
                    const onPath = showingPath && pathSet.has(n.id);
                    const isDetectTarget = showingDetect && step.detect_edge[1] === n.id;
                    if (n.id === step.current) {
                        fill = "#facc15"; stroke = "#fef08a";
                        c.classList.add("is-current");
                    } else if (onPath) {
                        fill = layerColor(step.dist[n.id]); stroke = "#fde68a"; sw = 6;
                        c.classList.add("is-path");
                    } else if (isDetectTarget) {
                        fill = "#34d399"; stroke = "#a7f3d0"; sw = 6;
                    } else if (visitedSet.has(n.id)) {
                        fill = layerColor(step.dist[n.id]); stroke = "#e2e8f0";
                    } else if (queueSet.has(n.id)) {
                        fill = "#f59e0b"; stroke = "#fbbf24";
                    } else {
                        fill = "#334155"; stroke = "#475569";
                    }
                    if (reveal && !onPath && !isDetectTarget) {
                        c.style.opacity = "0.3";
                    } else {
                        c.style.opacity = "1";
                    }
                    c.setAttribute("fill", fill);
                    c.setAttribute("stroke", stroke);
                    c.setAttribute("stroke-width", sw);
                    if (step.dist && (n.id in step.dist)) {
                        b.txt.textContent = step.dist[n.id];
                        b.g.style.display = "";
                        b.g.style.opacity = (reveal && !onPath && !isDetectTarget) ? "0.3" : "1";
                    } else {
                        b.g.style.display = "none";
                    }
                });
                svg.querySelectorAll(".bfsa-edge").forEach(e => {
                    e.classList.remove("is-active", "is-path", "is-detect");
                    e.style.opacity = reveal ? "0.18" : "1";
                });
                if (step.current) {
                    (step.frontier || []).forEach(f => {
                        const key = [step.current, f].sort().join("-");
                        const ln = svg.querySelector(`.bfsa-edge[data-edge="${key}"]`);
                        if (ln) ln.classList.add("is-active");
                    });
                }
                (step.path_edges || []).forEach(([a, b]) => {
                    const key = [a, b].sort().join("-");
                    const ln = svg.querySelector(`.bfsa-edge[data-edge="${key}"]`);
                    if (ln) {
                        if (showingDetect) ln.classList.add("is-detect");
                        else ln.classList.add("is-path");
                        ln.style.opacity = "1";
                    }
                });
                msgEl.textContent = step.message;
                queueEl.textContent = step.queue.length ? step.queue.join("  ") : "\u2205";
                visitedEl.textContent = step.visited.length ? step.visited.join(", ") : "\u2205";
                counterEl.textContent = "step " + (stepIdx + 1) + " / " + steps.length;
                playBtn.innerHTML = playing ? "\u275A\u275A Pause" : "\u25B6 Play";
                stepBtn.disabled = stepIdx >= steps.length - 1;
            }

            function clearTimer() { if (timer) { clearInterval(timer); timer = null; } }
            function startTimer() {
                clearTimer();
                timer = setInterval(() => {
                    if (stepIdx < steps.length - 1) { stepIdx++; update(); }
                    else { pause(); }
                }, delay);
            }
            function play() {
                if (stepIdx >= steps.length - 1) stepIdx = 0;
                playing = true;
                update();
                startTimer();
            }
            function pause() { playing = false; clearTimer(); update(); }

            playBtn.onclick = () => { playing ? pause() : play(); };
            stepBtn.onclick = () => { pause(); if (stepIdx < steps.length - 1) { stepIdx++; update(); } };
            resetBtn.onclick = () => { pause(); stepIdx = 0; update(); };

            el.querySelectorAll(".bfsa-speed").forEach(btn => {
                btn.onclick = () => {
                    delay = parseInt(btn.dataset.delay, 10);
                    el.querySelectorAll(".bfsa-speed").forEach(x => x.classList.remove("is-active"));
                    btn.classList.add("is-active");
                    if (playing) startTimer();
                };
            });

            function setMode(m) {
                mode = m;
                steps = (m === "path") ? stepsPath : stepsExists;
                el.querySelectorAll(".bfsa-mode").forEach(x => x.classList.toggle("is-active", x.dataset.mode === m));
                subtitleEl.textContent = m === "path"
                    ? "target: T4 \u00b7 terminate on dequeue, show shortest path"
                    : "target: T4 \u00b7 terminate when spotted in neighbors";
                pause();
                stepIdx = 0;
                update();
                setTimeout(play, 300);
            }
            el.querySelectorAll(".bfsa-mode").forEach(btn => {
                btn.onclick = () => setMode(btn.dataset.mode);
            });

            update();
            setTimeout(play, 600);
        }
        export default { render };
        """

        _css = r"""
        .bfsa {
            font-family: system-ui, -apple-system, sans-serif;
            max-width: 780px;
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 20px;
            background: #0f172a;
        }
        .bfsa-header { display: flex; align-items: baseline; gap: 8px; margin-bottom: 6px; }
        .bfsa-title { font-size: 1.15em; font-weight: 700; color: #f1f5f9; }
        .bfsa-subtitle { font-size: 0.8em; color: #64748b; }
        .bfsa-modes { display: inline-flex; gap: 4px; margin-bottom: 10px; }
        .bfsa-svg { width: 100%; height: 340px; }
        .bfsa-node {
            stroke-width: 3;
            transition: fill 0.3s ease, stroke 0.3s ease, opacity 0.3s ease;
            transform-box: fill-box;
            transform-origin: center;
        }
        .bfsa-node.is-current { animation: bfsa-pulse 1s ease-in-out infinite; }
        @keyframes bfsa-pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.13); }
        }
        .bfsa-edge { stroke: #1e293b; stroke-width: 2.5; transition: stroke 0.3s, stroke-width 0.3s, opacity 0.3s; }
        .bfsa-edge.is-active { stroke: #fde68a; stroke-width: 4.5; }
        .bfsa-edge.is-detect { stroke: #34d399; stroke-width: 5.5; }
        .bfsa-edge.is-path { stroke: #fde68a; stroke-width: 5.5; }
        .bfsa-label {
            fill: #fff; font-size: 13px; font-weight: 700;
            pointer-events: none; user-select: none;
        }
        .bfsa-badge-bg { fill: #0f172a; stroke: #e2e8f0; stroke-width: 1.5; }
        .bfsa-badge-txt {
            fill: #e2e8f0; font-size: 9px; font-weight: 700;
            pointer-events: none; user-select: none;
        }
        .bfsa-message {
            color: #e2e8f0; font-size: 0.92em; min-height: 1.4em;
            margin: 10px 0 8px; font-family: ui-monospace, "SF Mono", monospace;
        }
        .bfsa-queues { display: flex; gap: 18px; margin-bottom: 10px; }
        .bfsa-qbox { display: flex; flex-direction: column; gap: 3px; }
        .bfsa-qlabel {
            font-size: 0.68em; text-transform: uppercase;
            letter-spacing: 0.05em; color: #64748b; font-weight: 600;
        }
        .bfsa-qval {
            font-size: 0.88em; color: #cbd5e1;
            font-family: ui-monospace, "SF Mono", monospace;
        }
        .bfsa-legend {
            display: flex; flex-wrap: wrap; align-items: center;
            gap: 4px 10px; font-size: 0.76em; color: #94a3b8; margin-bottom: 12px;
        }
        .bfsa-leg { display: inline-flex; align-items: center; gap: 5px; }
        .bfsa-dot { display: inline-block; width: 12px; height: 12px; border-radius: 50%; border: 2px solid; }
        .bfsa-dot.bfsa-unvisited { background: #334155; border-color: #475569; }
        .bfsa-dot.bfsa-queued { background: #f59e0b; border-color: #fbbf24; }
        .bfsa-dot.bfsa-current { background: #facc15; border-color: #fef08a; }
        .bfsa-dot.bfsa-layer { background: linear-gradient(90deg,#3b82f6,#06b6d4,#22c55e); border-color: #e2e8f0; }
        .bfsa-dot.bfsa-detect { background: #34d399; border-color: #a7f3d0; }
        .bfsa-dot.bfsa-pathdot { background: transparent; border-color: #fde68a; border-width: 3px; }
        .bfsa-controls { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
        .bfsa-btn {
            padding: 7px 16px; border-radius: 8px; border: 1px solid #475569;
            background: #1e293b; color: #e2e8f0; cursor: pointer;
            font-size: 0.88em; font-weight: 500; transition: background 0.15s, border-color 0.15s;
        }
        .bfsa-btn:hover { background: #334155; }
        .bfsa-btn:active { transform: scale(0.97); }
        .bfsa-btn:disabled { opacity: 0.4; cursor: not-allowed; }
        .bfsa-btn.is-active { background: #fb923c; border-color: #fdba74; color: #1e293b; }
        .bfsa-spacer { flex: 1; }
        .bfsa-speeds, .bfsa-modes { display: inline-flex; gap: 4px; }
        .bfsa-counter {
            margin-top: 8px; font-size: 0.74em; color: #64748b;
            font-family: ui-monospace, monospace;
        }
        """

        speed_ms = traitlets.Int(900).tag(sync=True)
        nodes_json = traitlets.Unicode(json.dumps(_anim_nodes)).tag(sync=True)
        edges_json = traitlets.Unicode(json.dumps(_anim_edges)).tag(sync=True)
        steps_exists_json = traitlets.Unicode(json.dumps(_anim_steps_exists)).tag(sync=True)
        steps_path_json = traitlets.Unicode(json.dumps(_anim_steps_path)).tag(sync=True)

    BFSAnimation()

    return


@app.cell(hide_code=True)
def load_graph(cf):
    G = cf.load_sociopatterns_network() 
    return (G,)


@app.cell
def bfs_algorithm_reveal():

    # UNCOMMENT NEXT LINE TO GET THE ANSWER.
    # bfs_algorithm()
    return


@app.cell(hide_code=True)
def implement_exercise(mo):
    mo.md(r"""
    ### Exercise: Implement the algorithm

    > Now that you've seen how the algorithm works, try implementing it!
    """)
    return


@app.cell
def path_exists_stub(
    ____,
    _____,
    _________,
    ___________,
    _____________,
    _________________,
):
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
def path_exists_solution_reveal():
    # UNCOMMENT THE FOLLOWING LINES TO SEE THE ANSWER
    # print(inspect.getsource(path_exists_solution))
    return


@app.cell
def test_path_exists(G, nx, path_exists, sample):
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
    return


@app.cell(hide_code=True)
def visualizing_paths(mo):
    mo.md(r"""
    ## Visualizing Paths

    One of the objectives of that exercise before was to help you "think on graphs".
    Now that you've learned how to do so, you might be wondering,
    "How do I visualize that path through the graph?"

    Well first off, if you inspect the `test_path_exists` function above,
    you'll notice that NetworkX provides a `shortest_path()` function
    that you can use. Here's what using `nx.shortest_path()` looks like.
    """)
    return


@app.cell
def shortest_path_example(G, nx):
    path = nx.shortest_path(G, 7, 400)
    path
    return (path,)


@app.cell(hide_code=True)
def subgraph_explanation(mo):
    mo.md(r"""
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
    """)
    return


@app.cell(hide_code=True)
def matrix_plot(G, nv, path):
    g = G.subgraph(path)
    nv.matrix(g, sort_by="order")
    return


@app.cell(hide_code=True)
def frozen_graph_note(mo):
    mo.md(r"""
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
    """)
    return


@app.cell(hide_code=True)
def path_neighbors_exercise(mo):
    mo.md(r"""
    ### (Optional) Exercise: Draw path with neighbors of the path nodes

    If there's enough time, we will work through this exercise. If not, we will simply discuss the plot.

    Try out this next puzzle 🧩:

    > Plot an arc plot, in which all nodes from G are ordered on the x-axis.
    > Make a subgraph of the path nodes + their neighbors,
    > and then plot the edges in the arc plot.
    > Finally, highlight the path in red.

    This one is advanced, and if you need to peek at the answer, please feel free to do so.
    """)
    return


@app.cell
def plot_path_stub(plt):


    def plot_path_with_neighbors_answer(G, node1, node2):
        # Your answer here
        plt.show()


    # Now execute `plot_path_with_neighbors_answer`
    return


@app.cell
def plot_path_call(G, plot_path_with_neighbors, plt):
    plot_path_with_neighbors(G, 7, 400)
    plt.show()
    return


@app.cell(hide_code=True)
def arc_plot_note(mo):
    mo.md(r"""
    In this case, we opted for an Arc plot because we only have one grouping of nodes but have a logical way to order them.
    Because the path follows the order, the edges being highlighted automatically look like hops through the graph.
    """)
    return


@app.cell(hide_code=True)
def bottleneck_nodes(mo):
    mo.md(r"""
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
    """)
    return


@app.cell(hide_code=True)
def betweenness_nx(mo):
    mo.md(r"""
    ### Betweenness centrality in NetworkX

    NetworkX provides a "betweenness centrality" function
    that behaves consistently with the "degree centrality" function,
    in that it returns a mapping from node to metric:
    """)
    return


@app.cell
def betweenness_series(G, nx, pd):
    pd.Series(nx.betweenness_centrality(G))
    return


@app.cell(hide_code=True)
def scatter_exercise(mo):
    mo.md(r"""
    ### Exercise: compare degree and betweenness centrality

    > Make a scatterplot of degree centrality on the x-axis
    > and betweenness centrality on the y-axis.
    > Do they correlate with one another?
    """)
    return


@app.cell
def exercise_scatter():
    # YOUR ANSWER HERE:
    return


@app.cell
def plot_degree_betweenness_call(G, plot_degree_betweenness, plt):

    plot_degree_betweenness(G)
    plt.show()
    return


@app.cell(hide_code=True)
def think_about_it(mo):
    mo.md(r"""
    ### Think about it...

    ...does it make sense that degree centrality and betweenness centrality
    are not well-correlated?

    Can you think of a scenario where a node has a
    "high" betweenness centrality
    but a "low" degree centrality?
    Before peeking at the graph below,
    think about your answer for a moment.
    """)
    return


@app.cell
def barbell_graph(nx, plt):
    nx.draw(nx.barbell_graph(10, 1))
    plt.show()
    return


@app.cell(hide_code=True)
def recap(mo):
    mo.md(r"""
    ## Recap

    In this chapter, you learned the following things:

    1. You figured out how to implement the breadth-first-search algorithm to find shortest paths.
    1. You learned how to extract subgraphs from a larger graph.
    1. You implemented visualizations of subgraphs, which should help you as you communicate with colleagues.
    1. You calculated betweenness centrality metrics for a graph, and visualized how they correlated with degree centrality.
    """)
    return


@app.cell(hide_code=True)
def solutions_header(mo):
    mo.md(r"""
    ## Solutions

    Here are the solutions to the exercises above.
    """)
    return


@app.cell
def solutions_dump(inspect, paths):
    print(inspect.getsource(paths))
    return


if __name__ == "__main__":
    app.run()
