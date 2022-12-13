from DBFS import Graph
g1 = Graph()
g1.addEdge2(0, 1)
g1.addEdge2(0, 2)
g1.addEdge2(1, 2)
g1.addEdge2(2, 0)
g1.addEdge2(2, 3)
g1.addEdge2(3, 3)
g1.BFS(2)