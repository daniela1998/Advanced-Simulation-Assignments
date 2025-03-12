import math
import networkx as nx
import matplotlib.pyplot as plt


def distance(p1, p2):
    dx = abs(p2['pos'][0] - p1['pos'][0])
    dy = abs(p2['pos'][1] - p1['pos'][1])
    return round(100 * math.sqrt(dx * dx + dy * dy)) / 100


if __name__ == '__main__':
    G = nx.Graph()
    G.add_node(1, pos=(12, 4))
    G.add_node(2, pos=(5, 5))
    G.add_node(3, pos=(13, 10))
    G.add_node(4, pos=(3, 9))
    G.add_node(5, pos=(4, 1))
    G.add_node(6, pos=(8, 3))
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(2, 5)
    G.add_edge(4, 5)
    G.add_edge(4, 2)
    G.add_edge(5, 6)
    G.add_edge(1, 6)
    G.add_edge(2, 6)
    for u,v in G.edges:
        G[u][v]['weight'] = distance(G.nodes.get(u), G.nodes.get(v))

    sp = nx.shortest_path(G, 4, 3, weight='weight')
    splen = nx.shortest_path_length(G, 4, 3, weight='weight')
    print(f"Shortest path from node 4 to node 3 is {sp} with length {splen}")
    print(f"All shortest paths  {nx.floyd_warshall(G, 'weight')}")
    print(f"Degree centrality: {nx.degree_centrality(G)}")
    for n in G.nodes:
        print(f"Closeness centrality node {n}: {nx.closeness_centrality(G, n, 'weight')}")
    for n in G.nodes:
        print(f"Betweenness centrality node {n}: {nx.betweenness_centrality(G, n, weight='weight')}")
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, node_color='orange', with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
