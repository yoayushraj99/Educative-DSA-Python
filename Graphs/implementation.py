from typing import *

class Graph:
    def __init__(self):
        adj: Dict[int, List[int]] = {}

    def addEdge(self, u, v, direction: bool):
        # Direction = 0 -> undirected
        # Direction = 1 -> Directed graphs
        adj = self.adj
        # Create an edge from u to v
        adj[u].append(v)
        if direction == 0:
            adj[v].append(u)

    def printAdjList(self):
        for i, j in self.adj.items():
            print(i, end="-> ")
            for k in j:
                print(k, end=", ")
            print()


    