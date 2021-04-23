import numpy as np
from scipy import sparse
from scipy.sparse import isspmatrix
import numpy as np 
import time 

class Graph:
    """
    Graph class is used to contain the related specifications to the modular multiplication and create the associated undirected graph in the console.
        
    :param N: Corresponds to the multiplication table assigned by the user. This number is rounded to :math:`10^{-2}`
    :type N: float
    :param mod: Corresponds to the modulo number entered by the user
    :type mod: int
    :param M: Symmetric adjacency matrix used to represent the graph. This dimension of this matrix is (mod*100, mod*100) whose non-diagonal element :math:`m_{ij}` corresponds to an edge between vertex i and vertex j
    :type M: numpy
    """

    def __init__(self, table_number, modulo_number):
        """
        Constructor method. This method instantiates an empty graph.
        """
        self.N = round(float(table_number),2)
        self.mod = int(modulo_number)   
        self.M = np.full((self.mod*100, self.mod*100), 0) 

    def print_matrix(self):
        """
        Displays the adjacency matrix.
        """
        print(self.M)

    def modulo_result(self, i):
        """
        Returns the result of the modular multiplication. 

        :param i: Vertex i
        :type i: int
        :return: Returns the result of the modular multiplication
        :rtype: float

        :Example:

            For N=2, i=7 and mod=10 \n
            >>> modulo_result(2,10,7) 
            4
        """
        return (self.N * int(i)) % self.mod

    def print_graph(self):
        """
        Displays in a textual format all the vertices, each one of them is accompanied by all the edges incident to it. 
        """
        for i in range(len(self.M.row)):
            print(self.M.row[i], "<--->", self.M.col[i]/100)

    def sparse_matrix(self):
        """ 
        Fill the adjacency sparse matrix from the results of the modular multiplication.   
        """
        start = time.time()
        val = [1]*self.mod
        row = np.array(range(self.mod))
        col = np.zeros(self.mod)
        for i in range(self.mod):
            col[i] = self.modulo_result(i)*100

        self.M = sparse.coo_matrix((val[1:],(row[1:],col[1:])), shape = (self.mod*100, self.mod*100))
        end = time.time()



