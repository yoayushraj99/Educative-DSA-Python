from collections import defaultdict

def createAdjList(adjList, size, edges):
    for i in range(size):
        u,v = edges[i]

        adjList[u].append(v)
        adjList[v].append(u)

def dfs(adjList, visited,component, node):
    component.append(node)
    visited[node] = 1

    # For every connected node a recursive call with be executed
    for i in adjList[node]:
        if not visited[i]:
            dfs(adjList, visited, component, i)

def depthFirstSearch(V, E, edges):
    # write your code here
    adjList = defaultdict(list)
    ans = []
    visited = defaultdict(bool)

    # Prepare adjList
    createAdjList(adjList, E, list(edges))

    for i in range(V):
        if not visited[i]:
            component = []
            dfs(adjList, visited, component, i)
            ans.append(component)
    for j in ans:
        j.sort()
    return ans

print(depthFirstSearch(4, 4, [[0,1],
[0,3], [1,2], [2,3]
]))