def adjacency_matrix_power():
    ans = """
1. The diagonals equal to the degree of each node.
1. The off-diagonals also contain values,
which correspond to the number of paths that exist of length 2
between the node on the row axis and the node on the column axis.

In fact, the diagonal also takes on the same meaning!

For the terminal nodes, there is only 1 path
from itself back to itself,
while for the middle nodes, there are 2 paths
from itself back to itself!
"""
    return ans
