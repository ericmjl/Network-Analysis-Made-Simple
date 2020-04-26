import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd

from nams import ecdf


def rank_ordered_neighbors(G):
	"""
	Uses a pandas Series to help with sorting.
	"""
	s = pd.Series(
			{
				n: len(list(G.neighbors(n)))
            	for n
            	in G.nodes()
        	}
    	)
	return s.sort_values(ascending=False)


def rank_ordered_neighbors_original(G):
	return sorted(G.nodes(),
       key=lambda x:len(list(G.neighbors(x))), reverse=True)


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
