from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
    def print_graph(self):
        for i in range(self.v):
            for j in range(self.v):
                print(self.edges[i][j], end=" ")
            print()
    def dijkstra(self, source):
        
        # Create a priority queue to store vertices that
        # are being preprocessed. This is weird syntax in
        # Python. Refer below link for details of this syntax
        # https://www.geeksforgeeks.org/priority-queue-in-python/
        pq = PriorityQueue()
        
        # Create a vector for distances and initialize all
        # distances as infinite (INF)
        dist = [float("Inf")] * self.v
        
        # Insert source itself in priority queue and initialize
        # its distance as 0.
        pq.put((0, source))
        dist[source] = 0
        
        while not pq.empty():
            
            # The first vertex in pair is the minimum distance
            # vertex, extract it from priority queue.
            # vertex label is stored in second of pair (it
            # has to be done this way to keep the vertices
            # sorted distance (distance must be first item
            # in pair)
            u = pq.get()[1]
            
            # 'i' is used to get all adjacent vertices of a vertex
            for i in range(self.v):
                if self.edges[u][i] > 0:
                    if dist[i] > dist[u] + self.edges[u][i]:
                        dist[i] = dist[u] + self.edges[u][i]
                        pq.put((dist[i], i))
        self.print_solution(dist)
    def print_solution(self, dist):
        print("Vertex \tDistance from Source")
        for i in range(self.v):
            print(i, "\t", dist[i])

