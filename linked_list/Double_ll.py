class Node:
  def __init__(self,data):
    self.prev=None
    self.data=data
    self.next=None

class Double_ll:
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
    new_node.prev=last
    last.next=new_node 

  def display(self):
    current=self.head
    while current:
      print(current.data,end=" ")
      current=current.next
    print("\n")  
 

  def insert_at_begin(self,data):
    new_node=Node(data)
    if not self.head:
      self.head=new_node
      return
    new_node.next=self.head
    self.head.prev=new_node
    self.head=new_node
    self.display()

  def insert_at_position(self,index,data):
    if index == 0:
      self.insert_at_begin(data)
      return 
    new_node=Node(data)
    position=0
    current=self.head
    while(position+1 != index and current != None):
      position+=1
      current=current.next
    if current != None:
      new_node.prev=current
      new_node.next=current.next
      current.next=new_node
    else:
      print("index not found")
    self.display()  

  def remove_first_node(self):
    if self.head == None:
      return
    self.head=self.head.next
    self.head.prev=None
    self.display()

  def remove_last_node(self):
    if self.head == None:
      return
    if self.head.next is None:
      self.head = None
      self.display()
      return
    current=self.head
    while(current.next.next !=None):
      current=current.next
    current.next = None
    self.display()   

  def remove_node_at_a_pos(self,index):
    if self.head == None:
      return
    position=0
    current=self.head
    prev=None
    while(position!= index and current):
      position=position+1
      prev=current
      current=current.next
    prev.next=current.next
    current.next.prev=current.prev
    self.display()        
      

  def display_rev(self):
    current=self.head
    while current.next:
      current=current.next
    while current :
      print(current.data,end=" ")
      current=current.prev 
   
linked_list=Double_ll()   
linked_list.append(1)
linked_list.append(5)
linked_list.append(7)
linked_list.append(4)
linked_list.insert_at_begin(10)
linked_list.insert_at_position(2,11)
linked_list.remove_first_node()
linked_list.remove_last_node()
linked_list.remove_node_at_a_pos(2)
linked_list.display_rev()                     
        