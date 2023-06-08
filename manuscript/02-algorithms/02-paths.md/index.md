# Paths

```python
%load_ext autoreload
%autoreload 2
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
import warnings
warnings.filterwarnings('ignore')


```

## Introduction




```python
from IPython.display import YouTubeVideo

YouTubeVideo(id="JjpbztqP9_0", width="100%")


```





<iframe
    width="100%"
    height="300"
    src="https://www.youtube.com/embed/JjpbztqP9_0"
    frameborder="0"
    allowfullscreen

></iframe>




Graph traversal is akin to walking along the graph, node by node,
constrained by the edges that connect the nodes.
Graph traversal is particularly useful for understanding 
the local structure of certain portions of the graph
and for finding paths that connect two nodes in the network.

In this chapter, we are going to learn how to perform pathfinding in a graph,
specifically by looking for _shortest paths_ via the _breadth-first search_ algorithm.



## Breadth-First Search

The BFS algorithm is a staple of computer science curricula,
and for good reason:
it teaches learners how to "think on" a graph,
putting one in the position of 
"the dumb computer" that can't use a visual cortex to 
"_just know_" how to trace a path from one node to another.
As a topic, learning how to do BFS
additionally imparts algorithmic thinking to the learner.

### Exercise: Design the algorithm

Try out this exercise to get some practice with algorithmic thinking.

> 1. On a piece of paper, conjure up a graph that has 15-20 nodes. Connect them any way you like.
> 1. Pick two nodes. Pretend that you're standing on one of the nodes, but you can't see any further beyond one neighbor away.
> 1. Work out how you can find _a_ path from the node you're standing on to the other node, given that you can _only_ see nodes that are one neighbor away but have an infinitely good memory.

If you are successful at designing the algorithm, you should get the answer below.




```python
from nams import load_data as cf
G = cf.load_sociopatterns_network()


```


```python
from nams.solutions.paths import bfs_algorithm

# UNCOMMENT NEXT LINE TO GET THE ANSWER.
# bfs_algorithm()


```

### Exercise: Implement the algorithm

> Now that you've seen how the algorithm works, try implementing it!




```python
# FILL IN THE BLANKS BELOW

def path_exists(node1, node2, G):
    """
    This function checks whether a path exists between two nodes (node1, 
    node2) in graph G.
    """
    visited_nodes = _____
    queue = [_____]
    
    while len(queue) > 0:
        node = ___________
        neighbors = list(_________________)
        if _____ in _________:
            # print('Path exists between nodes {0} and {1}'.format(node1, node2))
            return True
        else:
            visited_nodes.___(____)
            nbrs = [_ for _ in _________ if _ not in _____________]
            queue = ____ + _____
    
    # print('Path does not exist between nodes {0} and {1}'.format(node1, node2))
    return False



```


```python
# UNCOMMENT THE FOLLOWING TWO LINES TO SEE THE ANSWER
from nams.solutions.paths import path_exists
# path_exists??


```


```python
# CHECK YOUR ANSWER AGAINST THE TEST FUNCTION BELOW
from random import sample
import networkx as nx


def test_path_exists(N):
    """
    N: The number of times to spot-check.
    """
    for i in range(N):
        n1, n2 = sample(G.nodes(), 2)
        assert path_exists(n1, n2, G) == bool(nx.shortest_path(G, n1, n2))
    return True
    
assert test_path_exists(10)


```

## Visualizing Paths

One of the objectives of that exercise before was to help you "think on graphs".
Now that you've learned how to do so, you might be wondering,
"How do I visualize that path through the graph?"

Well first off, if you inspect the `test_path_exists` function above,
you'll notice that NetworkX provides a `shortest_path()` function
that you can use. Here's what using `nx.shortest_path()` looks like.




```python
path = nx.shortest_path(G, 7, 400)
path


```




    [7, 51, 188, 230, 335, 400]



As you can see, it returns the nodes along the shortest path,
incidentally in the exact order that you would traverse.

One thing to note, though!
If there are multiple shortest paths from one node to another,
NetworkX will only return one of them.

So how do you draw those nodes _only_?

You can use the `G.subgraph(nodes)`
to return a new graph that only has nodes in `nodes`
and only the edges that exist between them.
After that, you can use any plotting library you like.
We will show an example here that uses nxviz's matrix plot.

Let's see it in action:




```python
import nxviz as nv
g = G.subgraph(path)
nv.matrix(g, sort_by="order")


```




    <Axes: >




    
![png](images/02-algorithms_02-paths_md_14_1.png)
    


_Voila!_ Now we have the subgraph (1) extracted and (2) drawn to screen!
In this case, the matrix plot is a suitable visualization for its compactness.
The off-diagonals also show that each node is a neighbor to the next one.

You'll also notice that if you try to modify the graph `g`, say by adding a node:

```python
g.add_node(2048)
```

you will get an error:

```python
---------------------------------------------------------------------------
NetworkXError                             Traceback (most recent call last)
<ipython-input-10-ca6aa4c26819> in <module>
----> 1 g.add_node(2048)

~/anaconda/envs/nams/lib/python3.7/site-packages/networkx/classes/function.py in frozen(*args, **kwargs)
    156 def frozen(*args, **kwargs):
    157     """Dummy method for raising errors when trying to modify frozen graphs"""
--> 158     raise nx.NetworkXError("Frozen graph can't be modified")
    159 
    160 

NetworkXError: Frozen graph can't be modified
```

From the perspective of semantics, this makes a ton of sense:
the subgraph `g` is a perfect subset of the larger graph `G`,
and should not be allowed to be modified
unless the larger container graph is modified.



### Exercise: Draw path with neighbors one degree out

Try out this next exercise:

> Extend graph drawing with the neighbors of each of those nodes.
> Use any of the nxviz plots (`nv.matrix`, `nv.arc`, `nv.circos`);
> try to see which one helps you tell the best story.




```python
from nams.solutions.paths import plot_path_with_neighbors

### YOUR SOLUTION BELOW



```


```python
plot_path_with_neighbors(G, 7, 400)


```


    
![png](images/02-algorithms_02-paths_md_18_0.png)
    


In this case, we opted for an Arc plot because we only have one grouping of nodes but have a logical way to order them.
Because the path follows the order, the edges being highlighted automatically look like hops through the graph.



## Bottleneck nodes

We're now going to revisit the concept of an "important node",
this time now leveraging what we know about paths.

In the "hubs" chapter, we saw how a node that is "important"
could be so because it is connected to many other nodes.

Paths give us an alternative definition.
If we imagine that we have to pass a message on a graph
from one node to another,
then there may be "bottleneck" nodes
for which if they are removed,
then messages have a harder time flowing through the graph.

One metric that measures this form of importance
is the "betweenness centrality" metric.
On a graph through which a generic "message" is flowing,
a node with a high betweenness centrality
is one that has a high proportion of shortest paths
flowing through it.
In other words, it behaves like a _bottleneck_.



### Betweenness centrality in NetworkX

NetworkX provides a "betweenness centrality" function
that behaves consistently with the "degree centrality" function,
in that it returns a mapping from node to metric:




```python
import pandas as pd

pd.Series(nx.betweenness_centrality(G))


```




    100    0.014809
    101    0.001398
    102    0.000748
    103    0.006735
    104    0.001198
             ...   
    89     0.000004
    91     0.006415
    96     0.000323
    99     0.000322
    98     0.000000
    Length: 410, dtype: float64



### Exercise: compare degree and betweenness centrality

> Make a scatterplot of degree centrality on the x-axis
> and betweenness centrality on the y-axis.
> Do they correlate with one another?




```python
import matplotlib.pyplot as plt
import seaborn as sns

# YOUR ANSWER HERE:



```


```python
from nams.solutions.paths import plot_degree_betweenness
plot_degree_betweenness(G)


```


    
![png](images/02-algorithms_02-paths_md_25_0.png)
    


### Think about it...

...does it make sense that degree centrality and betweenness centrality
are not well-correlated?

Can you think of a scenario where a node has a
"high" betweenness centrality
but a "low" degree centrality?
Before peeking at the graph below,
think about your answer for a moment.




```python
nx.draw(nx.barbell_graph(5, 1))


```


    
![png](images/02-algorithms_02-paths_md_27_0.png)
    


## Recap

In this chapter, you learned the following things:

1. You figured out how to implement the breadth-first-search algorithm to find shortest paths.
1. You learned how to extract subgraphs from a larger graph.
1. You implemented visualizations of subgraphs, which should help you as you communicate with colleagues.
1. You calculated betweenness centrality metrics for a graph, and visualized how they correlated with degree centrality.



## Solutions

Here are the solutions to the exercises above.




```python
from nams.solutions import paths
import inspect

print(inspect.getsource(paths))


```

    """Solutions to Paths chapter."""
    
    import matplotlib.pyplot as plt
    import networkx as nx
    import pandas as pd
    import seaborn as sns
    from nams.functions import render_html
    
    
    def bfs_algorithm():
        """
        How to design a BFS algorithm.
        """
        ans = """
    How does the breadth-first search work?
    It essentially is as follows:
    
    1. Begin with a queue that has only one element in it: the starting node.
    2. Add the neighbors of that node to the queue.
        1. If destination node is present in the queue, end.
        2. If destination node is not present, proceed.
    3. For each node in the queue:
        1. Remove node from the queue.
        2. Add neighbors of the node to the queue. Check if destination node is present or not.
        3. If destination node is present, end. <!--Credit: @cavaunpeu for finding bug in pseudocode.-->
        4. If destination node is not present, continue.
    """
        return render_html(ans)
    
    
    def path_exists(node1, node2, G):
        """
        This function checks whether a path exists between two nodes (node1,
        node2) in graph G.
        """
    
        visited_nodes = set()
        queue = [node1]
    
        while len(queue) > 0:
            node = queue.pop()
            neighbors = list(G.neighbors(node))
            if node2 in neighbors:
                return True
            else:
                visited_nodes.add(node)
                nbrs = [n for n in neighbors if n not in visited_nodes]
                queue = nbrs + queue
    
        return False
    
    
    def path_exists_for_loop(node1, node2, G):
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
    
        If you would like to see @dgerlanc's implementation, see
        https://github.com/ericmjl/Network-Analysis-Made-Simple/issues/76
        """
        visited_nodes = set()
        queue = [node1]
    
        for node in queue:
            neighbors = list(G.neighbors(node))
            if node2 in neighbors:
                return True
            else:
                visited_nodes.add(node)
                queue.extend([n for n in neighbors if n not in visited_nodes])
    
        return False
    
    
    def path_exists_deque(node1, node2, G):
        """An alternative implementation."""
        from collections import deque
    
        visited_nodes = set()
        queue = deque([node1])
    
        while len(queue) > 0:
            node = queue.popleft()
            neighbors = list(G.neighbors(node))
            if node2 in neighbors:
                return True
            else:
                visited_nodes.add(node)
                queue.extend([n for n in neighbors if n not in visited_nodes])
    
        return False
    
    
    import nxviz as nv
    from nxviz import annotate, highlights
    
    
    def plot_path_with_neighbors(G, n1, n2):
        """Plot a path with the heighbors of of the nodes along that path."""
        path = nx.shortest_path(G, n1, n2)
        nodes = [*path]
        for node in path:
            nodes.extend(list(G.neighbors(node)))
        nodes = list(set(nodes))
    
        g = G.subgraph(nodes)
        nv.arc(
            g, sort_by="order", node_color_by="order", edge_enc_kwargs={"alpha_scale": 0.5}
        )
        for n in path:
            highlights.arc_node(g, n, sort_by="order")
        for n1, n2 in zip(path[:-1], path[1:]):
            highlights.arc_edge(g, n1, n2, sort_by="order")
    
    
    def plot_degree_betweenness(G):
        """Plot scatterplot between degree and betweenness centrality."""
        bc = pd.Series(nx.betweenness_centrality(G))
        dc = pd.Series(nx.degree_centrality(G))
    
        df = pd.DataFrame(dict(bc=bc, dc=dc))
        ax = df.plot(x="dc", y="bc", kind="scatter")
        ax.set_ylabel("Betweenness\nCentrality")
        ax.set_xlabel("Degree Centrality")
        sns.despine()
    

