from tkinter import Tk, Canvas
import numpy as np
import multiplication_table.process_vis.base_vis as bv


def all_edges(canvas, graph, radius, center):
    angle = bv.angle_tab(radius, graph)
    for i in range(graph.mod): 
        one_edge(graph, canvas, i, angle, center)
    

def one_edge(graph,canvas, i, angle, center):
    j = graph.modulo_result(i)
    xA, yA= angle[i]
    xB, yB = angle[j]
    A = bv.coord(center, center, xA,yA)
    B = bv.coord(center, center, xB, yB)
    return canvas.create_line(A, B, fill='black', width=2)