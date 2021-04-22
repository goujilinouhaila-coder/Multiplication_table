import multiplication_table.process_vis.base_vis as bv


def all_edges(canvas, graph, radius, center, color_graph, edges_width):
    """
    This function takes:
     -six parameters:
       canvas: display object
       graph: it's the graphic
       radius: it's the radius of the circle
       center: it's the center of the circle
       color_graph: for coloring the graph
       edges_width: the width of edges. Can be int or float
     -two global variables:
       angle and col
    And call the second function
    """
    angle = bv.angle_tab(radius, graph)
    col=0
    for i in range(0, graph.mod):
        one_edge(graph, canvas, i, angle, center,
                 color_graph[col], edges_width)
        col=(col+1)%len(color_graph)


def one_edge(graph, canvas, i, angle, center, color_graph, edges_width):
    """
    This function draws for any i fixed the edges between i and the result
    of the modular calculate ( N*i modulo mod)
    
    :param i: fixed
    :type i: int
    :param j: modular calculate
    :type j: int
    :param xA, yA: angle
    :type xA, yA: int
    :param xB, yB: angle
    :type xB, yB: int
    """
    j = int(graph.modulo_result(i)*100)
    xA, yA = angle[i*100]
    xB, yB = angle[j]
    A = bv.coord(center, center, xA, yA)
    B = bv.coord(center, center, xB, yB)
    canvas.create_line(A, B, fill=color_graph, width=edges_width)

