class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class Stack:
  def __init__(self):
    self.top=None
    self.count=0
    
  def isEmpty(self):
    return self.top is None

  def push(self,x):
    newNode = Node(x)
    newNode.next = self.top
    self.count +=1
    self.top=newNode
    
  def pop(self):
    if self.isEmpty():
      return -1
    x = self.top.data
    self.top=self.top.next
    self.count -= 1
    return x

  def peek(self):
    if self.isEmpty():
      return -1
    return self.top.data

  def size(self):
    return self.count
     
     