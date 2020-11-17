#Uses python3

import sys
import queue


def bfs(adj, s):
    vis = [False] * len(adj)
    q = queue.Queue()
    for elem in s:
        q.put(elem)
        
    while not q.empty():
        u = q.get()
        if vis[u]:
            continue
        else:
            vis[u] = True
            
        for v in adj[u]:
            if vis[v] == False:
                q.put(v)
    return vis


def shortet_paths(adj, cost, s, dist, reachable, shortest):
    #write your code here
    inf = float('inf')
    dist[s] = 0
    
    for _ in range(len(adj)-1):
        for u in range(len(adj)):
            for i in range(len(adj[u])):
                v = adj[u][i]
                if dist[v] > dist[u] + cost[u][i]:
                    dist[v] = dist[u] + cost[u][i]
                    #print("Node :", v+1, "from Node:", u+1)
    
    changed_list = []
    for u in range(len(adj)):
        for i in range(len(adj[u])):
            v = adj[u][i]
            if dist[v] > dist[u] + cost[u][i]:
                changed_list.append(v)
                dist[v] = dist[u] + cost[u][i]
                #print("Additional Node :", v+1, "from Node:", u+1)
                
    if len(changed_list):
        vis = bfs(adj, changed_list)
        for i in range(len(vis)):
            if vis[i] == True:
                shortest[i] = 0
    
    for i in range(len(reachable)):
        if shortest[i] == 0 or dist[i] != inf:
            reachable[i] = 1


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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

