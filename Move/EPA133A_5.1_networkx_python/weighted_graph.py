import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    G = nx.DiGraph()
    G.add_nodes_from([1, 2, 3, 4, 5])
    G.add_weighted_edges_from([(1, 2, 2.5), (2, 3, 1.2), (2, 5, 1.3), (4, 5, 4)])
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='orange')
    labels = nx.get_edge_attributes(G, 'weight')
    print(labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
