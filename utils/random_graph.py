# Generate a random, completely connected graph
#
# Author: William Schloetel
# Date: 12/31/22



import random

def generate_random_graph(num_nodes, min_edge_weight, max_edge_weight):
	nodes = []
	edges = []
	for i in range(0, num_nodes):
		nodes.append(i)
		for j in range(i + 1, num_nodes):
			edge_weight = random.randint(min_edge_weight, max_edge_weight)
			edges.append((i, j, edge_weight))
	return nodes, edges

