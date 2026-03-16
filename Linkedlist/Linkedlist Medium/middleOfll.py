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

  def middleNode(self):
    curr=self.head
    count=0
    while(curr):
      count+=1
      curr=curr.next
    mid=count//2+1
    temp=self.head
    pos=0
    while(temp and pos<mid-1):
      pos+=1
      temp=temp.next
    return temp
    

ll1= single_ll()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
ll1.append(5)
ll1.display()