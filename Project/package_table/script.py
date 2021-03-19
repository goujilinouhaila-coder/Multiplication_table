import multiplication_table

graph_object = multiplication_table.Graph(6, 5)
graph_object.add_edge(2, 4)
graph_object.add_edge(1, 5)
graph_object.add_edge(4, 5)
graph_object.print_matrix()
graph_object.print_graph()