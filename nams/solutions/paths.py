"""Solutions to Paths chapter."""

import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import seaborn as sns
from nams.functions import render_html


def bfs_algorithm():
    """
    How to design a BFS algorithm.
    """
    ans = """
How does the breadth-first search work?
It essentially is as follows:

1. Begin with a queue that has only one element in it: the starting node.
2. Add the neighbors of that node to the queue.
    1. If destination node is present in the queue, end.
    2. If destination node is not present, proceed.
3. For each node in the queue:
    1. Remove node from the queue.
    2. Add neighbors of the node to the queue. Check if destination node is present or not.
    3. If destination node is present, end. <!--Credit: @cavaunpeu for finding bug in pseudocode.-->
    4. If destination node is not present, continue.
"""
    return render_html(ans)


def path_exists(node1, node2, G):
    """
    This function checks whether a path exists between two nodes (node1,
    node2) in graph G.
    """

    visited_nodes = set()
    queue = [node1]

    while len(queue) > 0:
        node = queue.pop()
        neighbors = list(G.neighbors(node))
        if node2 in neighbors:
            return True
        else:
            visited_nodes.add(node)
            nbrs = [n for n in neighbors if n not in visited_nodes]
            queue = nbrs + queue

    return False


def path_exists_for_loop(node1, node2, G):
    """
    This function checks whether a path exists between two nodes (node1,
    node2) in graph G.

    Special thanks to @ghirlekar for suggesting that we keep track of the
    "visited nodes" to prevent infinite loops from happening. This also
    removes the need to remove nodes from queue.

    Reference: https://github.com/ericmjl/Network-Analysis-Made-Simple/issues/3

    With thanks to @joshporter1 for the second bug fix. Originally there was
    an extraneous "if" statement that guaranteed that the "False" case would
    never be returned - because queue never changes in shape. Discovered at
    PyCon 2017.

    With thanks to @chendaniely for pointing out the extraneous "break".

    If you would like to see @dgerlanc's implementation, see
    https://github.com/ericmjl/Network-Analysis-Made-Simple/issues/76
    """
    visited_nodes = set()
    queue = [node1]

    for node in queue:
        neighbors = list(G.neighbors(node))
        if node2 in neighbors:
            return True
        else:
            visited_nodes.add(node)
            queue.extend([n for n in neighbors if n not in visited_nodes])

    return False


def path_exists_deque(node1, node2, G):
    """An alternative implementation."""
    from collections import deque

    visited_nodes = set()
    queue = deque([node1])

    while len(queue) > 0:
        node = queue.popleft()
        neighbors = list(G.neighbors(node))
        if node2 in neighbors:
            return True
        else:
            visited_nodes.add(node)
            queue.extend([n for n in neighbors if n not in visited_nodes])

    return False


def plot_path_with_neighbors(G, n1, n2):
    """Plot path while also including neighbors of nodes along path."""
    path = nx.shortest_path(G, n1, n2)

    nodes = [*path]
    for node in path:
        nodes.extend(list(G.neighbors(node)))
    nodes = list(set(nodes))

    colors = []
    for n in nodes:
        if n not in path:
            colors.append("blue")
        else:
            colors.append("red")

    nx.draw(G.subgraph(nodes), with_labels=False, node_color=colors)


def plot_degree_betweenness(G):
    """Plot scatterplot between degree and betweenness centrality."""
    bc = pd.Series(nx.betweenness_centrality(G))
    dc = pd.Series(nx.degree_centrality(G))

    df = pd.DataFrame(dict(bc=bc, dc=dc))
    ax = df.plot(x="dc", y="bc", kind="scatter")
    ax.set_ylabel("Betweenness\nCentrality")
    ax.set_xlabel("Degree Centrality")
    sns.despine()
