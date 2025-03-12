import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    G = nx.DiGraph()
    G.add_nodes_from([1, 2, 3, 4, 5])
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(2, 5)
    G.add_edge(4, 5)
    nx.draw(G, with_labels=True, node_color='orange')
    plt.show()
