import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    G = nx.Graph()
    G.add_node(1, pos=(12, 4))
    G.add_node(2, pos=(5, 5))
    G.add_node(3, pos=(8, 7))
    G.add_node(4, pos=(3, 9))
    G.add_node(5, pos=(4, 1))
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(2, 5)
    G.add_edge(4, 5)
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_color='orange')
    plt.show()
