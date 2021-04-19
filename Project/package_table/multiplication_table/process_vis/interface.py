from tkinter import Tk, Canvas, Scale
import multiplication_table as mt
import multiplication_table.process_vis.edges_vis as ev
import multiplication_table.process_vis.base_vis as bv

class Interface_gestion:

    def __init__(self):
        self.root = Tk()
        self.radius = 300
        self.N = 2
        self.modulo = 2
        self.center = (360, 360)
        self.graph = mt.Graph(self.N, self.modulo)
        self.cnv = Canvas(self.root, width=750, height=750, bg='ivory')
        self.cnv.pack(side="left", fill="both", expand=True)
        self.initalisation()
        self.user_IU()
        self.root.mainloop()


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
    
    def initalisation(self):
        bv.circle(self.cnv, self.center, self.radius)
        bv.dot(self.cnv, self.graph, self.radius, self.center[0])
        ev.Edge(self.cnv, self.graph, self.radius, self.center[0])

    # Coding the function with the "Scale" widget which allows the user to select a numeric value by moving  a cursor
    # button along a scale.
    def user_IU(self):
        table_cursor = Scale(self.root, label="Table of ...", font="Arial 15 bold",
                            orient="horizontal", command=self.table, from_=2, to=450,
                            length=250, resolution=0.01, repeatdelay=500)
        table_cursor.pack(pady=15)
        peak_cursor = Scale(self.root, label="Number of peaks", font="Arial 15 bold",
                            orient="horizontal", command=self.peak, from_=2,
                            to=200, length=250, repeatdelay=500)
        peak_cursor.pack(pady=5)