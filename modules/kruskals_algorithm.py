# Kruskal's algorithm
# Used to solve Christofides TSP Approximation 
#
# Author: William Schloetel
# Date: 11/21/22

import math
import modules.weighted_quick_union as w


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

	














