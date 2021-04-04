from tkinter import Tk, Canvas
import numpy as np
# import edges_vis as ev

def init_IU(self, graph):
    cnv = Canvas(self, width = 750, height = 750, bg = 'ivory')
    cnv.pack()
    center = (375,375) # (width/2,height/2)
    radius=300 
    circle(cnv, center, radius)
    dot(cnv, graph, radius, center[0])
    all_edges(cnv, graph, radius, center[0])


def circle(canvas, center, radius):
    # Create a circle of radius R in the canvas 
    xC, yC = center # center of the circle
    A = (xC-radius, yC-radius)
    B = (xC+radius, yC+radius)
    return canvas.create_oval(A, B, width = 2)

def coord(x, y, a, b):
    return(x+b, y-a)

def angle_tab(radius, graph): 
    t = (2*np.pi)/graph.mod # I remove the graph.mod and put only graph instead, need to see this with you
    angle = [None] * graph.mod
    for k in range(graph.mod):
        angle[k] = (radius*np.cos(k*t), radius*np.sin(k*t))# angle for the dots (modulo_number)
    return angle

def dot(canvas, graph, radius, center):
    # Add the number of points needed on the cercle, they are proportionally spaced (angle : 2pi/modulo_number)
    angle = angle_tab(radius, graph)
    for j in range(len(angle)):
        a, b = angle[j]
        A = coord(center-3, center-3, a, b)
        B = coord(center+3, center+3, a, b)
        canvas.create_oval(A, B, fill='black') # create modulo_number circles (R=3)
        name_peak(canvas, radius, graph, center)

def name_peak(cnv, radius, graph, center): 
    angle = angle_tab(radius+15, graph)
    for j in range(len(angle)):
        a, b = angle[j]
        Dots_C = (center+b, center-a) # Center of each dots
        if (graph.mod<= 150): 
            size = str(int(6)) #A modifier car size pas bonne !!!!!!!!!!!!!!!!
            cnv.create_text(Dots_C, text = str(j), font = "Arial " + size + " bold")




# def all_edges(canvas, graph, radius, center):
#     angle = angle_tab(radius, graph)
#     for i in range(graph.mod): 
#         one_edge(graph, canvas,i, angle, center)
    

# def one_edge(graph,canvas, i, angle, center):
#     j = graph.modulo_result(i)
#     xA, yA= angle[i]
#     xB, yB = angle[j]
#     A = coord(center, center, xA,yA)
#     B = coord(center, center, xB, yB)
#     return canvas.create_line(A, B, fill='black', width=2)