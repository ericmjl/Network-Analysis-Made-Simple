import pandas as pd
import networkx as nx

def weighted_degree(G, weight):
    result = dict()
    for node in G.nodes():
        weight_degree = 0
        for n in G.edges([node], data=True):
            weight_degree += n[2]['weight']
        result[node] = weight_degree
    return result

def correlation_centrality(G):
    cor = pd.DataFrame.from_records([nx.pagerank_numpy(G, weight='weight'),
                                 nx.betweenness_centrality(G, weight='weight_inv'),
                                 weighted_degree(G, 'weight'),
                                 nx.degree_centrality(G)])
    return cor.T.corr()

def evol_betweenness(graphs):
    evol = [nx.betweenness_centrality(graph, weight='weight_inv') for graph in graphs]
    evol_df = pd.DataFrame.from_records(evol).fillna(0)

    set_of_char = set()
    for i in range(5):
        set_of_char |= set(list(evol_df.T[i].sort_values(ascending=False)[0:5].index))


    evol_df[list(set_of_char)].plot(figsize=(19,10))

def most_important_node_in_partition(graph, partition_dict):
    max_d = {}
    deg = nx.degree_centrality(graph)
    for group in partition_dict:
        temp = 0
        for character in partition_dict[group]:
            if deg[character] > temp:
                max_d[group] = character
                temp = deg[character]
    return max_d