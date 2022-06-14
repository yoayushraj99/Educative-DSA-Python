'''A directed graph is said to be strongly connected if every vertex is reachable from every other vertex. The strongly connected components of a graph are the subgraphs which are themselves strongly connected.'''

# Time Complexity: O(V+E)

from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    # Add edge Function
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, node, vis):
        # Mark the current node as visited
        vis[node] = True
        #Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[node]:
            if not vis[neighbour]:
                self.dfs(neighbour, vis)
    
    def fillOrder(self, node, vis, st):
        vis[node] = True
        for neighbour in self.graph[node]:
            if not vis[neighbour]:
                self.dfs(neighbour, node, st)
        st.append(node)

    # Function that returns reverse(or transpose) of this graph
    def getTranspose(self):
        g = Graph(self.V)

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)

        return g

    def stronglyConnectedComponents(self):
        # Topo Sort 
        stack = []
        visited = [False]*self.V
        for i in range(self.V):
            if not visited[i]:
                self.fillOrder(i, visited, stack)

        # Create a transpose graph
        transpose = self.getTranspose()

        visited = [False]* self.V

        # Now process all vertices in order defined in stack
        count = 0
        while stack:
            i = stack.pop()
            if not visited[i]:
                count += 1
                transpose.dfs(i, visited)

        return count