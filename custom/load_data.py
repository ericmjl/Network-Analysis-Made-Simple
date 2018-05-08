import gzip
import json

import networkx as nx
import pandas as pd
from tqdm import tqdm


def load_seventh_grader_network():
    # Read the edge list
    df = pd.read_csv('datasets/moreno_seventh/out.moreno_seventh_seventh',
                     skiprows=2, header=None, sep=' ')
    df.columns = ['student1', 'student2', 'count']

    # Read the node metadata
    meta = pd.read_csv(
        'datasets/moreno_seventh/ent.moreno_seventh_seventh.student.gender',
        header=None)
    meta.index += 1
    meta.columns = ['gender']

    # Construct graph from edge list.
    G = nx.DiGraph()
    for row in df.iterrows():
        G.add_edge(row[1]['student1'], row[1]['student2'],
                   count=row[1]['count'])
    # Add node metadata
    for n in G.nodes():
        G.node[n]['gender'] = meta.ix[n]['gender']
    return G


def load_facebook_network():
    # Read the edge list

    df = pd.read_csv('datasets/ego-facebook/out.ego-facebook',
                     sep=' ', skiprows=2, header=None)
    df = df[[0, 1]]
    df.columns = ['user1', 'user2']

    G = nx.DiGraph()
    for row in df.iterrows():
        G.add_edge(row[1]['user1'], row[1]['user2'])

    return G


def load_sociopatterns_network():
    # Read the edge list

    df = pd.read_csv(
        'datasets/sociopatterns-infectious/out.sociopatterns-infectious',
        sep=' ', skiprows=2, header=None)
    df = df[[0, 1, 2]]
    df.columns = ['person1', 'person2', 'weight']

    G = nx.Graph()
    for row in df.iterrows():
        p1 = row[1]['person1']
        p2 = row[1]['person2']
        if G.has_edge(p1, p2):
            G.edges[p1, p2]['weight'] += 1
        else:
            G.add_edge(p1, p2, weight=1)

    for n in sorted(G.nodes()):
        G.node[n]['order'] = float(n)

    return G


def load_physicians_network():
    # Read the edge list

    df = pd.read_csv(
        'datasets/moreno_innovation/out.moreno_innovation_innovation',
        sep=' ', skiprows=2, header=None)
    df = df[[0, 1]]
    df.columns = ['doctor1', 'doctor2']

    G = nx.Graph()
    for row in df.iterrows():
        G.add_edge(row[1]['doctor1'], row[1]['doctor2'])

    return G


def load_propro_network():
    propro = pd.read_csv('datasets/moreno_propro/out.moreno_propro_propro.txt', skiprows=2, header=None, delimiter=' ')
    propro.columns = ['prot1_id', 'prot2_id']
    G = nx.Graph()
    G.add_edges_from(zip(propro['prot1_id'], propro['prot2_id']))

    return G


def load_crime_network():
    df = pd.read_csv('datasets/moreno_crime/out.moreno_crime_crime',
                     sep=' ', skiprows=2, header=None)
    df = df[[0, 1]]
    df.columns = ['personID', 'crimeID']
    df.index += 1

    # Read in the role metadata
    roles = pd.read_csv(
        'datasets/moreno_crime/rel.moreno_crime_crime.person.role',
        header=None)
    roles.columns = ['roles']
    roles.index += 1

    # Add the edge data to the graph.
    G = nx.Graph()
    for r, d in df.join(roles).iterrows():
        pid = 'p{0}'.format(d['personID'])  # pid stands for "Person I.D."
        cid = 'c{0}'.format(d['crimeID'])  # cid stands for "Crime I.D."
        G.add_node(pid, bipartite='person')
        G.add_node(cid, bipartite='crime')
        G.add_edge(pid, cid, role=d['roles'])

    # Read in the gender metadata
    gender = pd.read_csv(
        'datasets/moreno_crime/ent.moreno_crime_crime.person.sex', header=None)
    gender.index += 1
    for n, gender_code in gender.iterrows():
        nodeid = 'p{0}'.format(n)
        G.node[nodeid]['gender'] = gender_code[0]

    return G


def load_university_social_network():
    G = nx.read_edgelist('datasets/moreno_oz/out.moreno_oz_oz',
                         comments='%',
                         delimiter=' ',
                         data=[('rating', int)],
                         create_using=nx.DiGraph(),
                         nodetype=int)
    return G


def load_amazon_reviews():
    # Read raw data.
    data = []
    with gzip.open('datasets/amazon_reviews/reviews_Digital_Music_5.json.gz', 'rt') as f:
        for line in tqdm(f.readlines()):
            # Clean data
            line = line.strip('\n')
            # Parse with JSON
            j = json.loads(line)
            data.append(j)

    # Add nodes
    G = nx.Graph()  # noqa: N806
    for d in tqdm(data):
        G.add_node(d['asin'], bipartite='product')
        G.add_node(d['reviewerID'], bipartite='customer')

    # Add edges
    for d in tqdm(data):
        G.add_edge(d['reviewerID'], d['asin'])

    return G
