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

class Solution:
    def reverse(self,head):
      prev2=None
      prev=None
      curr = head
      while(curr):
        prev2=prev
        prev=curr
        curr=curr.next
        prev.next=prev2
      return prev
    def addOne(self,head):
      newHead=self.reverse(head)
      dummy=Node(-1)
      curr=dummy
      carry=1
      while(newHead):
        add=newHead.data+carry
        if(add >= 10):
          curr.next=Node(0)
          carry=1
        else:
          curr.next=Node(add)
          carry=0
        curr=curr.next
        newHead=newHead.next
      if(carry):
        curr.next = Node(1)
      sol =self.reverse(dummy.next)
      self.display(sol)
      return self.reverse(dummy.next)
    def display(self,head):
      last=head
      while last:
        print(last.data)
        last=last.next
        
        

ll1=single_ll()
ll1.append(9)
ll1.append(9)
ll1.append(9)
ll1.append(9)
ll1.append(9)

sol=Solution()
sol.addOne(ll1.head)
      