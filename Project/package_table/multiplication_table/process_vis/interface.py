from tkinter import Tk, Canvas, Scale  
from math import sin, cos, pi 
import numpy as np 
import multiplication_table as mt
import multiplication_table.process_vis.edges_vis as ev
import multiplication_table.process_vis.base_vis as bv


def table(n):
    global N #Declaration of the variable
    N = float(n)
    graph.N = float(n)
    show_update()
   

def peak(mod):
    global modulo
    modulo=int(mod)
    graph.mod= int(mod)
    show_update()
   

def show_update():
    cnv.delete('all')
    bv.circle(cnv, center, radius)
    bv.dot(cnv, graph, radius, center[0])
    ev.all_edges(cnv, graph, radius, center[0])
   

## Coding the function with the "Scale" widget which allows the user to select a numeric value by moving  a cursor
##button along a scale.
def user_IU():
    global N, modulo, cnv, radius, graph, center
    root = Tk()
    radius=300
    N=2
    modulo=2
    center=(360,360)
    graph = mt.Graph(N, modulo)
    cnv = Canvas(root, width = 750, height = 750, bg = 'ivory')
    cnv.pack(side="left")
    show_update()
    table_cursor = Scale(root, label="Table of ...",font="Arial 15 bold",orient = "horizontal", command=table,from_=2, to=450, length=250, resolution=0.01)
    table_cursor.pack(pady=15)
    peak_cursor = Scale(root, label="Number of peaks",font="Arial 15 bold",orient = "horizontal", command=peak,from_=2, to=200, length=250)
    peak_cursor.pack(pady=5)
    root.mainloop()

