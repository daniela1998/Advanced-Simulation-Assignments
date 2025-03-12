import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Link:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return self.name


if __name__ == '__main__':
    G = nx.Graph()
    nodes = {'a': Node('a'), 'b': Node('b'), 'c': Node('c'), 'd': Node('d'), 'e': Node('e')}
    for key, node in nodes.items():
        G.add_node(node)
    G.add_edge(nodes['a'], nodes['b'])
    G.add_edge(nodes['b'], nodes['c'])
    G.add_edge(nodes['b'], nodes['e'])
    G.add_edge(nodes['d'], nodes['e'])
    nx.draw(G, with_labels=True, node_color='orange')
    plt.show()
