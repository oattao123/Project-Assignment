from SpanningTree import Graph1
g1 = Graph1(4)
g1.addEdge1(0, 1, 10)
g1.addEdge1(0, 2, 6)
g1.addEdge1(0, 3, 5)
g1.addEdge1(1, 3, 15)
g1.addEdge1(2, 3, 4)
g1.KruskalMST()

