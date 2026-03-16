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

  def insertAtbegin(self,data):
    newNode = Node(data)
    if not self.head:
      self.head = newNode
      return
    newNode.next=self.head
    self.head= newNode

  def insertAtPosition(self,ind,data):
    if ind == 0:
      self.insertAtbegin(data)
      return
    newNode = Node(data)
    count =0
    temp = self.head
    while temp and count < ind-1:
      temp = temp.next
      count+=1
    if temp is None:
      print("position not found")
      return
    newNode.next=temp.next
    temp.next= newNode

  def deleteBegin(self):
    if not self.head:
      print("list is empty")
      return 
    self.head = self.head.next

  def deleteEnd(self):
    if not self.head:
      print("list is empty")
      return
    curr= self.head
    while curr.next:
      prev=curr
      curr=curr.next
    prev.next=None

  def deletePosition(self,ind):
    if ind == 0:
      self.deleteBegin()
    count=0
    temp = self.head
    while count < ind-1 and temp:
      temp = temp.next
      count+=1
    temp.next= temp.next.next
    
  def display(self):
    if not self.head:
      return "list is empty"
    last=self.head
    while last:
      print(last.data)
      last=last.next

ll1=single_ll()
ll1.append(10)
ll1.append(20)
ll1.append(30)
ll1.append(40)
ll1.insertAtbegin(45)
print(ll1.display())
ll1.insertAtPosition(4,36)
print(ll1.display())
ll1.deleteBegin()
print(ll1.display())
ll1.deleteEnd()
print(ll1.display())
ll1.deletePosition(1)
print(ll1.display())
      