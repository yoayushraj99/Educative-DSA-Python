# Time Complexity: O(V+E)

from collections import defaultdict

# This graph represents undirected graph using adjacency list representation.
class Graph:
    def __init__(self, vertices: int):
        self.V = vertices # No. of vertices
        self.graph = defaultdict(list)
        self.time = 0
        self.result = []

    # Function to add an edge to a graph.
    def add_edge(self,u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    '''A recursive function that finds and prints bridges
    using DFS traversal
    low --> Store the lowest possible time to reach the node.
    visited[] --> keeps track of visited vertices
    disc[] --> Stores discovery times of visited vertices
    parent[] --> Stores parent vertices in DFS tree'''

    def findBridges(self, node, parent, disc, low, visited):
        visited[node] = True
        disc[node] = low[node] = self.time
        self.time += 1

        for neighbour in self.graph[node]:
            if neighbour == parent[node]:
                continue
            # If neighbour is not visited yet, then make it a child of node in DFS tree and recur for it.
            if not visited[neighbour]:
                self.findBridges(neighbour, node, disc, low, visited)
                # Check if the subtree rooted with neighbour has a connection to one of the ancestors of node.
                low[node] = min(low[node], low[neighbour])

                # Check edge is bridge
                if low[neighbour] > disc[node]:
                    ans = []
                    ans.append(node)
                    ans.append(neighbour)
                    self.result.append(ans)
            else:
                # Back-Edge
                # Update low value of u for parent function calls.
                low[node] = min(low[node], disc[neighbour])



    def bridge(self):
        visited = [False] * self.V
        disc = [-1]*self.V
        low = [-1]*self.V
        parent = -1

        # Dfs
        for i in range(self.V):
            if not visited[i]:
                self.findBridge(i, parent, disc, low, visited)

        return self.result