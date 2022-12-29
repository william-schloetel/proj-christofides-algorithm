# Minimum Weight Perfect matching
# 
# Author: William Schloetel
# Date 12/17/22

import os


# Test subgraph information 
# /////////////////////////////////////////////////////////////////////////////////
total_num_edges = 18    
total_num_nodes = 10

subgraph = [(8, 9, 0), (0, 4, 1), (2, 8, 1), (4, 5, 1), (6, 7, 1), (1, 3, 2), \
		(2, 9, 2), (3, 4, 2), (3, 7, 2), (0, 3, 4), (1, 2, 4), (2, 7, 4), \
		(6, 8, 4), (0, 1, 5), (3, 5, 5), (7, 8, 6), (5, 6, 7), (3, 6, 11)]
# /////////////////////////////////////////////////////////////////////////////////


def min_cost_perf_matching(total_num_edges, total_num_nodes, subgraph):
	# converting subgraph to format read by Kolmogorov's program
	kolmogorov_formated_list_of_edges = [str(total_num_nodes) + " " + str(total_num_edges) + "\n"]
	subgraph_dictionary = {}
	for edge in subgraph:
		# convert tuple to string
		# (8, 9, 0)  -->   "8 9 0"
		st = ""
		st = st + str(edge[0]) + " " + str(edge[1])
		subgraph_dictionary[st] = edge
		st = st + " " + str(edge[2]) + "\n"
		kolmogorov_formated_list_of_edges.append(st)

	# writing graph data to file
	with open('modules/blossom_graph_files/subgraph.txt', 'w') as f:
	    f.writelines(kolmogorov_formated_list_of_edges)
	    f.close()

	# run Kolmogorov's program
	print("BEGIN Blossom V Algorithm -------- ")
	os.system("modules/blossom5-v2.05.src/blossom5 -e modules/blossom_graph_files/subgraph.txt \
		-w modules/blossom_graph_files/solution.txt")
	print("END Blossom V Algorithm  -------- ")

	# read program's solution from file
	with open('modules/blossom_graph_files/solution.txt', 'r') as s:
		content = s.readlines()

	# format data in a way meaningful to christofides.py
	perfect_matching_edges = []
	for x in range(1, len(content)):
		key = content[x][0:3]
		perfect_matching_edges.append(subgraph_dictionary[key])

	return perfect_matching_edges




