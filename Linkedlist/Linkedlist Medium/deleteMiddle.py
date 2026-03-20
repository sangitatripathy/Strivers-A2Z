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

  def deleteMiddle(self):
    slow=self.head
    fast=self.head
    temp=None
    while(fast and fast.next):
      temp=slow
      slow=slow.next
      fast=fast.next.next
    temp.next=slow.next
    


ll1= single_ll()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
ll1.append(5)
ll1.deleteMiddle()

ll2= single_ll()
ll2.append(1)
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(5)
ll2.append(6)
ll2.deleteMiddle()