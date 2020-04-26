def rank_ordered_neighbors(G):
	"""
	Uses a pandas Series to help with sorting.
	"""
	import pandas as pd
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
