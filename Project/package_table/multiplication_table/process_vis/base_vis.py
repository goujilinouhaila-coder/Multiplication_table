import numpy as np


def circle(canvas, center, radius, state_circle, background_circle, outline_circle):
    """
    This function create a circle in the canvas.

    :param canvas: Canvas where the circle will be created
    :param center: Center of the circle in the canvas
    :type center: int
    :param radius: Corresponds to the radius of the circle
    :type radius: int
    :param state_circle: Displays the the frame of the circle if it takes True
    :type state_circle: boolean
    :param background_circle: Choice of the color for the circle's background
    :type background_circle: str
    :param outline_circle: Choice of the color for the circle's lines
    :type outline_circle: str
    """
    if (state_circle):
        xC, yC = center
        A = (xC-radius, yC-radius)
        B = (xC+radius, yC+radius)
        canvas.create_oval(A, B, width=2, fill=background_circle,
                           outline=outline_circle)


def coord(x, y, a, b):
    """
    Give the coordinnates of the new mark (interger numbers).

    :Example:
    \n
    >>> coord(200,200,40,60)
    (260,160)
    """
    return(x+b, y-a)


def angle_tab(radius, graph):
    """
    Returns a list of coordinnates which give the angle of each dots, they are proportionally spaced (angle : 2*pi/modulo number).

    :param radius: Radius of the circle
    :type radius: int
    :param graph: Graph type object
    :return: Returns a list of coordonnates which give the angle of each dots
    :rtype: list of float
    """
    t = (2*np.pi)/(graph.mod)
    angle = [None] * graph.mod*100
    for k in range(graph.mod*100):
        angle[k] = (radius*np.cos(k*t/100), radius*np.sin(k*t/100))
    return angle


def dot(canvas, graph, radius, center, color_graph, color_name):
    """
    Add the number of points needed on the cercle thanks to the :py:meth:`angle_tab` function.

    :param canvas: Canvas where the dots will be created
    :param graph: Graph type object
    :param radius: Corresponds to the radius of the circle
    :type radius: int
    :param center: Center of the circle in the canvas
    :type center: int
    :param color_graph: It's about a table of colors of the circle frame
    :type color_graph: list of strings
    :param color_name: Choice of the color for the numbers placed on the frame of the circle
    :type color_name: str
    """
    col=0
    if (graph.mod <= 150):
        angle = angle_tab(radius, graph)
        for j in np.arange(0, len(angle), 100):
            a, b = angle[j]
            A = coord(center-3, center-3, a, b)
            B = coord(center+3, center+3, a, b)
            # create modulo_number circles (R=3)
            canvas.create_oval(A, B, fill=color_graph[col])
            col = (col+1)%len(color_graph)
        name_peak(canvas, radius, graph, center, color_name)


def name_peak(cnv, radius, graph, center, color_name):
    """
    Add a number, for each dots, on the frame of the circle.

    :param cnv: Canvas where the numbers will be added
    :param radius: Corresponds to the radius of the circle
    :type radius: int 
    :param center: Center of the circle in the canvas
    :type center: int
    :param color_name: Choice of the color for the numbers placed on the frame of the circle
    :type color_name: str
    """
    angle = angle_tab(radius+17, graph)
    for j in np.arange(0, len(angle), 100):
        a, b = angle[j]
        Dots_C = (center+b, center-a)
        if (graph.mod <= 150):
            size = str(int(min(18, 16*62/graph.mod)))
            cnv.create_text(Dots_C, text=str(int(j/100)),
                            font="Arial " + size + " bold", fill=color_name)
