def path_exists(node1, node2, G):
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
    """
    visited_nodes = set()
    queue = [node1]

    for node in queue:
        neighbors = G.neighbors(node)
        if node2 in neighbors:
            print('Path exists between nodes {0} and {1}'.format(node1, node2))
            return True
        else:
            visited_nodes.add(node)
            queue.extend([n for n in neighbors if n not in visited_nodes])

    print('Path does not exist between nodes {0} and {1}'.format(node1, node2))
    return False
