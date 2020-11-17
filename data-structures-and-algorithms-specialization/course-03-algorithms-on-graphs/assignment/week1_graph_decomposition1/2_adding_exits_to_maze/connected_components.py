#Uses python3

import sys

visited = []
def explore(x, adj):
    visited[x] = True
    for nb in adj[x]:
        if not visited[nb]:
            explore(nb, adj)

def number_of_components(adj):
    result = 0
    #write your code here
    for v in range(len(adj)):
        if not visited[v]:
            explore(v, adj)
            result += 1
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
        adj[b - 1].append(a - 1)
    visited = [False for _ in range(n)]
    print(number_of_components(adj))
