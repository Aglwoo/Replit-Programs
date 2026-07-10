import networkx as nx
import numpy
import matplotlib

G = nx.random_k_out_graph(n=8, k=2, alpha=0.85)
def draw_graph(G):
    nx.draw_circular(G, node_size=400, with_labels=True)

draw_graph(G)
ranks_pr = nx.pagerank(G)
ranks_pr