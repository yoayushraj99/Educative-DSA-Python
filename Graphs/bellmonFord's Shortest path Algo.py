def bellmonFord(n, m, src, dest, adj): # n -> no. of nodes, m -> no. of edges, adj-> adjacency list
    dist = [float('inf')]*(n+1)
    dist[src] = 0

    for _ in range(1, n+1):
        #traverse on edge list
        for j in range(m):
            u, v, wt = adj[j]

            if dist[u] != float('inf') and dist[u]+wt < dist[v]:
                dist[v] = dist[u] + wt

    flag = 0
    for j in range(m):
        u = adj[j][0]
        v = adj[j][1]
        wt = adj[j][2]

        if dist[u] != float('inf') and dist[u]+wt < dist[v]:
            flag = 1

    if flag == 0:
        return dist[dest]
    return -1