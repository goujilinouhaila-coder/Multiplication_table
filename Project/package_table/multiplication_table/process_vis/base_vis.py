from tkinter import Tk, Canvas
import numpy as np


def init_IU(self):
    cnv = Canvas(self, width = 500, height = 500, bg = 'ivory')
    cnv.pack()
    C = (250,250) # (width/2,height/2) 
    circle(cnv, C, R=100)


def circle(canvas, C, R):
    # Create a circle of radius R in the canvas 
    xC, yC = C # center of the circle
    A = (xC-R, yC-R)
    B = (xC+R, yC+R)
    return canvas.create_oval(A, B, width = 2)


def dot():
    # Add the number of points needed on the cercle, they are proportionally spaced (angle : 2pi/modulo_number)
    for k in range(p): # angle for the dots (p=modulo_number)
        base=[(R*np.cos(k*t), R*np.sin(k*t))]
    # return base can be use for the creation of the edges 


def nb_peak():
    # Each point is associated with a number, starting with 0 until modulo_number - 1 
    # Maybe use this function only if the modulo_number < 50 or 100, to not overload the graph ?


