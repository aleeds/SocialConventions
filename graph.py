# will have a class graph with methods:
#   GetConnectivity

# Additionally, this file will have methods for creating scale free, random, and
#   small world grpahs.
import random
import numpy

class Graph:
    def __init__(self,mat):
        self.matrix = mat
    def GetRandomNeighbor(self,i):
        neighbors = self.matrix[i]
        i = random.randint(0,len(neighbors) - 1)
        t = neighbors[i]
        while t == 0:
            i = random.randint(0,len(neighbors) - 1)
            t = neighbors[i]
        return i

    def FloydWarshall(self):
        matrix = self.matrix.copy()

        (n,m) = matrix.shape
        for i in range(0,n):
            for j in range(0,n):
                if matrix[i][j] == 0: matrix[i][j] = 100000000
        for k in range(0,n):
            for i in range(0,n):
                for j in range(0,n):
                    matrix[i][j] = min(matrix[i][j],matrix[i][k] + matrix[k][j])

        return matrix


    def GetConnectivity(self):
        matrix  = self.FloydWarshall()
        s = 0
        (n,m) = matrix.shape
        for i in range(0,n):
            for j in range(0,n):
                s += matrix[i][j]

        return 1 / (s / (n * n))

# k > n
def BuildScaleFree(n,k):
    mat = numpy.zeros((n,n))
    ls = [0 for i in range(0,n)]
    mat[0][1] = 1
    ls[0] = 1
    ls[1] = 1
    for i in range(0,k):
        c = sum(ls)
        v = random.randint(0,n - 1)
        p = random.randint(0,c - 1)
        j = ls[0]
        ne = 0
        while j < p:
            j += ls[ne + 1]
            ne += 1
            if ne > n:
                ne = n - 1
                break
        mat[v][ne] = 1
        mat[ne][v] = 1
        ls[v] += 1
        ls[ne] += 1
    return Graph(mat)




def Test():
    mat = numpy.zeros((4,4))
    mat[0][1] = 1
    mat[0][2] = 1
    mat[0][3] = 1

    mat[1][0] = 1
    mat[1][2] = 1

    mat[2][0] = 1
    mat[2][1] = 1

    mat[3][0] = 1
    g = Graph(mat)
    print(g.GetConnectivity())
