#Uses python3

import sys


def negative_cycle(adj, cost):
    #write your code here
    inf = 10**7 + 1
    dist = [inf] * len(adj)
    
    for _ in range(len(adj)-1):
        for u in range(len(adj)):
            for i in range(len(adj[u])):
                v = adj[u][i]
                curcost = cost[u][i]
                if dist[v] > dist[u] + curcost:
                    dist[v] = dist[u] + curcost
    
    flag_changed = 0
    for u in range(len(adj)):
        for i in range(len(adj[u])):
            v = adj[u][i]
            curcost = cost[u][i]
            if dist[v] > dist[u] + curcost:
                flag_changed = 1
                dist[v] = dist[u] + curcost
    return flag_changed


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
