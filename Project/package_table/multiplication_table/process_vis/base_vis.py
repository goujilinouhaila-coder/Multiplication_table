import numpy as np


def circle(canvas, center, radius, state_circle, background_circle, outline_circle):
    # Create a circle of radius R in the canvas
    if (state_circle):
        xC, yC = center
        A = (xC-radius, yC-radius)
        B = (xC+radius, yC+radius)
        canvas.create_oval(A, B, width=2, fill=background_circle,
                           outline=outline_circle)


def coord(x, y, a, b):
    return(x+b, y-a)


def angle_tab(radius, graph):
    t = (2*np.pi)/(graph.mod)
    angle = [None] * graph.mod*100
    for k in range(graph.mod*100):
        angle[k] = (radius*np.cos(k*t/100), radius*np.sin(k*t/100))
        # angle for the dots (modulo_number)
    return angle


def dot(canvas, graph, radius, center, color_graph, color_name):
    # Add the number of points needed on the cercle, they are proportionally
    # spaced (angle : 2pi/modulo_number)
    if (graph.mod <= 150):
        angle = angle_tab(radius, graph)
        for j in np.arange(0, len(angle), 100):
            a, b = angle[j]
            A = coord(center-3, center-3, a, b)
            B = coord(center+3, center+3, a, b)
            # create modulo_number circles (R=3)
            canvas.create_oval(A, B, fill=color_graph)
        name_peak(canvas, radius, graph, center, color_name)


def name_peak(cnv, radius, graph, center, color_name):
    angle = angle_tab(radius+17, graph)
    for j in np.arange(0, len(angle), 100):
        a, b = angle[j]
        Dots_C = (center+b, center-a)
        if (graph.mod <= 150):
            size = str(int(min(18, 16*62/graph.mod)))
            cnv.create_text(Dots_C, text=str(int(j/100)),
                            font="Arial " + size + " bold", fill=color_name)
