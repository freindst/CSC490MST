import csv
import timeit


def parent(i):
    return (i - 1) // 2


class MinHeap:
    def __init__(self):
        self.size = 0
        self.arr = []   #two elements, [vertice, weight]
        self.pos = {}   #list[vertice, index]

    def swap(self, i, j):
        pos_i = self.arr[i][0]
        pos_j = self.arr[j][0]
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.pos[pos_i] = j
        self.pos[pos_j] = i

    def heapify(self, i):
        if i < 0:
            return

        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.size and self.arr[smallest][1] > self.arr[left][1]:
            smallest = left

        if right < self.size and self.arr[smallest][1] > self.arr[right][1]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.heapify(smallest)

    def heapifyTraverse(self, k):
        i = parent(k)

        if i < 0:
            return

        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < self.size and self.arr[smallest][1] > self.arr[left][1]:
            smallest = left

        if right < self.size and self.arr[smallest][1] > self.arr[right][1]:
            smallest = right

        if smallest != i:
            self.swap(i, smallest)
            self.heapifyTraverse(smallest)

    def heappush(self, v, l):
        self.arr.append([v, l])
        self.pos[v] = self.size
        self.size = self.size + 1
        self.heapifyTraverse(self.size - 1)

    def getMin(self):
        return self.arr[0]

    def extrudeMin(self):
        if self.size == 0:
            return

        root = self.arr[0]
        lastNode = self.arr[self.size - 1]

        self.arr[0] = lastNode
        self.pos[lastNode[0]] = 0
        self.pos[root[0]] = self.size - 1
        self.size = self.size - 1

        self.heapify(0)
        return root

    def decreaseKey(self, v, l):
        self.arr[self.pos[v]][1] = l
        self.heapifyTraverse(self.pos[v])

    def isInMinHeap(self, v):
        if self.pos[v] < self.size:
            return True
        return False


class Graph:
    def __init__(self):
        self.V = []

    def importGraph(self, v):
        self.V = v

    def process(self):
        degree = len(self.V)
        MST = []
        E = MinHeap()

        currentNode = [0, 0]
        MST.append(currentNode)

        for i in range(1, degree):
            if i == 1:
                for j in range(1, degree):
                    E.heappush(j, self.V[0][j])
            else:
                lastVertice = currentNode[0]
                for j in range(1, degree):
                    if E.isInMinHeap(j):
                        if E.arr[E.pos[j]][1] > self.V[lastVertice][j]:
                            E.decreaseKey(j, self.V[lastVertice][j])
            currentNode = E.extrudeMin()
            MST.append(currentNode)

        totalLength = 0
        last = 0
        for p in MST:
            if p[0] != 0:
                totalLength = totalLength + p[1]
                print(last, " - ", p[0])
                last = p[0]
        print("Total distance of Minimum Spanning Tree is: ", totalLength)

def readCSV(filename):
    v = []
    with open(filename, 'r', newline='') as file:
        myreader = csv.reader(file, delimiter=',')
        for rows in myreader:
            v.append([int(i) for i in rows])
    return v

g = readCSV('graph.csv')
graph = Graph()
graph.importGraph(g)
# graph.process()
print(timeit.Timer(graph.process).repeat(number=1))