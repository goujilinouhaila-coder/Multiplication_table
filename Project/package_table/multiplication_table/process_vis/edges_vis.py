import multiplication_table.process_vis.base_vis as bv


def all_edges(canvas, graph, radius, center, color_graph, edges_width):
    """
    This function reiterates the :py:meth:`one_edge` function for every vertex i between 0 and the modulo number - 1.

    :param canvas: Canvas where edges will be created
    :param graph: Graph type object
    :param radius: Corresponds to the radius of the circle
    :type radius: int
    :param center: Center of the circle in the canvas
    :type center: int
    :param color_graph: It's about a table of colors of the circle frame
    :type color_graph: list of strings
    :param edges_width: The width of ridgs (edges)
    :type edges_width: float or int
    :return: Returns the  Canvas widget
    :rtype: tkinter.Canvas
    """
    angle = bv.angle_tab(radius, graph)
    col=0
    for i in range(0, graph.mod):
        one_edge(graph, canvas, i, angle, center,
                 color_graph[col], edges_width)
        col = (col+1)%len(color_graph)
    return canvas

def one_edge(graph, canvas, i, angle, center, color_graph, edges_width):
    """
    This function draws for any i fixed the edge between the vertex i and the vertex j whitch is given by the result
    of the modular calculate.
    
    :param i: Vertex i
    :type i: int
    :param j: Vertex j 
    :type j: int
    :param xA,yA: Coordinates of the first vertex
    :type xA,yA: int or float
    :param xB,yB: Coordinates of the second vertex
    :type xB,yB: int or float
    :return: Returns the  Canvas widget
    :rtype: tkinter.Canvas
    """
    j = int(graph.modulo_result(i)*100)
    xA, yA = angle[i*100]
    xB, yB = angle[j]
    A = bv.coord(center, center, xA, yA)
    B = bv.coord(center, center, xB, yB)
    canvas.create_line(A, B, fill=color_graph, width=edges_width)
    return canvas
