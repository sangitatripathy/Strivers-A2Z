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

  def reverse(self):
    # Optimal approach
    curr = self.head
    prev2=None
    prev=None
    while(curr.next):
      prev2=prev
      prev=curr
      curr=curr.next
      prev.next=prev2
    curr.next = prev
    self.head=curr

    # Brute Force approach
    # temp=self.head
    # stack=[]
    # while(temp):
    #   stack.append(temp.data)
    #   temp=temp.next
    # temp=self.head
    # while(temp):
    #   temp.data=stack.pop()
    #   temp=temp.next

  def display(self):
    if not self.head:
      return "list is empty"
    last=self.head
    while last:
      print(last.data)
      last=last.next

ll1= single_ll()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
ll1.append(5)
ll1.display()
ll1.reverse()
ll1.display()