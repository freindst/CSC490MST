def parent(i):
    return (i - 1) // 2


class MinHeap:
    def __init__(self):
        self.n = 0
        self.arr = []
        self.pos = {}

    def heapify(self, i):
        if i < 0:
            return

        smallest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < self.n and self.arr[smallest] > self.arr[l]:
            smallest = l

        if r < self.n and self.arr[smallest] > self.arr[r]:
            smallest = r

        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.heapify(parent(i))

    def heappush(self, v, l):
        self.arr.append(l)
        self.pos[v] = self.n
        self.n = self.n + 1
        self.heapify(parent(self.n - 1))

    def getMin(self):
        return self.arr[0]