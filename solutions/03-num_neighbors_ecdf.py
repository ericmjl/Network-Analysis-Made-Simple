fig = plt.figure(1)
neighbors = [len(G.neighbors(node)) for node in G.nodes()]
x, y = ecdf(neighbors)
plt.scatter(x, y)
plt.title('Number of Neighbors')
