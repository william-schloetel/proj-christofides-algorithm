# Hamiltonian Circuit
# Used to solve Christofides TSP Approximation 
#
# Author: William Schloetel
# Date: 11/20/22


def hamilton_cycle(euler_circuit):

	edges = []

	seen_nodes = dict()
	seen_nodes[euler_c[0]] = 1
	i = 1
	while(i < len(euler_c)):
		if not seen_nodes.get(euler_c[i]):
			edges.append((euler_c[i - 1], euler_c[i]))					#must pull edges from exiting edge list (which contain distances)
			seen_nodes[euler_c[i]] = 1
			i += 1
		else:
			edges.append((euler_c[i - 1], euler_c[i + 1]))
			seen_nodes[euler_c[i + 1]] = 1
			i += 2

	return edges















