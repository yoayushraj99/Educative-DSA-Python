''' 
	Time complexity: O(V + E). 
	Space complexity: O(V^2). 

	Where V is the number of vertices in the input graph and 
    E is the number of edges in the input graph.
'''

from collections import deque, defaultdict


def prepareAdjList(adjList, edges):
    for i in range(len(edges)):
        u = edges[i][0]
        v = edges[i][1]

        adjList[u].append(v)
        adjList[v].append(u)


def bfs(adjList, visited, ans, node):
    q = deque()
    q.append(node)
    visited[node] = 1

    while q:
        frontNode = q.popleft()

        # Store frontNode into ans
        ans.append(frontNode)
        # traverse all neighbours of frontNode
        for i in adjList[frontNode]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1


def BFS(vertex, edges):
    # Write your solution here
    # 'vertex' is the number of vertices present in the graph
    # 'edges' is a matrix of the set of edges between two given vertices in the graph
    adjList = defaultdict(list)
    ans = []
    visited = defaultdict(bool)

    prepareAdjList(adjList, edges)

    # Traverse all components of graph
    for i in range(vertex):
        if not visited[i]:
            bfs(adjList, visited, ans, i)

    return ans


print(BFS(9, [[0,8],[1,6],[1,7],[1,8],[5,8],[6,0], [7,3],[7,4],[8,7],[2,5]
]))