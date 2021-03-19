import numpy as np 
import math

class Graph: 

    def __init__(self, table_number, modulo_number):
        self.N = table_number
        self.mod = modulo_number
        self.M = np.full((self.N,self.N), 0)

    def print_matrix(self):
        print(self.M)

    def add_edge(self, i, j):
        self.M[i,j] = 1
        self.M[j,i] = 1

    def print_graph(self):
        for i in range(self.N):
            for j in range(i, self.N):
                if (self.M[i,j]==1):
                    print(i, "<--->", j) 
