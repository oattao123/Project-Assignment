from collections import defaultdict

class Graph1:

	def __init__(self, vertices): # หาจุดยอด 
		self.V = vertices 
		self.graph = []


	
	def addEdge1(self, u, v, w): # กำหนดจุดสองจุดและค่าของจุด
		self.graph.append([u, v, w])


	def find(self, parent, i): #ใช้หาเส้นทางต้นและปลาย 
		if parent[i] != i:
			parent[i] = self.find(parent, parent[i])
		return parent[i]

	def union(self, parent, rank, x, y): 

		# หาคู่ของจุดยอดสองที่น้อยด้วยการเปรียบเทียบ
		if rank[x] < rank[y]:
			parent[x] = y
		elif rank[x] > rank[y]:
			parent[y] = x

		# หาได้แล้วก็หาต่อไป
		else:
			parent[y] = x
			rank[x] += 1

	def KruskalMST(self):
		result = []
		parent = []
		rank = []
		i = 0
		e = 0
	
		self.graph = sorted(self.graph,key=lambda item: item[2])

		for node in range(self.V):  #ใส่ค่าว่าจุดอะไรบ้าง
			parent.append(node)
			rank.append(0)
	

		while e < self.V - 1: #หาทางที่ไปน้อยที่สุด

			u, v, w = self.graph[i] 
			i = i + 1
			x = self.find(parent, u) #กำหนดค่าจุดเริ่ม
			y = self.find(parent, v) #กำหนดค่าจุดปลาย

			if x != y: #ตรวจสอบจนหาทางได้น้อยที่สุด
				e = e + 1
				result.append([u, v, w])
				self.union(parent, rank, x, y)


		minimumCost = 0
		print("Edges in the constructed MST") 
		for u, v, weight in result:  #พิมพ์เส้นทาง
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Minimum Spanning Tree", minimumCost)
 