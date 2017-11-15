# Possible answer to Question 1:
# All we need here is the length of the path.


def compute_transmission_time(G, source, target):
    """
    Fill in code below.
    """
    length = nx.shortest_path_length(G, source, target)

    time = sum(range(1, length+1))

    return time


compute_transmission_time(G, 14, 4)
