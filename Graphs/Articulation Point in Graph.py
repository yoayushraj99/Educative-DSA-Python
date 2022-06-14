# Time Complexity: O(V+E)
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.timer = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    '''A recursive function that find articulation points
    using DFS traversal
    low --> Store the lowest possible time to reach the node.
    visited[] --> keeps track of visited vertices
    disc[] --> Stores discovery times of visited vertices
    parent[] --> Stores parent vertices in DFS tree
    ap[] --> Store articulation points'''
    def findAP(self, node, parent, disc, low, visited, ap):
        visited[node] = True
        low[node] = disc[node] = self.timer
        self.timer += 1
        child = 0

        for neighbour in self.graph[node]:
            if neighbour == parent:
                continue
            # If neighbour is not visited yet, then make it a child of node in DFS tree and recur for it.
            if not visited[neighbour]:
                self.findAP(neighbour,node, disc, low, visited, ap)
                low[node] = min(low[node], low[neighbour])

                # Check AP or not
                if low[neighbour] >= disc[node] and parent != -1:
                    ap.append(node)
                child += 1
            else:
                low[node] = min(low[node], disc[neighbour])

        if parent == -1 and child > 1:
            ap.append(node)



    def AP(self):
        visited = [False] * self.V
        disc = [-1]*self.V
        low = [-1]*self.V
        parent = -1
        ap = []

        for i in range(self.V):
            if not visited[i]:
                self.findAP(i, parent, disc, low, visited, ap)

        return ap