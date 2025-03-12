import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    G = nx.MultiGraph()
    G.add_nodes_from([1, 2, 3, 4, 5])
    G.add_edge(1, 2, '12')
    G.add_edge(2, 3, '23')
    G.add_edge(2, 5, '25a')
    G.add_edge(2, 5, '25b')
    G.add_edge(5, 2, '52')
    G.add_edge(4, 5, '45')
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"# edges connected to node 2: {G.degree(2)}")
    nx.draw(G, with_labels=True, node_color='orange')
    # nx.draw(G, with_labels=True, connectionstyle='arc3, rad = 0.1') # for digraph
    plt.show()
