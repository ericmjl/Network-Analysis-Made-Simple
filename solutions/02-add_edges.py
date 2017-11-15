G.add_node(30, gender='male')
G.add_node(31, gender='female')
G.add_edge(30, 31, count=3)
G.add_edge(31, 30, count=3)  # reverse is optional in undirected network
G.add_edge(30, 7, count=3)   # but this network is directed
G.add_edge(7, 30, count=3)
G.add_edge(31, 7, count=3)
G.add_edge(7, 31, count=3)
