import multiplication_table as mt
import time

start = time.time()
# Enter number of table (can be an integer or a float)
#  and modulo number (must be an integer)
table_number = 2
modulo_number = 18

graph_object = mt.Graph(table_number, modulo_number)
graph_object.sparse_matrix()
graph_object.print_graph()

mt.Interface_gestion(speed=10, state_button=True, background='white',
                     state_circle=True,
                     color_graph=['black', 'purple', "blue", "red", "cyan"],
                     background_circle="", outline_circle='black',
                     color_name="red", edges_width=1)

end = time.time()
print(end-start)