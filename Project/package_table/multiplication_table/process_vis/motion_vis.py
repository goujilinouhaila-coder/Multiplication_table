from tkinter import Tk, Canvas, Scale 
import time 
from math import sin, cos, pi 
import numpy as np 
import multiplication_table as mt
import multiplication_table.process_vis.edges_vis as ev
import multiplication_table.process_vis.base_vis as bv

# width of the animation window
animation_window_width=750
# height of the animation window
animation_window_height=750
# the pixel movement of the circle for each iteration
animation_circle_min_movement = 5
# delay between successive frames in seconds
animation_refresh_seconds = 5

<<<<<<< HEAD
def create_animation_window():
    window = Tk()
    window.title("Tkinter Animation ")
    window.geometry(f'{animation_window_width}x{animation_window_height}')
    return window

  # Create a canvas for animation and add it to main window
def create_animation_canvas(window):
    canvas = Canvas(window)
    canvas.configure(bg="ivory")
    canvas.pack(fill="both", expand=True)
    return canvas


class Motion:
=======
>>>>>>> main


# def create_animation_window():
#     window = Tk()
#     window.title("Tkinter Animation ")
#     window.geometry(f'{animation_window_width}x{animation_window_height}')
#     return window

#   # Create a canvas for animation and add it to main window
# def create_animation_canvas(window):
#     canvas = Canvas(window)
#     canvas.configure(bg="ivory")
#     canvas.pack(fill="both", expand=True)
#     return canvas

# edge = canvas.create_line(200,200,400,400,fill = "black",width=2)
class Motion:

    
  def __init__(self):
    self.window = self.create_animation_window()
    self.canvas = self.create_animation_canvas(self.window)
    

  def create_animation_window(self):
      window = Tk()
      window.title("Tkinter Animation ")
      window.geometry(f'{animation_window_width}x{animation_window_height}')
      return window

    # Create a canvas for animation and add it to main window
  def create_animation_canvas(self, window):
      canvas = Canvas(window)
      canvas.configure(bg="white")
      canvas.pack(fill="both", expand=True)
      return canvas

  def show_update(self):
    self.canvas.delete('all')
    bv.circle(self.canvas, center, radius)
    bv.dot(self.canvas, graph, radius, center[0])
    ev.all_edges(self.canvas, graph, radius, center[0])


  def movement(self,edge):
    self.canvas.itemconfigure(edge, fill="red")
    self.canvas.coords(edge,100,100,400,400)
    self.window.after(10,self.movement)


  # Create and animate the circle 
  def animate_circle(self):
      global N, modulo, radius, graph, center
      radius=300
      N=2
      modulo=2
      center=(360,360)
      graph = mt.Graph(N, modulo)
      edge = self.canvas.create_line(200,200,400,400,fill = "black",width=2)
<<<<<<< HEAD
      #self.canvas.after(10000,self.movement(edge))
=======
      self.canvas.after(10000,self.movement(edge))
>>>>>>> main
      self.movement(edge)
      self.window.mainloop()

      #self.show_update()
      #self.window.mainloop()
      # while True:
      #   self.canvas.coords(var, 0, 0, 300, 300)
      #   #self.show_update()
      #   self.window.update()
      #   time.sleep(animation_refresh_seconds)
          

      

