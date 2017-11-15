# Possible Answers:
sorted(G.nodes(),
       key=lambda x:len(G.neighbors(x)), reverse=True)[0:5]
# sorted([(n, G.neighbors(n)) for n in G.nodes()],
#        key=lambda x: len(x[1]), reverse=True)[0:5]
