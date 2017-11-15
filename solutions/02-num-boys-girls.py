from collections import Counter
mf_counts = Counter([d['gender']
                     for n, d in G.nodes(data=True)])

def test_answer(mf_counts):
    assert mf_counts['female'] == 17
    assert mf_counts['male'] == 12

test_answer(mf_counts)
