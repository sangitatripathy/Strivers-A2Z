class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class Single_ll:
  def __init__(self):
    self.head=None  

  def append(self,data):
    new_node=Node(data)
    if not self.head:
      self.head=new_node
      return
    last=self.head
    while last.next:
      last=last.next
    last.next=new_node


  def display(self):
    current=self.head
    while current:
      print(current.data," ")
      current=current.next
    print("None")

linked_list=Single_ll()   
linked_list.append(1)
linked_list.append(5)
linked_list.append(7)
linked_list.append(4)
linked_list.display()            