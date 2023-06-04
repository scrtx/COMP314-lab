import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#Creates graph using nx library
def makeGraph(file, header_list):
    data = pd.read_csv(file, sep=" ",header=None, names=header_list)
    if (header_list[2:] == []):
        return nx.from_pandas_edgelist(data, header_list[0], header_list[1])
    return nx.from_pandas_edgelist(data, header_list[0], header_list[1], header_list[2:])

#Implementaions of Graph Functions
class Graph:
    def __init__(self, G) -> None:
        self.G = G
        self.V = len(G.nodes)
        self.E = len(G.edges)
        self.degrees = []
        
        for node in self.G.nodes():
            deg = len(list(self.G.neighbors(node)))
            self.degrees.append(deg)
    
    def plot(self):
        nx.draw(self.G, with_labels = True)
        plt.show()
    
    def num_Vertices(self):
        return self.V

    def num_Edges(self):
        return self.E

    def avgDegree(self):
        degree_sum = sum(deg for deg in self.degrees)
        return (degree_sum / self.V)

    def density(self):
        density = 0
        if(self.V > 1):
            density = (2 * self.E) / (self.V * (self.V - 1))
        print("Graph Density =", density)
        return density

    def bfs(self, G, start):
        visited = {}
        distance = {}
        queue = []
        
        queue.append(start)
        visited[start] = True
        distance[start] = 0
       
        while queue:
            m = queue.pop(0)
            for i in G.neighbors(m):
                if i not in visited:
                    queue.append(i)
                    visited[i] = True
                    distance[i] = distance[m] + 1
        
        return max(distance.values())

    def diameter(self):
        diameter = 0
        for node in self.G.nodes:
            diameter = max(diameter, self.bfs(self.G, node))
        return diameter

    def num_neighbours(self, node):
        return len(list(self.G.neighbors(node)))

    def num_connections(self, node):
        neighbors = list(self.G.neighbors(node))
        connections = 0
        for i in range(len(neighbors)):
            for j in range(i+1, len(neighbors)):
                if self.G.has_edge(neighbors[i], neighbors[j]):
                    connections += 1
        return connections

    def clustering_coefficient(self):
        c = []
        for node in self.G.nodes:
            k = self.num_neighbours(node)
            e = self.num_connections(node)
            
            clustering_coeff = 0.0
            if k > 1:
                clustering_coeff = (2 * e) / (k * (k - 1))                
            
            c.append(clustering_coeff)
        avg_clustering_coeff = sum(c) / len(c)
        return avg_clustering_coeff
    
    def plot_deg_dist(self):
        deg_dist = [0] * (max(self.degrees) + 1)
        
        for deg in self.degrees:
            deg_dist[deg] += 1
        
        deg_dist = [count / self.V for count in deg_dist]
        
        plt.plot(deg_dist, 'ro-')
        plt.xlabel('Degree')
        plt.ylabel('Fraction of Nodes')
        plt.title('Degree Distribution')
        plt.show()

#Library Functions for comparision
class libGraph:
    def __init__(self, G) -> None:
        self.G = G
        self.num_nodes = self.G.number_of_nodes()
        self.num_edges = self.G.number_of_edges()
    
    def lib_num_nodes(self):
        return self.num_nodes
    
    def lib_num_edges(self):
        return self.num_edges
    
    def lib_avgDegree(self):
        degree_sum = sum(deg for _, deg in self.G.degree())
        return degree_sum / self.num_nodes
    
    def lib_diameter(self):
        G0 = self.G
        if not nx.is_connected(self.G):
            largest_component = max(nx.connected_components(self.G), key=len)
            G0 = self.G.subgraph(largest_component)

        diameter = nx.diameter(G0)
        return diameter
        
    def lib_cluster(self):
        clustering = nx.clustering(self.G)
        sum = 0
        for _, coefficient in clustering.items():
            sum += coefficient
        return (sum/self.lib_num_nodes())