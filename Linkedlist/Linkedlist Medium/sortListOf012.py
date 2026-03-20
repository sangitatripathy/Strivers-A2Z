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

  def sort(self):
    temp=self.head
    cout0=0
    cout1=0
    cout2=0
    while(temp):
      if(temp.data == 0):
          cout0+=1
      elif(temp.data == 1):
          cout1+=1
      else:
          cout2+=1
      temp=temp.next
    temp=self.head
    while(temp):
      if(cout0 > 0):
          cout0-=1
          temp.data=0
      elif(cout1 > 0):
          cout1-=1
          temp.data =1
      else:
          cout2-=1
          temp.data=2
      temp=temp.next

ll1= single_ll()
ll1.append(0)
ll1.append(2)
ll1.append(1)
ll1.append(0)
ll1.append(1)
ll1.display()
ll1.sort()
ll1.display()