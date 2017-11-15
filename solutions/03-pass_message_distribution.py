# Possible answer to Question 2:
# We need to know the length of every single shortest path between every pair of nodes.
# If we don't put a source and target into the nx.shortest_path_length(G) function call, then
# we get a dictionary of dictionaries, where all source-->target-->lengths are shown.

lengths = []
times = []
for source, sink_length in nx.shortest_path_length(G).items():
    for sink, length in sink_length.items():
        times.append(sum(range(1, length+1)))
        lengths.append(length)

plt.figure(0)
plt.bar(list(Counter(lengths).keys()), list(Counter(lengths).values()))

plt.figure(1)
plt.bar(list(Counter(times).keys()), list(Counter(times).values()))
