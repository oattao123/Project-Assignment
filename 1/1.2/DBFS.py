from collections import defaultdict

class Graph:
    def __init__(self): #จัดเก็บกราฟ
        self.graph = defaultdict(list) 

    def addEdge2(self,u,v): #เพิ่มขอบในกราฟ
        self.graph[u].append(v)

    def DFSUtil(self,v,visited): #หาเส้นทางด้วยใช้ DFS ในการหา
        visited.add(v)
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour,visited)
  
    def DFS(self, v): #พิมพ์เป็นทาง DFS ออกมา
        visited = set()
        self.DFSUtil(v,visited)

    def BFS(self, s): #ทำการหาเส้นทางด้วยใช้ BFS ในการหา
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue: 
            s = queue.pop(0)
            print (s, end = " ")
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
    