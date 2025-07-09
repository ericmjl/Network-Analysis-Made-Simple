# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "ipython==9.1.0",
#     "pyjanitor",
#     "marimo",
#     "nams==0.0.2",
#     "networkx==3.4.2",
#     "nxviz==0.7.6",
#     "pandas==2.2.3",
#     "pyprojroot==0.3.0",
#     "tqdm==4.67.1",
#     "matplotlib==3.10.1",
# ]
# [tool.uv.sources]
# nams = { path = "../../", editable = true }
# ///

import marimo

__generated_with = "0.14.9"
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


@app.cell
def _():
    from IPython.display import YouTubeVideo

    YouTubeVideo(id="3sJnTpeFXZ4", width="100%")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In order to get you familiar with graph ideas,
    I have deliberately chosen to steer away from
    the more pedantic matters
    of loading graph data to and from disk.
    That said, the following scenario will eventually happen,
    where a graph dataset lands on your lap,
    and you'll need to load it in memory
    and start analyzing it.

    Thus, we're going to go through graph I/O,
    specifically the APIs on how to convert
    graph data that comes to you
    into that magical NetworkX object `G`.

    Let's get going!

    ## Graph Data as Tables

    Let's recall what we've learned in the introductory chapters.
    Graphs can be represented using two **sets**:

    - Node set
    - Edge set

    ### Node set as tables

    Let's say we had a graph with 3 nodes in it: `A, B, C`.
    We could represent it in plain text, computer-readable format:

    ```csv
    A
    B
    C
    ```

    Suppose the nodes also had metadata.
    Then, we could tag on metadata as well:

    ```csv
    A, circle, 5
    B, circle, 7
    C, square, 9
    ```

    Does this look familiar to you?
    Yes, node sets can be stored in CSV format,
    with one of the columns being node ID,
    and the rest of the columns being metadata.

    ### Edge set as tables

    If, between the nodes, we had 4 edges (this is a directed graph),
    we can also represent those edges in plain text, computer-readable format:

    ```csv
    A, C
    B, C
    A, B
    C, A
    ```

    And let's say we also had other metadata,
    we can represent it in the same CSV format:

    ```csv
    A, C, red
    B, C, orange
    A, B, yellow
    C, A, green
    ```

    If you've been in the data world for a while,
    this should not look foreign to you.
    Yes, edge sets can be stored in CSV format too!
    Two of the columns represent the nodes involved in an edge,
    and the rest of the columns represent the metadata.

    ### Combined Representation

    In fact, one might also choose to combine
    the node set and edge set tables together in a merged format:

    ```
    n1, n2, colour, shape1, num1, shape2, num2
    A,  C,  red,    circle, 5,    square, 9
    B,  C,  orange, circle, 7,    square, 9
    A,  B,  yellow, circle, 5,    circle, 7
    C,  A,  green,  square, 9,    circle, 5
    ```

    In this chapter, the datasets that we will be looking at
    are going to be formatted in both ways.
    Let's get going.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Dataset

    We will be working with the Divvy bike sharing dataset.

    > Divvy is a bike sharing service in Chicago.
    > Since 2013, Divvy has released their bike sharing dataset to the public.
    > The 2013 dataset is comprised of two files:
    > - `Divvy_Stations_2013.csv`, containing the stations in the system, and
    > - `DivvyTrips_2013.csv`, containing the trips.

    Let's dig into the data!
    """
    )
    return


@app.cell
def _():
    from pyprojroot import here

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Firstly, we need to unzip the dataset:""")
    return


@app.cell
def _():
    import zipfile
    import os
    from nams.load_data import datasets

    # This block of code checks to make sure that a particular directory is present.
    if "divvy_2013" not in os.listdir(datasets):
        print("Unzipping the divvy_2013.zip file in the datasets folder.")
        with zipfile.ZipFile(datasets / "divvy_2013.zip", "r") as zip_ref:
            zip_ref.extractall(datasets)
    return (datasets,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Now, let's load in both tables.

    First is the `stations` table:
    """
    )
    return


@app.cell
def _(datasets):
    import pandas as pd

    stations = pd.read_csv(
        datasets / "divvy_2013/Divvy_Stations_2013.csv",
        parse_dates=["online date"],
        encoding="utf-8",
    )
    stations.head()
    return pd, stations


@app.cell
def _(stations):
    stations.describe()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Now, let's load in the `trips` table.""")
    return


@app.cell
def _(datasets, pd):
    trips = pd.read_csv(
        datasets / "divvy_2013/Divvy_Trips_2013.csv",
        parse_dates=["starttime", "stoptime"],
    )
    trips.head()
    return (trips,)


@app.cell
def _(trips):
    import janitor

    trips_summary = (
        trips.groupby(["from_station_id", "to_station_id"])
        .count()
        .reset_index()
        .select_columns(["from_station_id", "to_station_id", "trip_id"])
        .rename_column("trip_id", "num_trips")
    )
    return (trips_summary,)


@app.cell
def _(trips_summary):
    trips_summary.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Graph Model

    Given the data, if we wished to use a graph as a data model
    for the number of trips between stations,
    then naturally, nodes would be the stations,
    and edges would be trips between them.

    This graph would be directed,
    as one could have more trips from station A to B
    and less in the reverse.

    With this definition,
    we can begin graph construction!

    ### Create NetworkX graph from pandas edgelist

    NetworkX provides an extremely convenient way
    to load data from a pandas DataFrame:
    """
    )
    return


@app.cell
def _(trips_summary):
    import networkx as nx

    G = nx.from_pandas_edgelist(
        df=trips_summary,
        source="from_station_id",
        target="to_station_id",
        edge_attr=["num_trips"],
        create_using=nx.DiGraph,
    )
    return (G,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Inspect the graph

    Once the graph is in memory,
    we can inspect it to get out summary graph statistics.
    """
    )
    return


@app.cell
def _(G):
    print(G)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""You'll notice that the edge metadata have been added correctly: we have recorded in there the number of trips between stations.""")
    return


@app.cell
def _(G):
    list(G.edges(data=True))[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""However, the node metadata is not present:""")
    return


@app.cell
def _(G):
    list(G.nodes(data=True))[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Annotate node metadata

    We have rich station data on hand,
    such as the longitude and latitude of each station,
    and it would be a pity to discard it,
    especially when we can potentially use it as part of the analysis
    or for visualization purposes.
    Let's see how we can add this information in.

    Firstly, recall what the `stations` dataframe looked like:
    """
    )
    return


@app.cell
def _(stations):
    stations.head()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    The `id` column gives us the node ID in the graph,
    so if we set `id` to be the index,
    if we then also loop over each row,
    we can treat the rest of the columns as dictionary keys
    and values as dictionary values,
    and add the information into the graph.

    Let's see this in action.
    """
    )
    return


@app.cell
def _(G, stations):
    for node, metadata in stations.set_index("id").iterrows():
        for key, val in metadata.items():
            G.nodes[node][key] = val
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Now, our node metadata should be populated.""")
    return


@app.cell
def _(G):
    list(G.nodes(data=True))[0:5]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    In `nxviz`, a `GeoPlot` object is available
    that allows you to quickly visualize
    a graph that has geographic data.
    However, being `matplotlib`-based,
    it is going to be quickly overwhelmed
    by the sheer number of edges.

    As such, we are going to first filter the edges.

    ### Exercise: Filter graph edges

    > Leveraging what you know about how to manipulate graphs,
    > now try _filtering_ edges.
    >

    _Hint: NetworkX graph objects can be deep-copied using `G.copy()`:_

    ```python
    G_copy = G.copy()
    ```

    _Hint: NetworkX graph objects also let you remove edges:_

    ```python
    G.remove_edge(node1, node2)  # does not return anything
    ```
    """
    )
    return


@app.cell
def _(G, G_________, ___, ____, ___________, d):
    def filter_graph(G, minimum_num_trips):
        """
        Filter the graph such that
        only edges that have minimum_num_trips or more
        are present.
        """
        G_filtered = G.____()
        for _, _, _ in G._____(data=____):
            if d[___________] < ___:
                G_________.___________(_, _)
        return G_filtered

    from nams.solutions.io import filter_graph

    G_filtered = filter_graph(G, 50)
    return (G_filtered,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Visualize using GeoPlot

    `nxviz` provides a GeoPlot object
    that lets you quickly visualize geospatial graph data.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    A note on geospatial visualizations:

    > As the creator of `nxviz`,
    > I would recommend using proper geospatial packages
    > to build custom geospatial graph viz,
    > such as [`pysal`](http://pysal.org/).)
    >
    > That said, `nxviz` can probably do what you need
    > for a quick-and-dirty view of the data.
    """
    )
    return


@app.cell
def _(G_filtered):
    import nxviz as nv
    import matplotlib.pyplot as plt

    c = nv.geo(G_filtered, node_color_by="dpcapacity")
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    Does that look familiar to you? Looks quite a bit like Chicago, I'd say :)

    Jesting aside, this visualization does help illustrate
    that the majority of trips occur between stations that are
    near the city center.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Pickling Graphs

    Since NetworkX graphs are Python objects,
    the canonical way to save them is by pickling them.

    Here's an example in action:
    """
    )
    return


@app.cell
def _(G):
    import pickle

    with open("/tmp/divvy.pkl", "wb") as _f:
        pickle.dump(G, _f, pickle.HIGHEST_PROTOCOL)
    return (pickle,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""And just to show that it can be loaded back into memory:""")
    return


@app.cell
def _(pickle):
    with open("/tmp/divvy.pkl", "rb") as _f:
        G_loaded = pickle.load(_f)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ### Exercise: checking graph integrity

    If you get a graph dataset as a pickle,
    you should always check it against reference properties
    to make sure of its data integrity.

    > Write a function that tests that the graph
    > has the correct number of nodes and edges inside it.
    """
    )
    return


@app.cell
def _(G):
    def test_graph_integrity(G):
        """Test integrity of raw Divvy graph."""
        # Your solution here
        pass

    from nams.solutions.io import test_graph_integrity

    test_graph_integrity(G)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Other text formats

    CSV files and `pandas` DataFrames
    give us a convenient way to store graph data,
    and if possible, do insist with your data collaborators
    that they provide you with graph data that are in this format.
    If they don't, however, no sweat!
    After all, Python is super versatile.

    In this ebook, we have loaded data in
    from non-CSV sources,
    sometimes by parsing text files raw,
    sometimes by treating special characters as delimiters in a CSV-like file,
    and sometimes by resorting to parsing JSON.

    You can see other examples of how we load data
    by browsing through the source file of `load_data.py`
    and studying how we construct graph objects.
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Solutions

    The solutions to this chapter's exercises are below
    """
    )
    return


@app.cell
def _():
    from nams.solutions import io
    import inspect

    print(inspect.getsource(io))
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


if __name__ == "__main__":
    app.run()
