import numpy as np
import math

class Graph:
    def __init__(self, table_number, modulo_number):
        self.N = table_number
        self.mod = modulo_number     
        self.M = np.full((self.mod, self.mod),0) 

    def print_matrix(self):
        print(self.M)

    def add_edge(self, i, j):
        self.M[i, j] = 1 
        self.M[j, i] = 1
    
    def create_matrix(self):
        for i in range(self.mod):
            j = (self.N*i) % self.mod
            self.add_edge(i, j)
    
    def print_graph(self):
        index = np.where(np.triu(self.M,1)==1) 
        for i in range(len(index[0])):
            print(index[0][i],"<--->", index[1][i]) 
    