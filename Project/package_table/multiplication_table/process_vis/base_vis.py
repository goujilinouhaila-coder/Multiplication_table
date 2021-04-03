from tkinter import Tk, Canvas
import numpy as np


def init_IU(self, graph):
    cnv = Canvas(self, width = 650, height = 650, bg = 'ivory')
    cnv.pack()
    C = (325,325) # (width/2,height/2)
    R=200 
    circle(cnv, C, R)
    dot(cnv, graph, R)


def circle(canvas, C, R):
    # Create a circle of radius R in the canvas 
    xC, yC = C # center of the circle
    A = (xC-R, yC-R)
    B = (xC+R, yC+R)
    return canvas.create_oval(A, B, width = 2)

def coord(x, y, a, b):
    return(x+b, y-a)

def dot(canvas, graph, R):
    # Add the number of points needed on the cercle, they are proportionally spaced (angle : 2pi/modulo_number)
    t = (2*np.pi)/graph # I remove the graph.mod and put only graph instead, need to see this with you
    angle = [(R*np.cos(k*t), R*np.sin(k*t)) for k in range(graph)] # angle for the dots (modulo_number)
    for j in range(len(angle)):
        a, b = angle[j]
        A = coord(322, 322, a, b)
        B = coord(328, 328, a, b)
        Dots_C = (325+b, 325-a) # Center of each dots
        canvas.create_oval(A, B, fill='black') # create modulo_number circles (R=3)
        nb_peak(canvas, a, b, j, Dots_C)

def nb_peak(cnv, a, b, j, Dots_C):
    # Each point is associated with a number, starting with 0 until modulo_number - 1 
    # Maybe use this function only if the modulo_number < 50 or 100, to not overload the graph ?
    if a == 200 and b < 1e-10:
        cnv.create_text(Dots_C, anchor = 's', text = str(j), font = "Arial 10 bold")
    elif a == -200 and b < 1e-10:
        cnv.create_text(Dots_C, anchor = 'n', text = str(j), font = "Arial 10 bold")
    elif a < 1e-10  and b == 200:
        cnv.create_text(Dots_C, anchor = 'w', text = str(j), font = "Arial 10 bold")
    elif a < 1e-10 and b == -200:
        cnv.create_text(Dots_C, anchor = 'e', text = str(j), font = "Arial 10 bold")
    elif 0 < a < 200 and 0 < b < 200:
        cnv.create_text(Dots_C, anchor = 'sw', text = str(j), font = "Arial 10 bold")
    elif -200 < a < 0 and 0 < b < 200:
        cnv.create_text(Dots_C, anchor = 'nw', text = str(j), font = "Arial 10 bold")
    elif -200 < a < 0 and -200 < b < 0 :
        cnv.create_text(Dots_C, anchor = 'ne', text = str(j), font = "Arial 10 bold")
    else :
        cnv.create_text(Dots_C, anchor = 'se', text = str(j), font = "Arial 10 bold")



