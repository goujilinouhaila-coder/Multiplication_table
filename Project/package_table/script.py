import multiplication_table as mt


# Enter number of table (can be an integer or a float)
#  and modulo number (must be an integer)
table_number = 2
modulo_number = 10

graph_object = mt.Graph(table_number, modulo_number)
graph_object.create_matrix()
graph_object.print_graph()

mt.Interface_gestion(speed=3000, state_button=True, background='white',
                     state_circle=True, color_graph=['black', 'purple', "blue", "red", "cyan"],
                     background_circle="", outline_circle='black',
                     color_name="red", edges_width=1)

