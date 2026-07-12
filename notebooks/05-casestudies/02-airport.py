import marimo

__generated_with = "0.23.14"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell(hide_code=True)
def _(mo):
    mo.Html("""
    <div class="nams-hero">
    <style>
      .nams-hero{color:#e2e8f0;margin:0;font-family:inherit}
      .nams-hero__grid{display:grid;gap:22px;grid-template-columns:minmax(0,1.25fr) minmax(200px,0.85fr);padding:32px 28px;border-radius:14px;background:linear-gradient(135deg,#0f172a 0%,#1e293b 100%)}
      @media(max-width:760px){.nams-hero__grid{grid-template-columns:1fr;padding:22px 16px}}
      .nams-badge{display:inline-flex;align-items:center;gap:8px;padding:6px 12px;border:1px solid rgba(96,165,250,0.3);background:rgba(96,165,250,0.1);border-radius:999px;color:#60a5fa;font-size:0.72rem;font-weight:800;letter-spacing:0.06em;text-transform:uppercase}
      .nams-hero h1{margin:14px 0 8px;font-size:2.2rem;line-height:1.05;font-weight:880;letter-spacing:-0.02em;color:#f1f5f9}
      .nams-hero h1 .nams-em{color:#60a5fa}
      .nams-hero p.lead{margin:0;max-width:520px;color:#94a3b8;font-size:1.02rem;line-height:1.5}
      .nams-byline{margin-top:16px;color:#64748b;font-size:0.88rem;line-height:1.5}
      .nams-byline b{color:#cbd5e1}
      .nams-art{display:flex;align-items:center;justify-content:center}
    </style>
    <div class="nams-hero__grid">
      <div>
        <span class="nams-badge">Chapter 05 &middot; Case Study</span>
        <h1>US Airport<br><span class="nams-em">Network</span></h1>
        <p class="lead">25 years of flight data (1990&ndash;2015) as a directed graph. PageRank, betweenness, connected components, and shortest paths reveal the architecture of American air travel.</p>
        <div class="nams-byline">Network Analysis Made Simple &middot; <b>Eric Ma</b></div>
      </div>
      <div class="nams-art">
        <svg viewBox="0 0 140 120" style="width:100%;max-width:170px;height:auto">
          <!-- flight paths as arcs between airport dots on a map-like layout -->
          <line x1="20" y1="80" x2="60" y2="35" stroke="#60a5fa" stroke-width="1" opacity="0.2" stroke-linecap="round"/>
          <line x1="35" y1="90" x2="60" y2="35" stroke="#60a5fa" stroke-width="1" opacity="0.15" stroke-linecap="round"/>
          <line x1="60" y1="35" x2="100" y2="50" stroke="#60a5fa" stroke-width="1.2" opacity="0.25" stroke-linecap="round"/>
          <line x1="20" y1="80" x2="100" y2="50" stroke="#60a5fa" stroke-width="0.8" opacity="0.12" stroke-linecap="round"/>
          <line x1="35" y1="90" x2="100" y2="50" stroke="#60a5fa" stroke-width="1" opacity="0.18" stroke-linecap="round"/>
          <line x1="100" y1="50" x2="120" y2="85" stroke="#60a5fa" stroke-width="1" opacity="0.2" stroke-linecap="round"/>
          <line x1="60" y1="35" x2="120" y2="85" stroke="#60a5fa" stroke-width="0.8" opacity="0.1" stroke-linecap="round"/>
          <line x1="35" y1="90" x2="75" y2="100" stroke="#60a5fa" stroke-width="0.8" opacity="0.12" stroke-linecap="round"/>
          <line x1="75" y1="100" x2="120" y2="85" stroke="#60a5fa" stroke-width="1" opacity="0.15" stroke-linecap="round"/>
          <!-- airport nodes: hubs larger -->
          <circle cx="20" cy="80" r="4.5" fill="#60a5fa" opacity="0.8"/>
          <circle cx="35" cy="90" r="3.5" fill="#3b82f6" opacity="0.6"/>
          <circle cx="60" cy="35" r="6" fill="#60a5fa" opacity="0.9"/>
          <circle cx="100" cy="50" r="5.5" fill="#60a5fa" opacity="0.85"/>
          <circle cx="120" cy="85" r="4" fill="#3b82f6" opacity="0.7"/>
          <circle cx="75" cy="100" r="3" fill="#2563eb" opacity="0.5"/>
          <!-- hub labels -->
          <text x="60" y="25" text-anchor="middle" fill="#93c5fd" font-size="5" font-weight="600" opacity="0.5">ORD</text>
          <text x="100" y="40" text-anchor="middle" fill="#93c5fd" font-size="5" font-weight="600" opacity="0.5">ATL</text>
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
def _():
    import networkx as nx
    import matplotlib.pyplot as plt
    import warnings

    warnings.filterwarnings("ignore")
    return nx, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Introduction

    In this chapter, we will analyse the evolution of US Airport Network between 1990 and 2015. This dataset contains data for 25 years[1995-2015] of flights between various US airports and metadata about these routes. Taken from Bureau of Transportation Statistics, United States Department of Transportation.

    Let's see what can we make out of this!
    """)
    return


@app.cell(hide_code=True)
def _():
    from nams import load_data as cf

    pass_air_data = cf.load_airports_data()
    return cf, pass_air_data


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the `pass_air_data` dataframe we have the information of number of people that fly every year on a particular route on the list of airlines that fly that route.
    """)
    return


@app.cell
def _(pass_air_data):
    pass_air_data.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Every row in this dataset is a unique route between 2 airports in United States territory in a particular year. Let's see how many people flew from New York JFK to Austin in 2006.

    NOTE: This will be a fun chapter if you are an aviation geek and like guessing airport IATA codes.
    """)
    return


@app.cell
def _(pass_air_data):
    jfk_aus_2006 = pass_air_data.query("YEAR == 2006").query(
        "ORIGIN == 'JFK' and DEST == 'AUS'"
    )

    jfk_aus_2006.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    From the above pandas query we see that according to this dataset 105290 passengers travelled from JFK to AUS in the year 2006.

    But how does this dataset translate to an applied network analysis problem? In the previous chapter we created different graph objects for every book. Let's create a graph object which encompasses all the edges.

    NetworkX provides us with Multi(Di)Graphs to model networks with multiple edges between two nodes.

    In this case every row in the dataframe represents a directed edge between two airports, common sense suggests that if there is a flight from airport A to airport B there should definitely be a flight from airport B to airport A, i.e direction of the edge shouldn't matter. But in this dataset we have data for individual directions (A -> B and B -> A) so we create a MultiDiGraph.
    """)
    return


@app.cell
def _(nx, pass_air_data):
    passenger_graph = nx.from_pandas_edgelist(
        pass_air_data,
        source="ORIGIN",
        target="DEST",
        edge_key="YEAR",
        edge_attr=["PASSENGERS", "UNIQUE_CARRIER_NAME"],
        create_using=nx.MultiDiGraph(),
    )
    return (passenger_graph,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We have created a MultiDiGraph object `passenger_graph` which contains all the information from the dataframe `pass_air_data`. `ORIGIN` and `DEST` represent the column names in the dataframe `pass_air_data` used to construct the edge. As this is a `MultiDiGraph` we can also give a name/key to the multiple edges between two nodes and `edge_key` is used to represent that name and in this graph `YEAR` is used to distinguish between multiple edges between two nodes. `PASSENGERS` and `UNIQUE_CARRIER_NAME` are added as edge attributes which can be accessed using the nodes and the key form the MultiDiGraph object.

    Let's check if we can access the same information (the 2006 route between JFK and AUS) using our `passenger_graph`.

    To check an edge between two nodes in a Graph we can use the syntax `GraphObject[source][target]` and further specify the edge attribute using `GraphObject[source][target][attribute]`.

    <!-- Let's see if `passenger_graph['JFK']['AUS'][2006]` works. -->
    """)
    return


@app.cell
def _(passenger_graph):
    passenger_graph["JFK"]["AUS"][2006]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now let's use our new constructed passenger graph to look at the evolution of passenger load over 25 years.
    """)
    return


@app.cell
def _(passenger_graph, plt):
    _values = [
        (year, attr["PASSENGERS"])
        for year, attr in passenger_graph["JFK"]["SFO"].items()
    ]
    _x, _y = zip(*_values)
    plt.plot(_x, _y)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We see some usual trends all across the datasets like steep drops in 2001 (after 9/11) and 2008 (recession).
    """)
    return


@app.cell
def _(passenger_graph, plt):
    _values = [
        (year, attr["PASSENGERS"])
        for year, attr in passenger_graph["SFO"]["ORD"].items()
    ]
    _x, _y = zip(*_values)
    plt.plot(_x, _y)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    To find the overall trend, we can use our `pass_air_data` dataframe to calculate total passengers flown in a year.
    """)
    return


@app.cell
def _(pass_air_data, plt):
    pass_air_data.groupby(["YEAR"]).sum()["PASSENGERS"].plot()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise

    Find the busiest route in 1990 and in 2015 according to number of passengers, and plot the time series of number of passengers on these routes.

    You can use the DataFrame instead of working with the network. It will be faster :)
    """)
    return


@app.cell
def _():
    from nams.solutions.airport import busiest_route, plot_time_series

    return busiest_route, plot_time_series


@app.cell
def _(busiest_route, pass_air_data):
    busiest_route(pass_air_data, 1990).head()
    return


@app.cell
def _(pass_air_data, plot_time_series):
    plot_time_series(pass_air_data, "LAX", "HNL")
    return


@app.cell
def _(busiest_route, pass_air_data):
    busiest_route(pass_air_data, 2015).head()
    return


@app.cell
def _(pass_air_data, plot_time_series):
    plot_time_series(pass_air_data, "LAX", "SFO")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Before moving to the next part of the chapter let's create a method to extract edges from `passenger_graph` for a particular year so we can better analyse the data on a granular scale.
    """)
    return


@app.cell
def _(nx):
    def year_network(G, year):
        year_network = nx.DiGraph()
        for edge in G.edges:
            source, target, edge_year = edge
            if edge_year == year:
                attr = G[source][target][edge_year]
                year_network.add_edge(
                    source,
                    target,
                    weight=attr["PASSENGERS"],
                    weight_inv=1
                    / (attr["PASSENGERS"] if attr["PASSENGERS"] != 0.0 else 1),
                    airlines=attr["UNIQUE_CARRIER_NAME"],
                )
        return year_network

    return (year_network,)


@app.cell
def _(passenger_graph, year_network):
    pass_2015_network = year_network(passenger_graph, 2015)
    return (pass_2015_network,)


@app.cell
def _(pass_2015_network):
    print(pass_2015_network)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Visualise the airports
    """)
    return


@app.cell
def _(cf, pass_2015_network):
    lat_long = cf.load_airports_GPS_data()
    lat_long.columns = [
        "CODE4",
        "CODE3",
        "CITY",
        "PROVINCE",
        "COUNTRY",
        "UNKNOWN1",
        "UNKNOWN2",
        "UNKNOWN3",
        "UNKNOWN4",
        "UNKNOWN5",
        "UNKNOWN6",
        "UNKNOWN7",
        "UNKNOWN8",
        "UNKNOWN9",
        "LATITUDE",
        "LONGITUDE",
    ]
    lat_long
    wanted_nodes = list(pass_2015_network.nodes())
    us_airports = (
        lat_long.query("CODE3 in @wanted_nodes")
        .drop_duplicates(subset=["CODE3"])
        .set_index("CODE3")
    )
    us_airports.head()
    return (us_airports,)


@app.cell
def _(pass_2015_network, us_airports):
    no_gps = []
    for n, d in pass_2015_network.nodes(data=True):
        try:
            pass_2015_network.nodes[n]["longitude"] = us_airports.loc[n, "LONGITUDE"]
            pass_2015_network.nodes[n]["latitude"] = us_airports.loc[n, "LATITUDE"]
            pass_2015_network.nodes[n]["degree"] = pass_2015_network.degree(n)
        except KeyError:
            no_gps.append(n)

    has_gps = set(pass_2015_network.nodes()).difference(no_gps)
    g = pass_2015_network.subgraph(has_gps)
    return (g,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's first plot only the nodes, i.e airports. Places like Guam, US Virgin Islands are also included in this dataset as they are treated as domestic airports in this dataset.
    """)
    return


@app.cell
def _(g, plt):
    from nxviz import nodes as _nodes, plots as _plots

    plt.figure(figsize=(20, 9))
    _pos = _nodes.geo(g, encodings_kwargs={"size_scale": 1})
    _plots.aspect_equal()
    _plots.despine()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's also plot the routes(edges).
    """)
    return


@app.cell
def _(g, plt):
    from nxviz import (
        nodes as _nodes,
        plots as _plots,
        edges as _edges,
        annotate as _annotate,
    )

    plt.figure(figsize=(20, 9))
    _pos = _nodes.geo(g, color_by="degree", encodings_kwargs={"size_scale": 1})
    _edges.line(g, _pos, encodings_kwargs={"alpha_scale": 0.1})
    _annotate.node_colormapping(g, color_by="degree")
    _plots.aspect_equal()
    _plots.despine()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Before we proceed further, let's take a detour to briefly discuss directed networks and PageRank.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(rf"""
    ## Directed Graphs and PageRank

    The figure below explains the basic idea behind the PageRank algorithm. The "importance" of the node depends on the incoming links to the node, i.e if an "important" node A points towards a node B it will increase the PageRank score of node B, and this is run iteratively. In the given figure, even though node C is only connected to one node it is considered "important" as the connection is to node B, which is an "important" node.

    {mo.image("images/pagerank.png")}
    <!-- <img src='images/pagerank.png' alt='pagerank' width='500'/> -->

    Source: Wikipedia

    To better understand this let's work through an example.
    """)
    return


@app.cell
def _(nx):
    G = nx.DiGraph()
    G.add_edge(1, 2, weight=4)
    return (G,)


@app.cell
def _(G):
    print(G.edges(data=True))
    return


@app.cell
def _(G):
    G[1][2]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What happens when we try to access the edge from 2 to 1?

    ``` python
    G[2][1]

    ---------------------------------------------------------------------------
    KeyError                                  Traceback (most recent call last)
    <ipython-input-137-d6b8db3142ef> in <module>
          1 # Access edge from 2 to 1
    ----> 2 G[2][1]

    ~/miniconda3/envs/nams/lib/python3.7/site-packages/networkx/classes/coreviews.py in __getitem__(self, key)
         52
         53     def __getitem__(self, key):
    ---> 54         return self._atlas[key]
         55
         56     def copy(self):

    KeyError: 1
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As expected we get an error when we try to access the edge between 2 to 1 as this is a directed graph.
    """)
    return


@app.cell
def _(G, nx, plt):
    G.add_edges_from([(1, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2)])
    nx.draw_circular(G, with_labels=True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Just by looking at the example above, we can conclude that node 2 should have the highest PageRank score as all the nodes are pointing towards it.

    This is confirmed by calculating the PageRank of this graph.
    """)
    return


@app.cell
def _(G, nx):
    nx.pagerank(G)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    What happens when we add an edge from node 5 to node 6.
    """)
    return


@app.cell
def _(G, nx, plt):
    G.add_edge(5, 6)
    nx.draw_circular(G, with_labels=True)
    plt.show()
    return


@app.cell
def _(G, nx):
    nx.pagerank(G)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As expected there was some change in the scores (an increase for 6) but the overall trend stays the same, with node 2 leading the pack.
    """)
    return


@app.cell
def _(G, nx, plt):
    G.add_edge(2, 8)
    nx.draw_circular(G, with_labels=True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Now we have an added an edge from 2 to a new node 8. As node 2 already has a high PageRank score, this should be passed on node 8. Let's see how much difference this can make.
    """)
    return


@app.cell
def _(G, nx):
    nx.pagerank(G)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In this example, node 8 is now even more "important" than node 2 even though node 8 has only incoming connection.

    Let's move back to Airports and use this knowledge to analyse the network.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Important Hubs in the Airport Network

    So let's have a look at the important nodes in this network, i.e. important airports in this network. We'll use centrality measures like pagerank, betweenness centrality and degree centrality which we have gone through in this book.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's try to calculate the PageRank of `passenger_graph`.

    ``` python
    nx.pagerank(passenger_graph)

    ---------------------------------------------------------------------------
    NetworkXNotImplemented                    Traceback (most recent call last)
    <ipython-input-144-15a6f513bf9b> in <module>
          1 # Let's try to calculate the PageRank measures of this graph.
    ----> 2 nx.pagerank(passenger_graph)

    <decorator-gen-435> in pagerank(G, alpha, personalization, max_iter, tol, nstart, weight, dangling)

    ~/miniconda3/envs/nams/lib/python3.7/site-packages/networkx/utils/decorators.py in _not_implemented_for(not_implement_for_func, *args, **kwargs)
         78         if match:
         79             msg = 'not implemented for %s type' % ' '.join(graph_types)
    ---> 80             raise nx.NetworkXNotImplemented(msg)
         81         else:
         82             return not_implement_for_func(*args, **kwargs)

    NetworkXNotImplemented: not implemented for multigraph type
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As PageRank isn't defined for a MultiGraph in NetworkX we need to use our extracted yearly sub networks.
    """)
    return


@app.cell
def _(nx, pass_2015_network):
    PR_2015_scores = nx.pagerank(pass_2015_network, weight=None)
    return (PR_2015_scores,)


@app.cell
def _(PR_2015_scores):
    PR_2015_scores["JFK"]
    return


@app.cell
def _(PR_2015_scores):
    top_10_pr = sorted(PR_2015_scores.items(), key=lambda x: x[1], reverse=True)[:10]
    return (top_10_pr,)


@app.cell
def _(nx, pass_2015_network):
    top_10_bc = sorted(
        nx.betweenness_centrality(pass_2015_network, weight=None).items(),
        key=lambda x: x[1],
        reverse=True,
    )[0:10]
    return (top_10_bc,)


@app.cell
def _(nx, pass_2015_network):
    top_10_dc = sorted(
        nx.degree_centrality(pass_2015_network).items(),
        key=lambda x: x[1],
        reverse=True,
    )[0:10]
    return (top_10_dc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Before looking at the results do think about what we just calculated and try to guess which airports should come out at the top and be ready to be surprised :D
    """)
    return


@app.cell
def _(top_10_pr):
    top_10_pr
    return


@app.cell
def _(top_10_bc):
    top_10_bc
    return


@app.cell
def _(top_10_dc):
    top_10_dc
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The Degree Centrality results do make sense at first glance, ATL is Atlanta, ORD is Chicago, these are definitely airports one would expect to be at the top of a list which calculates "importance" of an airport. But when we look at PageRank and Betweenness Centrality we have an unexpected airport 'ANC'. Do think about measures like PageRank and Betweenness Centrality and what they calculate. Do note that currently we have used the core structure of the network, no other metadata like number of passengers. These are calculations on the unweighted network.

    'ANC' is the airport code of Anchorage airport, a place in Alaska, and according to pagerank and betweenness centrality it is the most important airport in this network. Isn't that weird? Thoughts?

    Looks like 'ANC' is essential to the core structure of the network, as it is the main airport connecting Alaska with other parts of US. This explains the high Betweenness Centrality score and there are flights from other major airports to 'ANC' which explains the high PageRank score.

    Related blog post: https://toreopsahl.com/2011/08/12/why-anchorage-is-not-that-important-binary-ties-and-sample-selection/

    Let's look at weighted version, i.e taking into account the number of people flying to these places.
    """)
    return


@app.cell
def _(nx, pass_2015_network):
    sorted(
        nx.betweenness_centrality(pass_2015_network, weight="weight_inv").items(),
        key=lambda x: x[1],
        reverse=True,
    )[0:10]
    return


@app.cell
def _(nx, pass_2015_network):
    sorted(
        nx.pagerank(pass_2015_network, weight="weight").items(),
        key=lambda x: x[1],
        reverse=True,
    )[0:10]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    When we adjust for number of passengers we see that we have a reshuffle in the "importance" rankings, and they do make a bit more sense now. According to weighted PageRank, Atlanta, Chicago, Seattle the top 3 airports while Anchorage is at 4th rank now.

    To get an even better picture of this we should do the analysis with more metadata about the routes not just the number of passengers.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## How reachable is this network?

    Let's assume you are the Head of Data Science of an airline and your job is to make your airline network as "connected" as possible.

    To translate this problem statement to network science, we calculate the average shortest path length of this network, it gives us an idea about the number of jumps we need to make around the network to go from one airport to any other airport in this network on average.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can use the inbuilt networkx method `average_shortest_path_length` to find the average shortest path length of a network.

    ```python
    nx.average_shortest_path_length(pass_2015_network)

    ---------------------------------------------------------------------------
    NetworkXError                             Traceback (most recent call last)
    <ipython-input-157-acfe9bf3572a> in <module>
    ----> 1 nx.average_shortest_path_length(pass_2015_network)

    ~/miniconda3/envs/nams/lib/python3.7/site-packages/networkx/algorithms/shortest_paths/generic.py in average_shortest_path_length(G, weight, method)
        401     # Shortest path length is undefined if the graph is disconnected.
        402     if G.is_directed() and not nx.is_weakly_connected(G):
    --> 403         raise nx.NetworkXError("Graph is not weakly connected.")
        404     if not G.is_directed() and not nx.is_connected(G):
        405         raise nx.NetworkXError("Graph is not connected.")

    NetworkXError: Graph is not weakly connected.

    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Wait, What? This network is not "connected" (ignore the term weakly for the moment).
    That seems weird. It means that there are nodes which aren't reachable from other set of nodes, which isn't good news in especially a transportation network.

    Let's have a look at these far flung airports which aren't reachable.
    """)
    return


@app.cell
def _(nx, pass_2015_network):
    components = list(nx.weakly_connected_components(pass_2015_network))
    return (components,)


@app.cell
def _(components):
    for c in components:
        print(len(c))
    return


@app.cell
def _(components):
    print(components[1])
    print(components[2])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The airports `SSB` and `SPB` are codes for Seaplanes airports and they have flights to each other so it makes sense that they aren't connected to the larger network of airports.

    The airport is even more weird as it is in a component in itself, i.e there is a flight from `AIK` to `AIK`. After investigating further it just seems like an anomaly in this dataset.
    """)
    return


@app.cell
def _(pass_air_data):
    AIK_DEST_2015 = pass_air_data[
        (pass_air_data["YEAR"] == 2015) & (pass_air_data["DEST"] == "AIK")
    ]
    AIK_DEST_2015.head()
    return


@app.cell
def _(pass_2015_network):
    pass_2015_network.remove_nodes_from(["SPB", "SSB", "AIK"])
    return


@app.cell
def _(nx, pass_2015_network):
    nx.is_weakly_connected(pass_2015_network)
    return


@app.cell
def _(nx, pass_2015_network):
    nx.is_strongly_connected(pass_2015_network)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Strongly vs weakly connected graphs.

    Let's go through an example to understand weakly and strongly connected directed graphs.
    """)
    return


@app.cell
def _(nx, plt):
    G_1 = nx.DiGraph()
    G_1.add_edge(1, 2)
    G_1.add_edge(2, 3)
    G_1.add_edge(3, 1)
    nx.draw(G_1, with_labels=True)
    plt.show()
    return (G_1,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In the above example we can reach any node irrespective of where we start traversing the network, if we start from 2 we can reach 1 via 3. In this network every node is "reachable" from one another, i.e the network is strongly connected.
    """)
    return


@app.cell
def _(G_1, nx):
    nx.is_strongly_connected(G_1)
    return


@app.cell
def _(G_1, nx, plt):
    G_1.add_edge(3, 4)
    nx.draw(G_1, with_labels=True)
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    It's evident from the example above that we *can't* traverse the network graph. If we start from node 4 we are stuck at the node, we don't have any way of leaving node 4. This is assuming we strictly follow the direction of edges. In this case the network isn't strongly connected but if we look at the structure and assume the directions of edges don't matter then we can go to any other node in the network even if we start from node 4.

    In the case an undirected copy of directed network is connected we call the directed network as weakly connected.
    """)
    return


@app.cell
def _(G_1, nx):
    nx.is_strongly_connected(G_1)
    return


@app.cell
def _(G_1, nx):
    nx.is_weakly_connected(G_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's go back to our airport network of 2015.

    After removing those 3 airports the network is weakly connected.
    """)
    return


@app.cell
def _(nx, pass_2015_network):
    nx.is_weakly_connected(pass_2015_network)
    return


@app.cell
def _(nx, pass_2015_network):
    nx.is_strongly_connected(pass_2015_network)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    But our network is still not strongly connected, which essentially means there are airports in the network where you can fly into but not fly back, which doesn't really seem okay
    """)
    return


@app.cell
def _(nx, pass_2015_network):
    strongly_connected_components = list(
        nx.strongly_connected_components(pass_2015_network)
    )
    return (strongly_connected_components,)


@app.cell
def _(strongly_connected_components):
    strongly_connected_components[0]
    return


@app.cell
def _(pass_air_data):
    bce_2015 = pass_air_data.query("YEAR == 2015").query(
        "ORIGIN == 'BCE' or DEST == 'BCE'"
    )
    bce_2015
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As we can see above you can fly into `BCE` but can't fly out, weird indeed. These airport are small airports with one off schedules flights. For the purposes of our analyses we can ignore such airports.
    """)
    return


@app.cell
def _(strongly_connected_components):
    pass_2015_strong_nodes = max(strongly_connected_components, key=len)
    return (pass_2015_strong_nodes,)


@app.cell
def _(pass_2015_network, pass_2015_strong_nodes):
    pass_2015_strong = pass_2015_network.subgraph(nodes=pass_2015_strong_nodes)
    return (pass_2015_strong,)


@app.cell
def _(nx, pass_2015_strong):
    nx.is_strongly_connected(pass_2015_strong)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    After removing multiple airports we now have a strongly connected airport network. We can now travel from one airport to any other airport in the network.
    """)
    return


@app.cell
def _(pass_2015_strong):
    len(pass_2015_strong)
    return


@app.cell
def _(nx, pass_2015_strong):
    nx.average_shortest_path_length(pass_2015_strong)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The 3.17 number above represents the average length between 2 airports in the network which means that it's possible to go from one airport to another in this network under 3 layovers, which sounds nice. A more reachable network is better, not necessarily in terms of revenue for the airline but for social health of the air transport network.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Exercise

    How can we decrease the average shortest path length of this network?

    Think of an effective way to add new edges to decrease the average shortest path length.
    Let's see if we can come up with a nice way to do this.

    The rules are simple:
    - You can't add more than 2% of the current edges( ~500 edges)
    """)
    return


@app.cell
def _():
    from nams.solutions.airport import add_opinionated_edges

    return (add_opinionated_edges,)


@app.cell
def _(add_opinionated_edges, pass_2015_strong):
    new_routes_network = add_opinionated_edges(pass_2015_strong)
    return (new_routes_network,)


@app.cell
def _(new_routes_network, nx):
    nx.average_shortest_path_length(new_routes_network)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Using an opinionated heuristic we were able to reduce the average shortest path length of the network. Check the solution below to understand the idea behind the heuristic, do try to come up with your own heuristics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Can we find airline specific reachability?

    Let's see how we can use the airline metadata to calculate the reachability of a specific airline.
    """)
    return


@app.cell
def _(pass_2015_network):
    pass_2015_network["JFK"]["SFO"]
    return


@app.function
def str_to_list(a):
    return a[1:-1].split(", ")


@app.cell
def _(pass_2015_network):
    for _origin, _dest in pass_2015_network.edges():
        pass_2015_network[_origin][_dest]["airlines_list"] = str_to_list(
            pass_2015_network[_origin][_dest]["airlines"]
        )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Let's extract the network of United Airlines from our airport network.
    """)
    return


@app.cell
def _(nx, pass_2015_network):
    united_network = nx.DiGraph()
    for _origin, _dest in pass_2015_network.edges():
        if (
            "'United Air Lines Inc.'"
            in pass_2015_network[_origin][_dest]["airlines_list"]
        ):
            united_network.add_edge(
                _origin, _dest, weight=pass_2015_network[_origin][_dest]["weight"]
            )
    return (united_network,)


@app.cell
def _(united_network):
    print(united_network)
    return


@app.cell
def _(nx, united_network):
    sorted(
        nx.pagerank(united_network, weight="weight").items(),
        key=lambda x: x[1],
        reverse=True,
    )[0:5]
    return


@app.cell
def _(nx, united_network):
    sorted(
        nx.degree_centrality(united_network).items(), key=lambda x: x[1], reverse=True
    )[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Solutions

    Here are the solutions to the exercises above.
    """)
    return


@app.cell
def _():
    from nams.solutions import airport
    import inspect

    print(inspect.getsource(airport))
    return


@app.cell(hide_code=True)
def _(mo):
    import wigglystuff

    tour = wigglystuff.CellTour(
        steps=[
            {
                "cell": 0,
                "title": "US Airport Network",
                "description": "25 years of flight data as a directed graph.",
            },
            {
                "cell": 5,
                "title": "Dataset",
                "description": "Passenger counts between US airports, 1990-2015.",
            },
            {
                "cell": 9,
                "title": "Building the graph",
                "description": "MultiDiGraph with year-keyed edges from pandas.",
            },
            {
                "cell": 17,
                "title": "Passenger trends",
                "description": "How air traffic grew over 25 years.",
            },
            {
                "cell": 25,
                "title": "Yearly subnetworks",
                "description": "Extract a single year for analysis.",
            },
            {
                "cell": 32,
                "title": "Geographic visualization",
                "description": "Plot airports on a US map with nxviz.",
            },
            {
                "cell": 44,
                "title": "PageRank",
                "description": "Which airports are the most important hubs?",
            },
            {
                "cell": 56,
                "title": "Centrality comparison",
                "description": "PageRank vs betweenness vs degree on the 2015 network.",
            },
            {
                "cell": 72,
                "title": "Connected components",
                "description": "Strongly vs weakly connected components.",
            },
            {
                "cell": 101,
                "title": "Shortest paths",
                "description": "Average path length and network reachability.",
            },
            {
                "cell": 104,
                "title": "Adding routes",
                "description": "Opinionated heuristic to improve connectivity.",
            },
        ],
        auto_start=False,
        show_progress=True,
    )
    mo.ui.anywidget(tour)
    return


if __name__ == "__main__":
    app.run()
