from tkinter import Tk, Canvas, Scale, Button , Toplevel, Label, Scrollbar, Text, END, Y
import multiplication_table as mt
import multiplication_table.process_vis.edges_vis as ev
import multiplication_table.process_vis.base_vis as bv
from PIL import Image
import imageio
import os
import shutil
import numpy as np


class Interface_gestion:

    def __init__(self, speed, state_button, background, state_circle, color_graph, background_circle, outline_circle, color_name, edges_width):
        self.nb_frame = 0
        self.nb_video = 0
        self.design_aspect(speed, state_circle, color_graph, background_circle,
                           outline_circle, color_name, edges_width)
        self.window_init(background)
        self.graph_init()
        self.graph_vis()
        self.slider()
        if (state_button):
            self.motion_button()
        self.root.mainloop()

    def design_aspect(self, speed, state_circle, color_graph, background_circle, outline_circle, color_name, edges_width):
        self.state_circle = state_circle
        self.outline_circle = outline_circle
        self.background_circle = background_circle
        self.color_name = color_name
        self.color_graph = color_graph
        self.speed = speed
        self.edges_width = edges_width

    def window_init(self, background):
        self.root = Tk()
        self.cnv = Canvas(self.root, width=750, height=750, bg=background)
        self.cnv.pack(side="left", fill="both", expand=True)

    def graph_init(self):
        self.radius = 300
        self.N = 2
        self.modulo = 2
        self.center = (360, 360)
        self.graph = mt.Graph(self.N, self.modulo)

    def graph_vis(self):
        bv.circle(self.cnv, self.center, self.radius, self.state_circle,
                  self.background_circle, self.outline_circle)
        bv.dot(self.cnv, self.graph, self.radius, self.center[0],
               self.color_graph, self.color_name)
        ev.all_edges(self.cnv, self.graph, self.radius, self.center[0],
                     self.color_graph, self.edges_width)

    def table(self, n):
        self.N = float(n)
        self.graph.N = float(n)
        self.show_update()

    def peak(self, mod):
        self.modulo = int(mod)
        self.graph.mod = int(mod)
        self.show_update()

    def show_update(self):
        self.cnv.delete("all")
        self.graph_vis()

    def slider(self):
        self.peak_cursor = Scale(self.root, label="Modulo",
                                 font="Arial 12 bold", orient="horizontal",
                                 command=self.peak, from_=2, to=200,
                                 length=250, repeatdelay=500)                
        self.peak_cursor.pack(pady=10, anchor="center")
        self.peak_cursor.set(10)
        self.table_cursor = Scale(self.root, label="Table",
                                  font="Arial 12 bold", orient="horizontal",
                                  command=self.table, from_=2, to=400,
                                  length=250, resolution=0.01,
                                  repeatdelay=1000)
        self.table_cursor.pack(pady=10, anchor="center")

    def move_value(self):
        self.state_button = not self.state_button
        while (self.state_button):
            self.table_cursor.set(self.table_cursor.get()+0.01)
            self.root.after(self.speed)
            self.root.update()
        
    def save_frame(self):
        text = self.cnv.create_text(640,730,fill="black",font="Arial 12 italic bold",text="Table de "+ str(self.N) + " modulo " + str(self.modulo))
        self.cnv.postscript(file="Project/package_table/temp/eps/frame.eps")
        img = Image.open("Project/package_table/temp/eps/frame.eps")
        if (self.nb_frame==0):
            os.mkdir('Project/package_table/temp/png'+str(self.nb_video))
        img.save('Project/package_table/temp/png'+str(self.nb_video)+'/' + str(self.nb_frame) + '.png')
        self.cnv.delete(text)
        self.nb_frame = self.nb_frame + 1

    def save_video(self):
        if (os.path.exists('Project/package_table/temp/png' + str(self.nb_video))):
            folder = 'Project/package_table/temp/png' + str(self.nb_video)
            frame=[]
            for i in range (self.nb_frame):
                frame.append(str(i) + ".png")
            files = [f"{folder}\{file}" for file in frame]
            images = [imageio.imread(file) for file in files]
            imageio.mimwrite('gif/gif'+ str(self.nb_video)+'.gif', images, fps=5)
            self.nb_video= self.nb_video + 1
            self.nb_frame = 0

    def destroy_root(self):
        for i in range(self.nb_video):
            shutil.rmtree('Project/package_table/temp/png'+str(i))
        self.root.destroy()

    def createNewWindow(self):
        new_root = Tk()
        new_root.geometry("300x350")
        scrollbar = Scrollbar(new_root)
        scrollbar.pack(side='right', fill=Y)
        textbox = Text(new_root)
        textbox.pack()
        for i in range(self.modulo):
            textbox.insert(END, str(self.N)+ " * " + str(i) + " modulo " + str(self.modulo) + " = " + str(round(self.N*i%self.modulo,2)) + "\n")
        textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=textbox.yview)
        new_root.mainloop()
    
    def create_description(self):
        newWindow = Toplevel(self.root)
        text=Label(newWindow, text="A midi j'ai mangé de la chantilligjkttttttttttttttttttttttttttttttttttttttttddeeeeeeeeeeeee \n \n \n ")
        text.pack()
        text=Label(newWindow, text="A midi j'ai mangé de la chantilligjkttttttttttttttttttttttttttttttttttttttttddeeeeeeeeeeeee \n \n \n ")
        text.pack()

    def motion_button(self):
        self.state_button = False
        button_play = Button(self.root, text="Play/Pause",
                             command=self.move_value)
        button_play.pack(padx=50, pady=5, side="top")
        button_photo= Button(self.root, text="Photo",
                                  command=self.save_frame)
        button_photo.pack(padx=50, pady=5, side="top")
        button_video = Button(self.root, text="Vidéo",
                                  command=self.save_video)
        button_video.pack(padx=50, pady=5, side="top")
        button_table_window = Button(self.root, text="Table of",
                                  command=self.createNewWindow)
        button_table_window.pack(padx=50, pady=5, side="top")
        button_table_window = Button(self.root, text="Description",
                                  command=self.create_description)
        button_table_window.pack(padx=50, pady=5, side="top")
        quit = Button(self.root, text="Quit", fg="black",
                      command=self.destroy_root)
        quit.pack(padx=50, pady=5, side="bottom")
