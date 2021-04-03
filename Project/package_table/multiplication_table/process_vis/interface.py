from tkinter import Tk, Canvas, Scale  
from math import sin, cos, pi 
import numpy as np 
from .base_vis import circle, dot 

def table(n):
    global N #Declaration of the variable
    N=int(n)

def peak(mod):
    global modulo
    modulo=int(mod)

## Coding the function with the "Scale" widget which allows the user to select a numeric value by moving  a cursor
##button along a scale.
def user_IU():
    global N, modulo, cnv, radius, a, b 
    # Starting position
    radius=200
    N=modulo=2
    root=Tk()
    a=b=1.2*radius
    circle_center=(a,a)
    cnv=Canvas(root, width=2*a, height=2*b, bg="ivory")
    cnv.pack(side="left")
    circle(cnv, circle_center, radius)
    dot(cnv, modulo, radius)
    table_cursor = Scale(root, label="Table of ...",font="Arial 15 bold",orient = "horizontal", command=table,from_=2, to=50, length=250)
    table_cursor.pack(pady=15)
    peak_cursor = Scale(root, label="Number of peaks",font="Arial 15 bold",orient = "horizontal", command=peak,from_=2, to=200, length=250)
    peak_cursor.pack(pady=5)
    root.mainloop()

user_IU() 


