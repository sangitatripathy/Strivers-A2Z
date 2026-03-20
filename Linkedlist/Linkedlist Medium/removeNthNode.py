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

  def removeNthNode(self,n):
    # Brute
    count=0
    temp=self.head
    while(temp):
      count+=1
      temp=temp.next
    steps=count-n
    temp=self.head
    while(temp):
      steps-=1
      if(steps == 0):
        break
      temp=temp.next
    print(temp.data)
    temp.next =temp.next.next
    self.display()

    #Optimal
    # fast=self.head
    # for i in range(n):
    #   fast= fast.next
    # slow=self.head
    # while(fast.next):
    #   slow=slow.next
    #   fast=fast.next
    # slow.next= slow.next.next
    # self.display()

ll1= single_ll()
ll1.append(1)
ll1.append(2)
ll1.append(3)
ll1.append(4)
ll1.append(5)
ll1.display()
ll1.removeNthNode(2)