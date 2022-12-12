from queue import PriorityQueue

class Graph:
    def __init__(self, num_of_vertices): #กำหนดจำนวนจุดยอด
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    def add_edge(self, u, v, weight): #กำหนดต่าในกราฟ มีจุดยอดหนึ่งไปอีกจุดยอดหนึ่ง มีความยาวเท่าไร
        self.edges[u][v] = weight
        self.edges[v][u] = weight
    def print_graph(self): #ใส่ต่าของแต่ละจุดในกราฟ
        for i in range(self.v):
            for j in range(self.v):
                print(self.edges[i][j], end=" ")
            print()
                
    def dijkstra(self, source):        
        pq = PriorityQueue()        
        dist = [float("Inf")] * self.v
        
        pq.put((0, source))
        dist[source] = 0
        
        while not pq.empty():
            u = pq.get()[1]            
            for i in range(self.v):
                if self.edges[u][i] > 0:
                    if dist[i] > dist[u] + self.edges[u][i]:
                        dist[i] = dist[u] + self.edges[u][i]
                        pq.put((dist[i], i))
        self.print_solution(dist)

    def print_solution(self, dist): #แสดงจุดยอดและระยะทางที่สั้นที่สุดของแต่จุด
        print("Vertex \tDistance from Source")
        for i in range(self.v):
            print(i, "\t", dist[i])

