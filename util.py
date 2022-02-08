import random
import csv


class util:
    def __init__(self):
        pass

    def generateGraph(self, size, max):
        v = []
        for i in range(size):
            r = [0] * size
            for j in range(size):
                if j == i:
                    r[j] = 0
                elif j < i:
                    r[j] = v[j][i]
                else:
                    r[j] = random.randint(1, max)
            v.append(r)
        return v

    def generateGraphCSV(self, size, max):
        v = self.generateGraph(size, max)
        with open('graph.csv', 'w', newline='') as file:
            mywriter = csv.writer(file, delimiter=',')
            mywriter.writerows(v)

    def readCSV(self):
        v = []
        with open('graph.csv', 'r', newline='') as file:
            myreader = csv.reader(file, delimiter=',')
            for rows in myreader:
                v.append([int(i) for i in rows])
        return v