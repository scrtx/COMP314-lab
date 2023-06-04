from lab5graph import makeGraph, Graph, libGraph
from prettytable import PrettyTable

aves = ('data/aves-sparrow-social.edges', ['a', 'b', 'w', 'year'])
rt_barahin = ('data/rt_bahrain.edges', ['a', 'b', 'w'])
rt_dash = ('data/rt_dash.edges', ['a', 'b', 'w'])
rt_gop = ('data/rt_gop.edges', ['a', 'b', 'w'])
rt_oman = ('data/rt_oman.edges', ['a', 'b', 'w'])
soc = ('data/soc-advogato.edges', ['a', 'b', 'w'])


G1 = makeGraph(aves[0], aves[1])
G2 = makeGraph(rt_barahin[0], rt_barahin[1])
G3 = makeGraph(rt_dash[0], rt_dash[1])
G4 = makeGraph(rt_gop[0], rt_gop[1])
G5 = makeGraph(rt_oman[0], rt_oman[1])
G6 = makeGraph(soc[0], soc[1])

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