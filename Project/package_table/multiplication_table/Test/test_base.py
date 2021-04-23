from multiplication_table.process_vis.edges_vis import all_edges, one_edge


def test_coord():
    result = coord(200,200,40,60)
    assert result == (260,160)

