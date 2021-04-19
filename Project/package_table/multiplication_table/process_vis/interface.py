from tkinter import Tk, Canvas, Scale, Button
import multiplication_table as mt
import multiplication_table.process_vis.edges_vis as ev
import multiplication_table.process_vis.base_vis as bv


class Interface_gestion:

    def __init__(self, speed, state_button):
        self.speed = speed
        self.window_init()
        self.graph_init()
        self.user_IU()
        if (state_button):
            self.motion_button()
        self.root.mainloop()

    def window_init(self):
        self.root = Tk()
        self.cnv = Canvas(self.root, width=750, height=750, bg='white')
        self.cnv.pack(side="left", fill="both", expand=True)

    def graph_init(self):
        self.radius = 300
        self.N = 2
        self.modulo = 2
        self.center = (360, 360)
        self.graph = mt.Graph(self.N, self.modulo)
        bv.circle(self.cnv, self.center, self.radius)
        bv.dot(self.cnv, self.graph, self.radius, self.center[0])
        ev.Edge(self.cnv, self.graph, self.radius, self.center[0])

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
        bv.circle(self.cnv, self.center, self.radius)
        bv.dot(self.cnv, self.graph, self.radius, self.center[0])
        ev.Edge(self.cnv, self.graph, self.radius, self.center[0])

    # Coding the function with the "Scale" widget which allows the user
    # to select a numeric value by moving  a cursor
    # button along a scale.
    def user_IU(self):
        self.table_cursor = Scale(self.root, label="Table of ...",
                                  font="Arial 15 bold", orient="horizontal",
                                  command=self.table, from_=2, to=400,
                                  length=250, resolution=0.01,
                                  repeatdelay=1000)
        self.table_cursor.pack(pady=5)
        self.peak_cursor = Scale(self.root, label="Number of peaks",
                                 font="Arial 15 bold", orient="horizontal",
                                 command=self.peak, from_=2, to=200,
                                 length=250, repeatdelay=500)
        self.peak_cursor.pack(pady=5)

    def move_value(self):
        self.state_button = not self.state_button
        while (self.state_button):
            self.table_cursor.set(self.table_cursor.get()+0.01)
            self.root.after(self.speed)
            self.root.update()

    def motion_button(self):
        self.state_button = False
        button_play = Button(self.root, text="Play/Pause",
                             command=self.move_value)
        button_play.pack(padx=50, pady=5)
