#Uses python3

import sys
import queue

def bipartite(adj):
    #write your code here
    col = [-1] * len(adj)
    for s in range(len(adj)):
        if col[s] != -1:
            continue
        col[s] = 0
        q = queue.Queue()
        q.put(s)
        while not q.empty():
            u = q.get()
            for v in adj[u]:
                if col[v] == col[u]:
                    return 0
                if col[v] == -1:
                    col[v] = (col[u] + 1) % 2
                    q.put(v)

    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))