import multiplication_table as mt
import tkinter as Tk


#Enter number of table (can be an integer or a float) and modulo number (must be an integer)

table_number = 3 #problem if table_number is a float
modulo_number = 13

graph_object = mt.Graph(table_number, modulo_number)
graph_object.create_matrix()

graph_object.print_matrix()
graph_object.print_graph()

root = Tk.Tk()
mt.init_IU(root, graph_object)
root.mainloop()

# 10     16     
# 150    6

# 15     2.6666
# 0.04   0.625