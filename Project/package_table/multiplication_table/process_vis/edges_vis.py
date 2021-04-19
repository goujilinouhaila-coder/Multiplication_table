import multiplication_table.process_vis.base_vis as bv


class Edge:

    def __init__(self, canvas, graph, radius, center, color_graph, edges_width ):
        self.edge_tab = self.all_edges(canvas, graph, radius, center, color_graph, edges_width)

    def all_edges(self, canvas, graph, radius, center, color_graph, edges_width):
        angle = bv.angle_tab(radius, graph)
        edges = [None]*graph.mod
        for i in range(0, graph.mod):
            edges[i] = self.one_edge(graph, canvas, i, angle, center, color_graph,edges_width)
        return edges

    def one_edge(self, graph, canvas, i, angle, center, color_graph,edges_width):
        j = int(graph.modulo_result(i)*100)
        xA, yA = angle[i*100]
        xB, yB = angle[j]
        A = bv.coord(center, center, xA, yA)
        B = bv.coord(center, center, xB, yB)
        return canvas.create_line(A, B, fill= color_graph, width= edges_width)

    def delete_one_edge(self, i, canvas, root):
        canvas.delete(root, self.edge_tab[i])
  
    def delete_all_edge(self, canvas, root):
        for i in range(len(self.edge_tab)):
            self.delete_one_edge(i, canvas, root)


