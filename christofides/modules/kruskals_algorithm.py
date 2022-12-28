# Kruskal's algorithm
# Used to solve Christofides TSP Approximation 
#
# Author: William Schloetel
# Date: 11/21/22

import math
import modules.weighted_quick_union as w


#sorted_edges = [('a','b', 2), ('a','c', 5), ('b','c', 5), ('c','d', 6), ('c','e', 7)]
#nodes = ['a', 'b', 'c', 'd', 'e']


# edge = (node1, node2, distance)
sorted_edges =[(8, 9, 0), (0, 4, 1), (2, 8, 1), (4, 5, 1), (6, 7, 1), (1, 3, 2), \
				(2, 9, 2), (3, 4, 2), (3, 7, 2), (0, 3, 4), (1, 2, 4), (2, 7, 4), \
				(6, 8, 4), (0, 1, 5), (3, 5, 5), (7, 8, 6), (5, 6, 7), (3, 6, 11)]
sorted_nodes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def kruskals(nodes, edges):
	"""Returns selected edges that form a minimum spanning tree"""

	edges = sorted(edges, key=lambda edge: edge[2])
	nodes = sorted(nodes)

	wqu = w.WeightedQuickUnion(nodes)
	selected_edges = []
	for edge in edges:
		if not wqu.is_grouped(edge[0], edge[1]):
			wqu.group(edge[0], edge[1])
			selected_edges.append(edge)
	return selected_edges

	














