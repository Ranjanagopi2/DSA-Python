class Node:
  def _init_(self,val):
    self.data=val 
    self.next=None
class Queue:
  def _init_(self):
    self.front=None
    self.rear=None
  def enqueue(self,val):
    newNode=Node(val)
    if self.rear is None:
      self.front=self.rear=newNode
    else:
      self.rear.next=newNode
      self.rear=newNode
  def dequeue(self):
    if self.front is None:
      print("Queue is Empty")
    data=self.front.data
    self.front=self.front.next
    return data 
  def display(self):
    temp=self.front
    while temp:
      print(temp.data,end="-->")
      temp=temp.next
    print("Null")
q1=Queue()
n=int(input())
for i in range(n):
  k=int(input())
  q1.enqueue(k)
q1.display()
q1.dequeue()
q1.display()
result=q1.dequeue()
print("Deleted element:",result)
q1.display()