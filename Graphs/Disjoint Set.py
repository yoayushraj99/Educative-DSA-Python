class DisJointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def findParent(self, node):
        # If node is the parent of itself then return the node.
        if node == self.parent[node]:
            return node
        # Else find and store the parent of the node and then return it.
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        # Find the parent of the node u and node v.
        u = self.findParent(u)
        v = self.findParent(v)

        # If rank[u] < rank[v], then attach node u to v
        if self.rank[u] < self.rank[v]:
            self.parent[u] = v
        # else if rank[u] > rank[v], then attach node v to u
        elif self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            # else if rank[u] == rank[v], then attach any node to the other node.
            self.parent[v] = u
            # When we attach same rank nodes then the height of the tree increases that's why we need to increase the rank by 1 of u.
            self.rank[u] += 1


obj = DisJointSet(5)
obj.union(0, 2)
obj.union(4, 2)
obj.union(3, 1)
if obj.findParent(4) == obj.findParent(0):
    print('Yes')
else:
    print('No')
if obj.findParent(1) == obj.findParent(0):
    print('Yes')
else:
    print('No')