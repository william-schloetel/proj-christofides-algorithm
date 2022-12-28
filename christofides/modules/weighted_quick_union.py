# Weighted Quick Union for disjoint sets
# Used for Kruskal's algorithm
#
# Author: William Schloetel
# Date: 10/10/22


class WeightedQuickUnion:

	def __init__(self, nodes):
		self.nodes = nodes
		self.parent = []
		self.size = []
		for i in range(len(nodes)):
			self.parent.append(-1)
			self.size.append(1)

	def find_root(self, n):
		"""Takes an integer value representation of node n
		and finds the root node of the set it is a member of

		"""
		while (self.parent[n] >= 0):
			n = self.parent[n]
		return n;
	
	def group(self, n1, n2):
		"""Groups nodes n1 and n2 into the same set""" 
		if self.is_grouped(n1, n2):
			return
		n1_root = self.find_root(n1)
		n2_root = self.find_root(n2)
		if self.size[n1_root] > self.size[n2_root]:
			self.size[n1_root] += self.size[n2_root]
			self.parent[n2_root] = n1_root
		else:
			self.size[n2_root] += self.size[n1_root]
			self.parent[n1_root] = n2_root

	def is_grouped(self, n1, n2):
		"""Returns True if nodes n1 and n2 are present in the same set"""
		return self.find_root(n1) == self.find_root(n2)


