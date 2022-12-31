# Eulerian Circuit using Hierholzer's Algorithm
#
# Author: William Schloetel 
# Date: 12/20/22

import copy

def create_adj_set(edges):
	adj_set = dict()
	for edge in edges:
		if edge[0] in adj_set:
			adj_set[edge[0]].add(edge[1])
		else:
			adj_set[edge[0]] = {edge[1]}
		if edge[1] in adj_set:
			adj_set[edge[1]].add(edge[0])
		else: 
			adj_set[edge[1]] = {edge[0]}	
	return adj_set

def create_adj_list(edges):
	adj_list = dict()
	for edge in edges:
		if edge[0] in adj_list:
			adj_list[edge[0]].append(edge[1])
		else:
			adj_list[edge[0]] = [edge[1]]
		if edge[1] in adj_list:
			adj_list[edge[1]].append(edge[0])
		else: 
			adj_list[edge[1]] = [edge[0]]	
	return adj_list

def hierholzer_with_set(edges, adj_set):
	"""Returns a list of edges forming an Euler Path using Hierholzer's Algorithm"""
	if not is_eulerian(adj_set):
		print("Graph is not eulerian. It contains nodes with odd degree.")
		return 
	adj_set = copy.deepcopy(adj_set)
	curr_node = edges[0][0]
	euler_path = [curr_node]
	num_edges = len(edges)
	while num_edges > 0:
		# if the degree of curr_node > 0
	    if len(adj_set[curr_node]) > 0:
	    	next_node = adj_set[curr_node].pop()
	    	euler_path.append(next_node)
	    	adj_set[next_node].remove(curr_node)
	    	curr_node = next_node
	    	num_edges -= 1
		# cycle through the list until you find a node with remaining incident edges 
	    else:
	    	euler_path.insert(0, euler_path.pop())	# insert end at beginning 
	    	curr_node = euler_path[-1]
	return euler_path

def hierholzer_with_list(edges, adj_list):
	"""Returns a list of edges forming an Euler Path using Hierholzer's Algorithm"""
	if not is_eulerian(adj_list):
		print("Graph is not eulerian. It contains nodes with odd degree.")
		return 
	adj_list = copy.deepcopy(adj_list)
	curr_node = edges[0][0]
	euler_path = [curr_node]
	num_edges = len(edges)
	while num_edges > 0:
		# if the degree of curr_node > 0
	    if len(adj_list[curr_node]) > 0:
	    	next_node = adj_list[curr_node].pop()
	    	euler_path.append(next_node)

	    	adj_list[next_node].remove(curr_node)
	    	curr_node = next_node
	    	num_edges -= 1
		# cycle through the list until you find a node with remaining incident edges 
	    else:
	    	euler_path.insert(0, euler_path.pop())	# insert end at beginning 
	    	curr_node = euler_path[-1]
	return euler_path

def is_eulerian(adj_set):
	for node in adj_set:
		if len(adj_set[node]) % 2 > 0:
			return False
	return True

def hamiltonian(euler_path):
	circuit = []
	seen_nodes = set()
	for node in euler_path:
		if node in seen_nodes:
			continue
		else:
			seen_nodes.add(node)
			circuit.append(node)
	return circuit



