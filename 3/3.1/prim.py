
from graph import Graph, Node    

class Prim:
    def __init__(self, graph, start): #กำหนดค่าที่ต้องการใช้ในการทำกราฟ
        self.graph = graph
        self.start = start
        self.tree = []
        self.vertices = self.graph.nodes


    def calculate_total_cost(self): #คำนวณ
        total_cost = 0
        for node in self.tree:
            total_cost += node.length_from_previous_node
        return total_cost


    def execution(self): #หาเส้นทางของกราฟที่ใช้ระยะที่น้อยที่สุดโดยใช้ prim 
        #ให้ค่าเริ่มเป็นค่าเท่ากับ 0
        selected_node = self.graph.find_node(self.start) 
        selected_node.length_from_previous_node = 0
        # Mark the selected node as visisted
        selected_node.visited = True
        self.vertices.remove(selected_node)
        #เพิ่มค่าในการทำกราฟ
        self.tree.append(selected_node)
        # คำนวณระยะห่าง
        for node in selected_node.neighbors:
            child = node[0]
            if node[1] < child.length_from_previous_node:
                child.length_from_previous_node = node[1]
                child.previous_node = selected_node.value

        while len(self.vertices) > 0:
            # เลือกที่มีระยะห่างน้อยที่สุดจากก่อนหน้า
            self.vertices.sort()
            selected_node = self.vertices[0]
            selected_node.visited = True
            # ลบที่เลือกออกจากชุดจุดยอด
            self.vertices.remove(selected_node)
            self.tree.append(selected_node)
            # คำนวณระยะห่างระหว่างพาเรนต์
            for node in selected_node.neighbors:
                child = node[0]
                if not child.visited:
                    if node[1] < child.length_from_previous_node:
                        child.length_from_previous_node = node[1]
                        child.previous_node = selected_node.value

        total_cost = self.calculate_total_cost()
        return self.tree, total_cost
        

