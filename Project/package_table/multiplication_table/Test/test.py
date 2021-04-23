from multiplication_table.process_math.Graph import Graph

from multiplication_table.process_vis.base_vis import angle_tab, coord
from multiplication_table.process_vis.edges_vis import all_edges, one_edge
from multiplication_tabl.process_vis.interface import Interface_gestion

def sparse_matrix():
    graph = Graph(10,2)
    result = (type(graph.M) != numpy)
    assert result

