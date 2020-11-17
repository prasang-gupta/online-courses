#Uses python3

import sys
import numpy as np

visited = []
clock = [0]

def explore(x, adj, order):
    visited[x] = True
    clock[0] += 1
    for nb in adj[x]:
        if not visited[nb]:
            explore(nb, adj, order)
    order[x] = clock[0]
    clock[0] += 1

def dfs(adj, order):
    #write your code here
    for v in range(len(adj)):
        if not visited[v]:
            explore(v, adj, order)

def toposort(adj):
    order = [0] * n
    #write your code here
    dfs(adj, order)
    order = np.array(order)
    order_idx = list(np.argsort(order))
    order_idx.reverse()
    return order_idx

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    visited = [False for _ in range(n)]
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

