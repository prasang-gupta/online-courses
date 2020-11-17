#Uses python3

import sys
import numpy as np

sys.setrecursionlimit(200000)

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

def explore_simple(x, adj, visited_new):
    visited_new[x] = True
    for nb in adj[x]:
        if not visited_new[nb]:
            explore_simple(nb, adj, visited_new)

def dfs(adj, order):
    #write your code here
    for v in range(len(adj)):
        if not visited[v]:
            explore(v, adj, order)

def reverse_graph(adj):
    rev_adj = [[] for _ in range(len(adj))]
    for source in range(len(adj)):
        for sink in adj[source]:
            rev_adj[sink].append(source)
    return rev_adj

def number_of_strongly_connected_components(adj):
    #write your code here
    order = [0] * n
    rev_adj = reverse_graph(adj)
    dfs(rev_adj, order)
    order = np.array(order)
    order_idx = list(np.argsort(order))
    order_idx.reverse()

    visited_new = [False for _ in range(len(adj))]
    result = 0
    for v in order_idx:
        if not visited_new[v]:
            result += 1
            explore_simple(v, adj, visited_new)
    return result

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
    print(number_of_strongly_connected_components(adj))
