import multiplication_table
import tkinter as Tk


#Enter number of table (can be an integer or a float) and modulo number (must be an integer)

table_number = 2 #problem if table_number is a float
modulo_number = 13

graph_object = multiplication_table.Graph(table_number, modulo_number)
graph_object.create_matrix()

graph_object.print_matrix()
graph_object.print_graph()

root = Tk()
init_IU(root, 10)
root.mainloop()
