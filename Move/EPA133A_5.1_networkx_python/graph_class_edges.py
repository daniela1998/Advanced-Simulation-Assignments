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
        return f"{self.name} [{self.weight}]"


if __name__ == '__main__':
    G = nx.Graph()
    nodes = {'a': Node('a'), 'b': Node('b'), 'c': Node('c'), 'd': Node('d'), 'e': Node('e')}
    for key, node in nodes.items():
        G.add_node(node)
    G.add_edge(nodes['a'], nodes['b'], link=Link('a-b', 10))
    G.add_edge(nodes['b'], nodes['c'], link=Link('c-c', 12))
    G.add_edge(nodes['b'], nodes['e'], link=Link('b-e', 8))
    G.add_edge(nodes['d'], nodes['e'], link=Link('d-e', 17))

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='orange', node_size=500)
    labels = nx.get_edge_attributes(G, 'link')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
