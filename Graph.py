#Representation of adjacent list in graph 

class Graph():
  def __init__(self):
    self.adjlist={}
  def addvertex(self,vertex):
    if vertex not in self.adjlist:
      self.adjlist[vertex]=[]
  def addedges(self,u,v):
    if u not in self.adjlist:
      self.addvertex(u)
    if v not in self.adjlist:
      self.addvertex(v)
    self.adjlist[u].append(v)
    self.adjlist[v].append(u)
  def display(self):
    for vertex in self.adjlist:
      print(f"{vertex}:{self.adjlist[vertex]}")
g1=Graph()
g1.addedges('A','B')
g1.addedges('A','C')
g1.addedges('B','D')
g1.addedges('D','E')
g1.display()


"""
Output:
A:['B', 'C']
B:['A', 'D']
C:['A']
D:['B', 'E']
E:['D']

"""
#Representation of adjacent matrix in graph 
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices 
        self.size = len(vertices)
        self.vertex_indices = {vertex: index for index, vertex in enumerate(vertices)}
        self.adj_matrix = [[0] * self.size for _ in range(self.size)]

    def add_edge(self, u, v):
        i = self.vertex_indices[u]
        j = self.vertex_indices[v]
        self.adj_matrix[i][j] = 1
        self.adj_matrix[j][i] = 1  

    def display(self):
        print("  ", " ".join(self.vertices))
        for i in range(self.size):
            print(self.vertices[i], self.adj_matrix[i])


vertices = ["A", "B", "C", "D", "E"]
g = Graph(vertices)
g.add_edge("A", "B")
g.add_edge("A", "C")
g.add_edge("B", "D")
g.add_edge("C", "D")
g.add_edge("D", "E")

g.display()

"""
Output:

   A B C D E
A [0, 1, 1, 0, 0]
B [1, 0, 0, 1, 0]
C [1, 0, 0, 1, 0]
D [0, 1, 1, 0, 1]
E [0, 0, 0, 1, 0]
"""
