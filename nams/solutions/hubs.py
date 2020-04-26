import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from nxviz import CircosPlot

from nams import ecdf


def rank_ordered_neighbors(G):
    """
    Uses a pandas Series to help with sorting.
    """
    s = pd.Series({n: len(list(G.neighbors(n))) for n in G.nodes()})
    return s.sort_values(ascending=False)


def rank_ordered_neighbors_original(G):
    return sorted(
        G.nodes(), key=lambda x: len(list(G.neighbors(x))), reverse=True
    )


def rank_ordered_neighbors_generator(G):
    """
    Contributed by @dgerlanc.

    Ref: https://github.com/ericmjl/Network-Analysis-Made-Simple/issues/75
    """
    gen = ((len(list(G.neighbors(x))), x) for x in G.nodes())
    return sorted(gen, reverse=True)


def ecdf_degree_centrality(G):
    x, y = ecdf(list(nx.degree_centrality(G).values()))
    plt.scatter(x, y)
    plt.xlabel("degree centrality")
    plt.ylabel("cumulative fraction")


def ecdf_degree(G):
    num_neighbors = [len(list(G.neighbors(n))) for n in G.nodes()]
    x, y = ecdf(num_neighbors)
    plt.scatter(x, y)
    plt.xlabel("degree")
    plt.ylabel("cumulative fraction")


def num_possible_neighbors():
    return r"""
The number of possible neighbors can either be defined as:

1. All other nodes but myself
2. All other nodes and myself

If $K$ is the number of nodes in the graph,
then if defined as (1), $N$ (the denominator) is $K - 1$.
If defined as (2), $N$ is equal to $K$.
"""


def circos_plot(G):
    c = CircosPlot(G, node_order="order", node_color="order")
    c.draw()


def visual_insights():
    return """
We see that most edges are "local" with nodes
that are proximal in order.
The nodes that are weird are the ones that have connections
with individuals much later than itself,
crossing larger jumps in order/time.

Additionally, if you recall the ranked list of degree centralities,
it appears that these nodes that have the highest degree centrality scores
are also the ones that have edges that cross the circos plot.
"""


def dc_node_order(G):
    import matplotlib.pyplot as plt
    import pandas as pd
    import networkx as nx

    # Degree centralities
    dcs = pd.Series(nx.degree_centrality(G))

    # Maximum node order difference
    maxdiffs = dict()
    for n, d in G.nodes(data=True):
        diffs = []
        for nbr in G.neighbors(n):
            diffs.append(abs(G.nodes[nbr]["order"] - d["order"]))
        maxdiffs[n] = max(diffs)
    maxdiffs = pd.Series(maxdiffs)

    ax = pd.DataFrame(dict(degree_centrality=dcs, max_diff=maxdiffs)).plot(
        x="degree_centrality", y="max_diff", kind="scatter"
    )
