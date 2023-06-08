# Bipartite Graphs

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

YouTubeVideo(id="BYOK12I9vgI", width="100%")


```





<iframe
    width="100%"
    height="300"
    src="https://www.youtube.com/embed/BYOK12I9vgI"
    frameborder="0"
    allowfullscreen

></iframe>




In this chapter, we will look at bipartite graphs and their applications.

## What are bipartite graphs?

As the name suggests,
bipartite have two (bi) node partitions (partite).
In other words, we can assign nodes to one of the two partitions.
(By contrast, all of the graphs that we have seen before are _unipartite_:
they only have a single partition.)

### Rules for bipartite graphs

With unipartite graphs, you might remember a few rules that apply.

Firstly, nodes and edges belong to a _set_.
This means the node set contains only unique members,
i.e. no node can be duplicated.
The same applies for the edge set.

On top of those two basic rules, bipartite graphs add an additional rule:
Edges can only occur between nodes of **different** partitions.
In other words, nodes within the same partition 
are not allowed to be connected to one another.

### Applications of bipartite graphs

Where do we see bipartite graphs being used?
Here's one that is very relevant to e-commerce,
which touches our daily lives:

> We can model customer purchases of products using a bipartite graph.
> Here, the two node sets are **customer** nodes and **product** nodes,
> and edges indicate that a customer {$$}C{/$$} purchased a product {$$}P{/$$}.

On the basis of this graph, we can do interesting analyses,
such as finding customers that are similar to one another
on the basis of their shared product purchases.

Can you think of other situations
where a bipartite graph model can be useful?

## Dataset

Here's another application in crime analysis,
which is relevant to the example that we will use in this chapter:

> This bipartite network contains persons
> who appeared in at least one crime case 
> as either a suspect, a victim, a witness 
> or both a suspect and victim at the same time. 
> A left node represents a person and a right node represents a crime. 
> An edge between two nodes shows that 
> the left node was involved in the crime 
> represented by the right node.

This crime dataset was also sourced from Konect.




```python
from nams import load_data as cf
G = cf.load_crime_network()
for n, d in G.nodes(data=True):
    G.nodes[n]["degree"] = G.degree(n)


```

If you inspect the nodes,
you will see that they contain a special metadata keyword: `bipartite`.
This is a special keyword that NetworkX can use 
to identify nodes of a given partition.



### Visualize the crime network

To help us get our bearings right, let's visualize the crime network.




```python
import nxviz as nv
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(7, 7))
nv.circos(G, sort_by="degree", group_by="bipartite", node_color_by="bipartite", node_enc_kwargs={"size_scale": 3})


```




    <Axes: >




    
![png](images/04-advanced_01-bipartite_md_7_1.png)
    


### Exercise: Extract each node set

A useful thing to be able to do
is to extract each partition's node set.
This will become handy when interacting with
NetworkX's bipartite algorithms later on.

> Write a function that extracts all of the nodes 
> from specified node partition.
> It should also raise a plain Exception
> if no nodes exist in that specified partition.
> (as a precuation against users putting in invalid partition names).




```python
import networkx as nx

def extract_partition_nodes(G: nx.Graph, partition: str):
    nodeset = [_ for _, _ in _______ if ____________]
    if _____________:
        raise Exception(f"No nodes exist in the partition {partition}!")
    return nodeset

from nams.solutions.bipartite import extract_partition_nodes
# Uncomment the next line to see the answer.
# extract_partition_nodes??


```

## Bipartite Graph Projections

In a bipartite graph, one task that can be useful to do
is to calculate the projection of a graph onto one of its nodes.

What do we mean by the "projection of a graph"?
It is best visualized using this figure:




```python
from nams.solutions.bipartite import draw_bipartite_graph_example, bipartite_example_graph
from nxviz import annotate
import matplotlib.pyplot as plt

bG = bipartite_example_graph()
pG = nx.bipartite.projection.projected_graph(bG, "abcd")
ax = draw_bipartite_graph_example()
plt.sca(ax[0])
annotate.parallel_labels(bG, group_by="bipartite")
plt.sca(ax[1])
annotate.arc_labels(pG)


```


    
![png](images/04-advanced_01-bipartite_md_11_0.png)
    


As shown in the figure above, we start first with a bipartite graph with two node sets,
the "alphabet" set and the "numeric" set.
The projection of this bipartite graph onto the "alphabet" node set
is a graph that is constructed such that it only contains the "alphabet" nodes,
and edges join the "alphabet" nodes because they share a connection to a "numeric" node.
The red edge on the right
is basically the red path traced on the left.



### Computing graph projections

How does one compute graph projections using NetworkX?
Turns out, NetworkX has a `bipartite` submodule,
which gives us all of the facilities that we need
to interact with bipartite algorithms.

First of all, we need to check that the graph
is indeed a bipartite graph.
NetworkX provides a function for us to do so:




```python
from networkx.algorithms import bipartite

bipartite.is_bipartite(G)


```




    True



Now that we've confirmed that the graph is indeed bipartite,
we can use the NetworkX bipartite submodule functions
to generate the bipartite projection onto one of the node partitions.

First off, we need to extract nodes from a particular partition.




```python
person_nodes = extract_partition_nodes(G, "person")
crime_nodes = extract_partition_nodes(G, "crime")


```

Next, we can compute the projection:




```python
person_graph = bipartite.projected_graph(G, person_nodes)
crime_graph = bipartite.projected_graph(G, crime_nodes)


```

And with that, we have our projected graphs!

Go ahead and inspect them:




```python
list(person_graph.edges(data=True))[0:5]


```




    [('p1', 'p336', {}),
     ('p1', 'p756', {}),
     ('p1', 'p694', {}),
     ('p1', 'p93', {}),
     ('p2', 'p287', {})]




```python
list(crime_graph.edges(data=True))[0:5]


```




    [('c1', 'c3', {}),
     ('c1', 'c4', {}),
     ('c1', 'c2', {}),
     ('c2', 'c3', {}),
     ('c2', 'c4', {})]



Now, what is the _interpretation_ of these projected graphs?

- For `person_graph`, we have found _individuals who are linked by shared participation (whether witness or suspect) in a crime._
- For `crime_graph`, we have found _crimes that are linked by shared involvement by people._

Just by this graph, we already can find out pretty useful information.
Let's use an exercise that leverages what you already know
to extract useful information from the projected graph.



### Exercise: find the crime(s) that have the most shared connections with other crimes

> Find crimes that are most similar to one another
> on the basis of the number of shared connections to individuals.

_Hint: This is a degree centrality problem!_




```python
import pandas as pd

def find_most_similar_crimes(cG: nx.Graph):
    """
    Find the crimes that are most similar to other crimes.
    """
    dcs = ______________
    return ___________________


from nams.solutions.bipartite import find_most_similar_crimes
find_most_similar_crimes(crime_graph)


```




    c110    0.136364
    c47     0.070909
    c23     0.070909
    c95     0.063636
    c14     0.061818
    c352    0.060000
    c432    0.060000
    c160    0.058182
    c417    0.058182
    c525    0.058182
    dtype: float64



### Exercise: find the individual(s) that have the most shared connections with other individuals

> Now do the analogous thing for individuals!




```python
def find_most_similar_people(pG: nx.Graph):
    """
    Find the persons that are most similar to other persons.
    """
    dcs = ______________
    return ___________________


from nams.solutions.bipartite import find_most_similar_people
find_most_similar_people(person_graph)


```




    p425    0.061594
    p2      0.057971
    p356    0.053140
    p56     0.039855
    p695    0.039855
    p497    0.036232
    p715    0.035024
    p10     0.033816
    p815    0.032609
    p74     0.030193
    dtype: float64



## Weighted Projection

Though we were able to find out which graphs were connected with one another,
we did not record in the resulting projected graph
the **strength** by which the two nodes were connected.
To preserve this information, we need another function:




```python
weighted_person_graph = bipartite.weighted_projected_graph(G, person_nodes)
list(weighted_person_graph.edges(data=True))[0:5]


```




    [('p1', 'p336', {'weight': 1}),
     ('p1', 'p756', {'weight': 1}),
     ('p1', 'p694', {'weight': 1}),
     ('p1', 'p93', {'weight': 1}),
     ('p2', 'p287', {'weight': 1})]



### Exercise: Find the people that can help with investigating a `crime`'s `person`.

Let's pretend that we are a detective trying to solve a crime,
and that we right now need to find other individuals
who were not implicated in the same _exact_ crime as an individual was,
but who might be able to give us information about that individual
because they were implicated in other crimes with that individual.

> Implement a function that takes in a bipartite graph `G`, a string `person` and a string `crime`,
> and returns a list of other `person`s that were **not** implicated in the `crime`,
> but were connected to the `person` via other crimes.
> It should return a _ranked list_,
> based on the **number of shared crimes** (from highest to lowest)
> because the ranking will help with triage.




```python
list(G.neighbors('p1'))


```




    ['c1', 'c2', 'c3', 'c4']




```python
def find_connected_persons(G, person, crime):
    # Step 0: Check that the given "person" and "crime" are connected.
    if _____________________________:
        raise ValueError(f"Graph does not have a connection between {person} and {crime}!")

    # Step 1: calculate weighted projection for person nodes.
    person_nodes = ____________________________________
    person_graph = bipartite.________________________(_, ____________)
    
    # Step 2: Find neighbors of the given `person` node in projected graph.
    candidate_neighbors = ___________________________________
    
    # Step 3: Remove candidate neighbors from the set if they are implicated in the given crime.
    for p in G.neighbors(crime):
        if ________________________:
            _____________________________
    
    # Step 4: Rank-order the candidate neighbors by number of shared connections.
    _________ = []
    ## You might need a for-loop here
    return pd.DataFrame(__________).sort_values("________", ascending=False)


from nams.solutions.bipartite import find_connected_persons
print(find_connected_persons(G, 'p2', 'c10').to_markdown())


```

|| node   |   weight |
|---:|:-------|---------:|
|  7 | p67|        4 |
| 30 | p356   |        2 |
| 41 | p338   |        2 |
| 17 | p361   |        2 |
|  0 | p287   |        1 |
| 35 | p690   |        1 |
| 27 | p768   |        1 |
| 28 | p475   |        1 |
| 29 | p608   |        1 |
| 31 | p223   |        1 |
| 32 | p439   |        1 |
| 33 | p660   |        1 |
| 34 | p528   |        1 |
| 36 | p39|        1 |
| 25 | p710   |        1 |
| 37 | p186   |        1 |
| 38 | p661   |        1 |
| 39 | p471   |        1 |
| 40 | p211   |        1 |
| 42 | p4 |        1 |
| 43 | p320   |        1 |
| 44 | p5 |        1 |
| 45 | p578   |        1 |
| 26 | p48|        1 |
| 23 | p305   |        1 |
| 24 | p563   |        1 |
|  1 | p620   |        1 |
|  2 | p665   |        1 |
|  3 | p495   |        1 |
|  4 | p90|        1 |
|  5 | p309   |        1 |
|  6 | p773   |        1 |
|  8 | p499   |        1 |
|  9 | p498   |        1 |
| 10 | p300   |        1 |
| 11 | p360   |        1 |
| 12 | p806   |        1 |
| 13 | p603   |        1 |
| 14 | p449   |        1 |
| 15 | p782   |        1 |
| 16 | p304   |        1 |
| 18 | p820   |        1 |
| 19 | p286   |        1 |
| 20 | p587   |        1 |
| 21 | p401   |        1 |
| 22 | p781   |        1 |
| 46 | p716   |        1 |


## Degree Centrality

The degree centrality metric is something we can calculate for bipartite graphs.
Recall that the degree centrality metric is the number of neighbors of a node
divided by the total number of _possible_ neighbors.

In a unipartite graph, the denominator can be the total number of nodes less one
(if self-loops are not allowed)
or simply the total number of nodes (if self loops _are_ allowed).

### Exercise: What is the denominator for bipartite graphs?

Think about it for a moment, then write down your answer.




```python
from nams.solutions.bipartite import bipartite_degree_centrality_denominator
from nams.functions import render_html
bipartite_degree_centrality_denominator()


```




    '\nThe total number of neighbors that a node can _possibly_ have\nis the number of nodes in the other partition.\nThis comes naturally from the definition of a bipartite graph,\nwhere nodes can _only_ be connected to nodes in the other partition.\n'



### Exercise: Which `persons` are implicated in the most number of crimes?

> Find the `persons` (singular or plural) who are connected to the most number of crimes.

To do so, you will need to use `nx.bipartite.degree_centrality`,
rather than the regular `nx.degree_centrality` function.

`nx.bipartite.degree_centrality` requires that you pass in
a node set from one of the partitions
so that it can correctly partition nodes on the other set.
What is returned, though, is the degree centrality
for nodes in both sets.
Here is an example to show you how the function is used:

```python
dcs = nx.bipartite.degree_centrality(my_graph, nodes_from_one_partition)
```




```python
def find_most_crime_person(G, person_nodes):
    dcs = __________________________
    return ___________________________

from nams.solutions.bipartite import find_most_crime_person
find_most_crime_person(G, person_nodes)


```




    'p815'



## Solutions

Here are the solutions to the exercises above.




```python
from nams.solutions import bipartite
import inspect

print(inspect.getsource(bipartite))


```

    import networkx as nx
    import pandas as pd
    from nams.functions import render_html
    
    
    def extract_partition_nodes(G: nx.Graph, partition: str):
        nodeset = [n for n, d in G.nodes(data=True) if d["bipartite"] == partition]
        if len(nodeset) == 0:
            raise Exception(f"No nodes exist in the partition {partition}!")
        return nodeset
    
    
    def bipartite_example_graph():
        bG = nx.Graph()
        bG.add_nodes_from("abcd", bipartite="letters")
        bG.add_nodes_from(range(1, 4), bipartite="numbers")
        bG.add_edges_from([("a", 1), ("b", 1), ("b", 3), ("c", 2), ("c", 3), ("d", 1)])
    
        return bG
    
    
    def draw_bipartite_graph_example():
        """Draw an example bipartite graph and its corresponding projection."""
        import matplotlib.pyplot as plt
        import nxviz as nv
        from nxviz import annotate, plots, highlights
    
        fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 4))
        plt.sca(ax[0])
        bG = bipartite_example_graph()
        nv.parallel(bG, group_by="bipartite", node_color_by="bipartite")
        annotate.parallel_group(bG, group_by="bipartite", y_offset=-0.5)
        highlights.parallel_edge(bG, "a", 1, group_by="bipartite")
        highlights.parallel_edge(bG, "b", 1, group_by="bipartite")
    
        pG = nx.bipartite.projected_graph(bG, nodes=list("abcd"))
        plt.sca(ax[1])
        nv.arc(pG)
        highlights.arc_edge(pG, "a", "b")
        return ax
    
    
    def find_most_similar_crimes(cG: nx.Graph):
        """
        Find the crimes that are most similar to other crimes.
        """
        dcs = pd.Series(nx.degree_centrality(cG))
        return dcs.sort_values(ascending=False).head(10)
    
    
    def find_most_similar_people(pG: nx.Graph):
        """
        Find the persons that are most similar to other persons.
        """
        dcs = pd.Series(nx.degree_centrality(pG))
        return dcs.sort_values(ascending=False).head(10)
    
    
    def find_connected_persons(G, person, crime):
        """Answer to exercise on people implicated in crimes"""
        # Step 0: Check that the given "person" and "crime" are connected.
        if not G.has_edge(person, crime):
            raise ValueError(
                f"Graph does not have a connection between {person} and {crime}!"
            )
    
        # Step 1: calculate weighted projection for person nodes.
        person_nodes = extract_partition_nodes(G, "person")
        person_graph = nx.bipartite.weighted_projected_graph(G, person_nodes)
    
        # Step 2: Find neighbors of the given `person` node in projected graph.
        candidate_neighbors = set(person_graph.neighbors(person))
    
        # Step 3: Remove candidate neighbors from the set if they are implicated in the given crime.
        for p in G.neighbors(crime):
            if p in candidate_neighbors:
                candidate_neighbors.remove(p)
    
        # Step 4: Rank-order the candidate neighbors by number of shared connections.
        data = []
        for nbr in candidate_neighbors:
            data.append(dict(node=nbr, weight=person_graph.edges[person, nbr]["weight"]))
        return pd.DataFrame(data).sort_values("weight", ascending=False)
    
    
    def bipartite_degree_centrality_denominator():
        """Answer to bipartite graph denominator for degree centrality."""
    
        ans = """
    The total number of neighbors that a node can _possibly_ have
    is the number of nodes in the other partition.
    This comes naturally from the definition of a bipartite graph,
    where nodes can _only_ be connected to nodes in the other partition.
    """
        return ans
    
    
    def find_most_crime_person(G, person_nodes):
        dcs = (
            pd.Series(nx.bipartite.degree_centrality(G, person_nodes))
            .sort_values(ascending=False)
            .to_frame()
        )
        return dcs.reset_index().query("index.str.contains('p')").iloc[0]["index"]
    



```python



```
