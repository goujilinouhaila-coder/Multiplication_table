import multiplication_table as mt
import tkinter as Tk


#Enter number of table (can be an integer or a float) and modulo number (must be an integer)

table_number = 2.71 
modulo_number = 10

graph_object = mt.Graph(table_number, modulo_number)
graph_object.create_matrix()

graph_object.print_matrix()
graph_object.print_graph()

mt.user_IU()

