#Uses python3

import sys

visited = []
def explore(x, adj, chain):
    visited[x] = True
    for nb in adj[x]:
        if visited[nb] and nb in chain:
            return 1
        if not visited[nb]:
            new_chain = chain.copy() + [nb]
            if explore(nb, adj, new_chain) == 1:
                return 1
    return 0

def acyclic(adj):
    for v in range(len(adj)):
        if not visited[v]:
            chain = [v]
            if explore(v, adj, chain.copy()) == 1:
                return 1
    return 0

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
    print(acyclic(adj))
