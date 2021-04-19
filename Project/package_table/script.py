import multiplication_table as mt


# Enter number of table (can be an integer or a float)
#  and modulo number (must be an integer)
table_number = 2.71
modulo_number = 10

graph_object = mt.Graph(table_number, modulo_number)
graph_object.create_matrix()
graph_object.print_graph()

mt.Interface_gestion(speed=10, state_button=True, background ='white', state_circle= True, color_graph= 'red', background_circle= "", outline_circle= 'green', color_name= "yellow", edges_width= 3)
# speed=vitesse visualisation
# state_button = affiche le bouton correspondant au deplacement 
