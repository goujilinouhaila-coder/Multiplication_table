from tkinter import Tk, Canvas, Scale, Button, Toplevel, Label, Scrollbar, Text, END, Y
import multiplication_table as mt
import multiplication_table.process_vis.edges_vis as ev
import multiplication_table.process_vis.base_vis as bv
from PIL import Image
import imageio
import os
import shutil
import time

class Interface_gestion:
    """
    This class supports functions which is used, for the graphical interface and link between the different aspects of visualization, 
    as well as the colors and design. It also generates the movement  in any canvas or tkinter toplevel.
    """

    def __init__(self, speed, state_button, background, state_circle, color_graph, background_circle, outline_circle, color_name, edges_width): 
        """
        This function is a constructor method, that instantiates the speed and all different aspects of the design and movement of the circle. 

        :param speed: Corresponds to the speed of the circle's movement 
        :type speed: float
        :param state_button: Show the button if it's true
        :type state_button: boolean
        :param state_circle: Displays the frame of the circle if it takes True
        :type state_circle: boolean
        :param color_graph: It's about a table of colors of the circle frame
        :type color_graph: list of strings
        :param background_circle:  Generates the color of the background of the circle
        :type background_circle: str
        :param outline_circle: The color of the circle' lines
        :type outline_circle: str
        :param color_name: The color of the numbers placed on the frame of the circle
        :type color_name: str
        :param edges_width: The width of ridgs (edges)
        :type edges_width: float or int. 
        :param nb_frame: The number of images captured for a gif
        :type nb_frame: int
        :param nb_video: The number of video already created 
        :type nb_video: int
        """
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
        """
        Initialization of the design aspect parameters.

        :param speed: Corresponds to the speed of the circle's movement. 
        :type N: float
        :param state_circle: Displays the frame of the circle if it takes True
        :type state_circle: boolean
        :param color_graph: It's about a table of colors of the circle frame
        :type color_graph: list of strings
        :param background_circle: Generates the color of the background of the circle 
        :type background_circle: str
        :param outline_circle: The color of the circle' lines
        :type outline_circle: str
        :param color_name: The color of the numbers placed on the frame of the circle
        :type color_name: str
        :param edges_width: The width of ridgs (edges)
        :type edges_width: float or int
        """
        self.state_circle = state_circle
        self.outline_circle = outline_circle
        self.background_circle = background_circle
        self.color_name = color_name
        self.color_graph = color_graph
        self.speed = speed
        self.edges_width = edges_width

    def window_init(self, background):
        '''
        Initialize the interface'window refers to a rectangular area somewhere on the user's display screen through which you can interact.
        '''
        self.root = Tk()
        self.cnv = Canvas(self.root, width=750, height=750, bg=background)
        self.cnv.pack(side="left", fill="both", expand=True)

    def graph_init(self):
        '''
        This method initializes the graph, as one its radius, its center, as well as its multiplication table and its modulo.
        '''
        self.radius = 300
        self.N = 2
        self.modulo = 2
        self.center = (360, 360)
        self.graph = mt.Graph(self.N, self.modulo)

    def graph_vis(self):
        '''
        Initialize the visualization part of the graph, concerning its dots and edges. 
        '''
        start = time.time()
        bv.circle(self.cnv, self.center, self.radius, self.state_circle,
                  self.background_circle, self.outline_circle)
        bv.dot(self.cnv, self.graph, self.radius, self.center[0],
               self.color_graph, self.color_name)
        ev.all_edges(self.cnv, self.graph, self.radius, self.center[0],
                     self.color_graph, self.edges_width)
        end = time.time()
        print("graph_vis'time : " + str(end-start))

    def table(self, n):
        '''
        This method is the table of n where the value read by the cursor.

        :param n: Represent the number in base 10. Like exemple if the cursor is moved switches to position 40; we have a table call ("42")
        :type n: str 
        '''
        self.N = float(n)
        self.graph.N = float(n)
        self.show_update()

    def vertices(self, mod):
        '''
        Represents the modulo of the multiplication table and which returns to the peaks of the circle.
        '''
        self.modulo = int(mod)
        self.graph.mod = int(mod)
        self.show_update()

    def show_update(self):
        '''
        Removes the previous Canvas and recreates a new one.
        '''
        start = time.time()
        self.cnv.delete("all")
        self.graph_vis()
        end = time.time()
        print("Show_update'time : " + str(end-start))

    def slider(self):
        '''
        This method generates the two cursors which captures the number of the table and the number of vertices (modulo). 
        The table cursor captures all tables from 2 to 400, it is placed horizontally and is 250 pixels long. The same for the other cursor 
        of the modulo which represents the number of points (vertices).
        '''
        self.peak_cursor = Scale(self.root, label="Modulo",
                                 font="Arial 12 bold", orient="horizontal",
                                 command=self.vertices, from_=2, to=200,
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
        '''
        By this method, we add 0.01 each time we take a value from the multiplication table.
        We rebuild the movement which is continuous.
        '''
        self.state_button = not self.state_button
        while (self.state_button):
            self.table_cursor.set(self.table_cursor.get()+0.01)
            self.root.after(self.speed)
            self.root.update()

    def save_frame(self):
        """
        This method captures the current canvas, converts it to .png format and saves it in the correct directory "/temp/png{number_video}".
        """
        text = self.cnv.create_text(640, 730, fill="black", 
                                    font="Arial 12 italic bold",
                                    text="Table de "+str(self.N) + " modulo "+str(self.modulo))
        self.cnv.postscript(file="Project/package_table/temp/eps/frame.eps")
        img = Image.open("Project/package_table/temp/eps/frame.eps")
        if (self.nb_frame == 0):
            os.mkdir('Project/package_table/temp/png'+str(self.nb_video))
        img.save('Project/package_table/temp/png'+str(self.nb_video)+'/'+str(self.nb_frame)+'.png')
        self.cnv.delete(text)
        self.nb_frame = self.nb_frame + 1

    def save_video(self):
        """
        This method accesses the folder where the corresponding images are saved.
        Then it creates the gif from the captured images.
        The latter is saved in the folder "/gif" in the format: gif{number}.gif
        """
        if (os.path.exists('Project/package_table/temp/png'+str(self.nb_video))):
            folder = 'Project/package_table/temp/png' + str(self.nb_video)
            frame = []
            for i in range(self.nb_frame):
                frame.append(str(i) + ".png")
            files = [f"{folder}\{file}" for file in frame]
            images = [imageio.imread(file) for file in files]
            imageio.mimwrite('gif/gif'+ str(self.nb_video)+'.gif', images, fps=5)
            self.nb_video = self.nb_video + 1
            self.nb_frame = 0

    def destroy_root(self):
        """
        This method deletes all the files whose format is "/temp/png{number_video}". 
        Then, it destroys all the canvas and closes the window.
        """
        for i in range(self.nb_video):
            shutil.rmtree('Project/package_table/temp/png'+str(i))
        self.root.destroy()

    def create_table_window(self):
        """ 
        This method creates an another window which contains all the modular calculations of the current Canvas.
        This window is managed by a scrollbar.
        """
        self.state_button = False
        new_root = Tk()
        new_root.geometry("300x350")
        scrollbar = Scrollbar(new_root)
        scrollbar.pack(side='right', fill=Y)
        textbox = Text(new_root)
        textbox.pack()
        for i in range(self.modulo):
            textbox.insert(END, str(self.N)+" x " + str(i) + " modulo "+str(self.modulo) + " = " + str(round(self.N*i%self.modulo,2)) + "\n")
        textbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=textbox.yview)
        new_root.mainloop()

    def create_description(self):
        """ 
        This method creates an another window which contains a description of the different graphicals performances.
        """
        newWindow = Toplevel(self.root)
        text = Label(newWindow, text="Play/Pause : The buttom to play or stop the animation. \n  ")
        text.pack()
        text = Label(newWindow, text="Photo : Take pictures of the circle, at the moment to make the gif.\n  ")
        text.pack()
        text = Label(newWindow, text="Vidéo : Make a gif from the images captured.\n  ")
        text.pack()
        text = Label(newWindow, text="Table of : Open the multiplication table.\n  ")
        text.pack()
        text = Label(newWindow, text="Quit : To quit the interface. \n You should pass by there and quit it, to avoid errors .\n  ")
        text.pack()

    def motion_button(self):
        '''
        Provides a button control on the motion graphic and visual, to play or stop the animation.
        '''
        self.state_button = False
        button_play = Button(self.root, text="Play/Pause",
                             command=self.move_value)
        button_play.pack(padx=50, pady=5, side="top")
        button_photo = Button(self.root, text="Photo",
                              command=self.save_frame)
        button_photo.pack(padx=50, pady=5, side="top")
        button_video = Button(self.root, text="Vidéo",
                              command=self.save_video)
        button_video.pack(padx=50, pady=5, side="top")
        button_table_window = Button(self.root, text="Table of",
                                     command=self.create_table_window)
        button_table_window.pack(padx=50, pady=5, side="top")
        button_table_window = Button(self.root, text="Description",
                                     command=self.create_description)
        button_table_window.pack(padx=50, pady=5, side="top")
        quit = Button(self.root, text="Quit", fg="black",
                      command=self.destroy_root)
        quit.pack(padx=50, pady=5, side="bottom")
