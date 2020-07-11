import networkx as nx
import pandas as pd

def busiest_route(pass_air_data, year):
    return pass_air_data[pass_air_data.groupby(
        ['YEAR'])['PASSENGERS'].transform(max) == pass_air_data['PASSENGERS']
                        ].query(f'YEAR == {year}')

def plot_time_series(pass_air_data, origin, dest):
    pass_air_data.query(f"ORIGIN == '{origin}' and DEST == '{dest}'").plot('YEAR', 'PASSENGERS')

def add_opinated_edges(G):
    G = nx.DiGraph(G)
    sort_degree = sorted(nx.degree_centrality(G).items(), key=lambda x:x[1], reverse=True)
    top_count = 0
    for n, v in sort_degree:
        count = 0
        for node, val in sort_degree:
            if node != n:
                if node not in G._adj[n]:
                    G.add_edge(n, node)
                    count += 1
                    if count == 25:
                        break
        top_count += 1
        if top_count == 20:
            break
    return G