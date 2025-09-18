#Directed 
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
B:['D']
C:[]
D:['E']
E:[]

"""


#Undirected graph
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
