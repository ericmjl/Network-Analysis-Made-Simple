# Possible Answers:
fig = plt.figure(0)
# Get a list of degree centrality scores for all of the
# nodes in the graph
degree_centralities = list(
    nx.degree_centrality(G).values())
x, y = ecdf(degree_centralities)
# Plot the histogram of degree centralities.
plt.scatter(x, y)
# Set the plot title.
plt.title('Degree Centralities')
