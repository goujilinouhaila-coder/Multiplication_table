import numpy as np


class Graph:
    def __init__(self, table_number, modulo_number):
        self.N = table_number
        self.mod = int(modulo_number)   
        self.M = np.full((self.mod*100, self.mod*100), 0) 

    def print_matrix(self):
        print(self.M)

    def add_edge(self, i, j):
        self.M[i, j] = 1
        self.M[j, i] = 1

    def create_matrix(self):
        for i in np.arange(0, self.mod, 1):
            self.add_edge(int(i*100), int(self.modulo_result(i)*100))

    def modulo_result(self, i):
        return (self.N * i) % self.mod

    def print_graph(self):
        index = np.where(np.triu(self.M, 1) == 1)
        for i in range(len(index[0])):
            print(index[0][i]/100, "<--->", index[1][i]/100)
