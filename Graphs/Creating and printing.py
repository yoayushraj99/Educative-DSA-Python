# Problem Statement
# You are given an undirected graph of 'N' nodes and 'M' edges. Your task is to create the graph and 
# print the adjacency list of the graph. It is guaranteed that all the edges are unique, i.e., 
# if there is an edge from 'X' to 'Y', then there is no edge present from 'Y' to 'X' and vice versa.
# Also, there are no self-loops present in the graph.
# In graph theory, an adjacency list is a collection of unordered lists used to represent a finite graph. 
# Each list describes the set of neighbors of a vertex in the graph.

# For Example:
# If 'N' = 3 and edges = {{2,1}, {2,0}}.

# So, the adjacency list of the graph is stated below.
# 0 → 2
# 1 → 2
# 2 → 0 → 1

'''
    Time Complexity : O(N + M)
    Space Complexity : O(N + M)

    Where 'N' and 'M' denote the number of nodes and the number of edges in the graph.
'''

def printAdjacency(n, m, edges):
    
    graph = [[] for i in range(n)]

    # Creating the graph.
    for i in range(m):

        # Adding adjecent nodes.
        graph[edges[i][0]].append(edges[i][1])
        graph[edges[i][1]].append(edges[i][0])

    # Create an adjacency list of size 'N'.
    adjacencyList = [[] for i in range(n)]

    for i in range(n):
        adjacencyList[i].append(i)

        for j in graph[i]:
            adjacencyList[i].append(j)

    return adjacencyList