# Time complexity: O(ElogE) or O(ElogV)

class Graph:
    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = []

    def addEdge(self, u, v, wt):
        self.graph.append([u,v,wt])

    # Implement DisJointSet Data structure
    def findParent(self,node, parent):
        if node == parent[node]:
            return node

        parent[node] = self.findParent(parent[node], parent)
        return parent[node]

    def union(self, parent, rank, u, v):
        # find parent of both node u and v
        u = self.findParent(u, parent)
        v = self.findParent(v, parent)

        if rank[u] < rank[v]:
            parent[u] = v
        elif rank[u] > rank[v]:
            parent[v] = u
        else:
            parent[v] = u
            rank[u] += 1
        
    def KruskalMST(self):
        result = []

        # Initiating an index variable for sorted edges.
        i = 0
        # Initiating an index variable for result array.
        e = 0

        # Step-1: Sort all the edges in decending order of their weight. If we are not allowed to change the given graph, we can create a copy of graph.
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = [i for i in range(self.V)]
        rank = [0]* self.V

        # Number of edges to be taken is equal to V-1.
        while e < self.V-1:
            # Step-2: Pick the smallest edge and increment the index for next iteration.
            u,v,wt = self.graph[i]
            i += 1
            u_root = self.findParent(u, parent)
            v_root = self.findParent(v, parent)

            # If including this edge doesn't create cycle, include it in result and increment the index of result arr for next edge.
            if u_root != v_root:
                e += 1
                result.append([u, v, wt])
                self.union(parent, rank, u_root, v_root)
            # Else discard the edge.

        return result