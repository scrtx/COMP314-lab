from lab5graph import makeGraph, Graph, libGraph
from prettytable import PrettyTable

aves = ('data/aves-sparrow-social.edges', ['a', 'b', 'w', 'year'])
bio = ('data/bio-DM-LC.edges', ['a', 'b', 'w'])
email = ('data/email-univ.edges', ['a', 'b'])
reptilia = ('data/reptilia-tortoise-network-fi.edges', ['a', 'b', 'year'])
road = ('data/road-euroroad.edges', ['a', 'b'])
rt = ('data/rt_voteonedirection.edges', ['a', 'b', 'w'])

G1 = makeGraph(aves[0], aves[1])
G2 = makeGraph(bio[0], bio[1])
G3 = makeGraph(email[0], email[1])
G4 = makeGraph(reptilia[0], reptilia[1])
G5 = makeGraph(road[0], road[1])
G6 = makeGraph(rt[0], rt[1])

G = [Graph(G1), Graph(G2), Graph(G3), Graph(G4) ,Graph(G5), Graph(G6)]
H = [libGraph(G1), libGraph(G2), libGraph(G3), libGraph(G4), libGraph(G5), libGraph(G6)]

def printTable(A, B):
    table = PrettyTable()
    table.field_names = ["Function", "Implementation", "Library"]
    table.add_row(["Number of Nodes", A.num_Vertices(), B.lib_num_nodes()])
    table.add_row(["Number of Edges", A.num_Edges(), B.lib_num_edges()])
    table.add_row(["Average Degree", A.avgDegree(), B.lib_avgDegree()])
    table.add_row(["Diameter", A.diameter(), B.lib_diameter()])
    table.add_row(["Avg Clustering Coeff", A.clustering_coefficient(), B.lib_cluster()])

    print(table)

for i in range(6):
    print(f"Comparison for Graph {i+1} : ")
    printTable(G[i], H[i])
    
for i in range(6):
    G[i].plot()
    
for i in range(6):
    G[i].plot_deg_dist()