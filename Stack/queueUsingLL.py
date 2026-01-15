class Node:
  def __init__(self, new_data):
      self.data = new_data
      self.next = None

class myQueue:

  def __init__(self):
      self.front=None
      self.rear=None
      self.count =0
      # Initialize your data members
      

  def isEmpty(self):
      return self.front is None 
      

  def enqueue(self, x):
      newNode= Node(x)
      if self.rear is None:
        self.rear = self.front = newNode
      else:
        self.rear.next = newNode
        self.rear = newNode
      self.count+1

  def dequeue(self):
      if self.isEmpty():
        return -1
      x=self.front.data
      self.front=self.front.next
      self.count -= 1
      return x


  def getFront(self):
    if self.isEmpty():
        return -1
    return self.front.data


  def size(self):
      return self.count