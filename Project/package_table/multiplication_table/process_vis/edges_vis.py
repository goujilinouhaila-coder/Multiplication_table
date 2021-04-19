import multiplication_table.process_vis.base_vis as bv


def all_edges(canvas, graph, radius, center):
    angle = bv.angle_tab(radius, graph)
    for i in range(0, graph.mod):
        one_edge(graph, canvas, i, angle, center)


def one_edge(graph, canvas, i, angle, center):
    j = int(graph.modulo_result(i)*100)
    xA, yA = angle[i*100]
    xB, yB = angle[j]
    A = bv.coord(center, center, xA, yA)
    B = bv.coord(center, center, xB, yB)
    return canvas.create_line(A, B, fill='black', width=2)
