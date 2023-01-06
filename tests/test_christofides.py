import utils.random_graph as r
import christofides as ch
import pytest




@pytest.fixture
def random_graph():
	"""Generates random graph with 10 nodes using utils.random_graph"""
	return r.generate_random_graph(10, 100, 1000)

def test_path_has_correct_num_nodes(random_graph):
	path = ch.christofides(random_graph[0], random_graph[1])
	assert len(path) == len(random_graph[0])

def test_path_has_correct_node_labels(random_graph):
	path = ch.christofides(random_graph[0], random_graph[1])
	for node in path:
		assert node in random_graph[0]
	

