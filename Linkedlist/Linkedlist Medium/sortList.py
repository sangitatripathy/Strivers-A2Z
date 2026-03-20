class Node:
  def __init__(self,data):
    self.data=data
    self.next = None

class single_ll:
  def __init__(self):
    self.head = None
    
  def append(self,data):
    newNode= Node(data)
    if not self.head:
      self.head = newNode
      return
    last = self.head
    while last.next:
      last = last.next
    last.next=newNode

  def display(self):
    if not self.head:
      return "list is empty"
    last=self.head
    while last:
      print(last.data)
      last=last.next

  def sortList(self):
    arr=[]
    temp=self.head
    while(temp):
      arr.append(temp.data)
      temp=temp.next
    arr.sort()
    temp=self.head
    i=0
    while(temp):
      temp.data=arr[i]
      i+=1
      temp=temp.next
    