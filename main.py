class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.size = len(vertices)

    def findMin(self, E):
        minVal = E[0]
        for i in range(len(E)):
            if E[i][2] < minVal[2]:
                minVal = E[i]
        return minVal

    def MST_Process(self):
        MST = [False] * self.size
        L = []
        E = []
        for i in range(self.size):
            if i == 0:
                MST[0] = True
            else:
                for j in range(len(MST)):
                    for k in range(j, len(MST)):
                        if MST[j] != MST[k]:
                            E.append([j, k, self.V[j][k]])
                edge = self.findMin(E)
                L.append(edge)
                MST[edge[0]] = True
                MST[edge[1]] = True
                E = []
        print(L)


g = Graph([
    [0, 2,  6,  12],
    [2, 0,  10, 5],
    [6, 10, 0,  4],
    [12,5,  4,  0]
])
g.MST_Process()
