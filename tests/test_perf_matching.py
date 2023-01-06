from utils.min_weight_perf_matching import min_cost_perf_matching as pm


total_num_edges = 18    
total_num_nodes = 10

# subgraph = [(8, 9, 0), (0, 4, 1), (2, 8, 1), (4, 5, 1), (6, 7, 1), (1, 3, 2), \
# 		(2, 9, 2), (3, 4, 2), (3, 7, 2), (0, 3, 4), (1, 2, 4), (2, 7, 4), \
# 		(6, 8, 4), (0, 1, 5), (3, 5, 5), (7, 8, 6), (5, 6, 7), (3, 6, 11)]



# REQUIREMENT OF THE GRAPH:
# THE TWO NODES OF AN EDGE MUST BE ORDERED NUMERICALLY 
#  (0, 3, 4)   --> OK
#  (3, 0, 4)   --> INCORRECT, WILL ERROR!!!!
#
subgraph = [(9, 8, 0), (0, 4, 1), (2, 8, 1), (4, 5, 1), (7, 6, 1), (1, 3, 2), \
		(2, 9, 2), (3, 4, 2), (3, 7, 2), (3, 0, 4), (1, 2, 4), (2, 7, 4), \
		(6, 8, 4), (0, 1, 5), (3, 5, 5), (7, 8, 6), (5, 6, 7), (3, 6, 11)]