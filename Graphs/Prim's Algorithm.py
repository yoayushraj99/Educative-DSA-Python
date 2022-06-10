from collections import defaultdict
import heapq

def prims(graph, N): #  N -> No. of vertices
    adj = defaultdict(list)
    for i in range(N-1):
        u = graph[i][0]
        v = graph[i][1]
        wt = graph[i][2]

        adj[u].append((v, wt))
        adj[v].append((u, wt))

    parent = [-1]*N
    key = [float('inf')]*N
    key[0] = 0
    pq = []
    heapq.heappush(pq, (0, 0))

    mstSet = [False]*N

    for i in range(N):
        minIndex, _ = heapq.heappop(pq)

        mstSet[minIndex] = True

        for neighbour in adj[u]:
            v, weight = neighbour
            if mstSet[v] == False and weight < key[v]:
                parent[v] = u
                heapq.heappush(pq, (v, key[v]))
                key[v] = weight

    for i in range(1, v):
        print(f'{parent[i]} - {i}')