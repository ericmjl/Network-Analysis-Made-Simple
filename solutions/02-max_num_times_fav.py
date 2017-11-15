# Answer
counts = [d['count'] for n1, n2, d in G.edges(data=True)]
maxcount = max(counts)

def test_maxcount(maxcount):
    assert maxcount == 3

test_maxcount(maxcount)
