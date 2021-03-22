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


def dot(canvas, graph, R):
    # Add the number of points needed on the cercle, they are proportionally spaced (angle : 2pi/modulo_number)
    t = (2*np.pi)/graph # I remove the graph.mod and put only graph instead, need to see this with you
    for k in range(graph): # angle for the dots (modulo_number)
        angle = [(R*np.cos(k*t), R*np.sin(k*t))] # return base can be use for the creation of the edges
    for j in range(len(angle)):
        a, b = angle[j]
        A = (322+b, 322-a) 
        B = (328+b, 328-a)
        canvas.create_oval(A, B, fill='black') # create modulo_number circles (R=3)


def nb_peak():
    # Each point is associated with a number, starting with 0 until modulo_number - 1 
    # Maybe use this function only if the modulo_number < 50 or 100, to not overload the graph ?




# Exemple
modulo = 10
C = (325,325)
R = 200

root = Tk()
cnv = Canvas(root, width = 650 , height = 650, bg = 'ivory')
cnv.pack()
t = (2*np.pi)/modulo
angle = [(R*np.cos(k*t), R*np.sin(k*t)) for k in range(modulo)]
for j in range(len(angle)):
    a, b = angle[j]
    A = (322+b, 322-a)
    B = (328+b, 328-a)
    cnv.create_oval(A, B, fill='black')
circle(cnv, C, R)
cnv.mainloop()


