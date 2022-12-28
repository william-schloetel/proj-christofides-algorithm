# Christofides TSP Approximation 
#
# Author: William S.
# Date: 12/16/22

import modules.kruskals_algorithm as kruskals_algorithm
import modules.eulerian_circuit as euler
import modules.min_weight_perf_matching as matching
import os


# TEST GRAPH
# /////////////////////////////////////////////////////////////////////////////////

# GRAPH 1
# edge = (node1, node2, weight)
# edges =[(8, 9, 0), (0, 4, 1), (2, 8, 1), (4, 5, 1), (6, 7, 1), (1, 3, 2), \
# 		(2, 9, 2), (3, 4, 2), (3, 7, 2), (0, 3, 4), (1, 2, 4), (2, 7, 4), \
# 		(6, 8, 4), (0, 1, 5), (3, 5, 5), (7, 8, 6), (5, 6, 7), (3, 6, 11)]
# nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# GRAPH 2
# edges = [(0, 1, 1), (0, 2, 2), (0, 3, 8), (0, 4, 9), (1, 2, 1), (1, 3, 25), \
#		(1, 4, 4), (2, 3, 3), (2, 4, 1), (3, 4, 10)]
# nodes = [0, 1, 2, 3, 4]


# GRAPH 3
edges = [(0, 1, 1), (0, 2, 2), (0, 3, 8), (0, 4, 9), (1, 2, 1), (1, 3, 25), \
		(1, 4, 4), (2, 3, 3), (2, 4, 1), (3, 4, 10)]
nodes = [0, 1, 2, 3, 4]

# /////////////////////////////////////////////////////////////////////////////////


def christofides(nodes, edges):
	"""Python implementation of Christofides approximation to the Traveling 
	Salesperson Problem. This function makes use of Vladimir Kolmogorov's
	C++ implementation of his Blossom V algorithm for finding a Minimum Cost
	Perfect Matching in a weighted graph. 

	Requirements: 	
		- Graph must be a complete graph (every node must be connected 
		to every other node). To randomly generate complete graphs, see
		random_graph.py module.
		- Graph is formated as a 0-indexed list of nodes and a list of 
		edges, where each edge is a tuple: (node1, node2, weight)

	UPDATES & TO-DO:
		- Will modify this function to more optimally interact with C++
		program.

	"""

	#edges = sorted(edges, key=lambda edge: edge[2])
	#nodes = sorted(nodes)


	# ---------------------------------------------------------------------------
	# 1. Create a minimum spanning tree T (min_span_edges) of graph G (edges).
	print("1. Create a minimum spanning tree T (min_span_edges) of graph G (edges).")

	min_span_edges = kruskals_algorithm.kruskals(nodes, edges)


	# ---------------------------------------------------------------------------
	# 2. Calculate the set of vertices O with odd degree in T.
	print("2. Calculate the set of vertices O with odd degree in T.")

	# UPDATE: the degree for each node could be stored with the node in 
	# the node list, saving time
	node_count = [0 for i in range(0, len(nodes))]

	for edge in min_span_edges:
		node_count[edge[0]] += 1
		node_count[edge[1]] += 1
	odd_nodes = []
	for i in range(0, len(nodes)):
		if node_count[i] % 2 > 0:
			odd_nodes.append(nodes[i])

	# naive implementation
	subgraph = []
	for edge in edges:
		if edge[0] in odd_nodes and edge[1] in odd_nodes:
			subgraph.append(edge)

	# format edges for Blossom V program
	for i in range(len(odd_nodes)):
		for j in range(len(subgraph)):
			e = list(subgraph[j])
			if e[0] == odd_nodes[i]:
				e[0] = i
			if e[1] == odd_nodes[i]:
				e[1] = i
			subgraph[j] = tuple(e)

	total_num_edges = len(subgraph)
	total_num_nodes = len(odd_nodes)
	

	# ---------------------------------------------------------------------------
	# 3. Find a minimum-weight perfect matching M (perfect_matching_edges) in 
	#		the induced subgraph given by the vertices from O. Using Kolmogorov's 
	#     	C++ implementation of his Blossom V algorithm. This implementation is 
	#		currently the fastest technique in practice for computing a minimum 
	#  		cost perfect matching.
	print("3. Find a minimum-weight perfect matching M (perfect_matching_edges) in \
		\n the induced subgraph given by the vertices from O.")

	perfect_matching_edges = matching.min_cost_perf_matching(total_num_edges, \
									total_num_nodes, subgraph)

	# format edges back to original format
	for j in range(len(perfect_matching_edges)):
		e = list(perfect_matching_edges[j])
		e[0] = odd_nodes[e[0]]
		e[1] = odd_nodes[e[1]]
		perfect_matching_edges[j] = tuple(e)


	# ---------------------------------------------------------------------------
	# 4. Combine the edges of M (perfect_matching_edges) and T (min_span_edges) to 
	#		form a connected multigraph H in which each vertex has even degree.
	print("4. Combine the edges of M (perfect_matching_edges) and T (min_span_edges) \
		\n to form a connected multigraph H")

	multigraph_edges = list(min_span_edges + perfect_matching_edges)


	# ---------------------------------------------------------------------------
	# 5. Form an Eulerian circuit in H.
	print("5. Form an Eulerian circuit in H.")

	multigraph_adj_list = euler.create_adj_list(multigraph_edges)
	euler_path = euler.hierholzer_with_list(multigraph_edges, multigraph_adj_list)


	# ---------------------------------------------------------------------------
	# 6. Make the circuit found in previous step into a Hamiltonian circuit by
	#		skipping repeated vertices (shortcutting).
	print("6. SMake the circuit found in previous step into a Hamiltonian circuit by \
		\n skipping repeated vertices (shortcutting).")
	
	hamiltonian_ciruit = euler.hamiltonian(euler_path)
	return hamiltonian_ciruit



	

