#Uses python3
import sys
import math

class DisjointSet:
    def __init__ (self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]
        
    def find(self, x):
        if (self.parent[x] != x):
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xset = self.find(x)
        yset = self.find(y)
        
        if xset == yset:
            return
        
        if self.rank[x] < self.rank[y]:
            self.parent[xset] = yset
        elif self.rank[y] < self.rank[x]:
            self.parent[yset] = xset
        else:
            self.parent[yset] = xset
            self.rank[xset] += 1
            

def dist(x1, y1, x2, y2):
    return math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2))


def clustering(x, y, k):
    #write your code here
    n = len(x)
    edges = [0] * ((n * (n - 1)) // 2)
    idx = 0
    for i in range(n-1):
        for j in range(n-1-i):
            edges[idx] = (dist(x[i], y[i], x[j+i+1], y[j+i+1]), i, j+i+1)
            idx += 1
    
    ds = DisjointSet(n)
    unique_sets = n
    retflag = False
    if unique_sets == k:
        retflag = True
    edges = sorted(edges)
    for obj in edges:
        if ds.find(obj[1]) != ds.find(obj[2]):
            if retflag:
                return obj[0]
            ds.union(obj[1], obj[2])
            unique_sets -= 1
            if unique_sets == k:
                retflag = True
                

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
