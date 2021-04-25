import multiplication_table as mt

# Enter number of table (can be an integer or a float)
#  and modulo number (must be an integer)


# Example 1 :
table_number1 = 2
modulo_number1 = 10

graph_object1 = mt.Graph(table_number1, modulo_number1)
graph_object1.sparse_matrix()
graph_object1.print_graph()


# Example 2 :
table_number2 = 15
modulo_number2 = 800
graph_object2 = mt.Graph(table_number2, modulo_number2)
graph_object2.sparse_matrix()
graph_object2.print_graph()
