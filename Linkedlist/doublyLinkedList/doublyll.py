class Node:
    def __init__(self, data):   
        self.data = data
        self.next = None
        self.prev = None

class double_ll:
    def __init__(self):
      self.head = None
      
    def append(self,data):
      newNode = Node(data)
      if not self.head:
        self.head = newNode
        return
      curr = self.head
      while curr.next:
        curr=curr.next
      newNode.prev = curr
      curr.next = newNode

    def insertAtPos(self,data,ind):
      newNode=Node(data)
      if not self.head:
        return None
      if ind == 0:
        self.head.prev=newNode
        newNode.next=self.head
        self.head = newNode
        return 
      count=0
      curr=self.head
      while curr and count < ind:
        curr = curr.next
        count+=1
      newNode.prev=curr
      newNode.next = curr.next
      if curr.next:
        curr.next.prev= newNode
      curr.next = newNode

    def deletePos(self,ind):
      if ind==1:
        self.head=self.head.next
        self.head.prev=None
        return 
      curr=self.head
      prev=curr
      count=0
      while curr and count < ind-1:
        prev=curr
        curr=curr.next
        count+=1
      prev.next=curr.next
      if curr.next:
        curr.next.prev=prev
      return
        
    def display(self):
      if not self.head:
        print("list is empty")
        return
      curr=self.head
      while curr:
        print(curr.data)
        curr= curr.next

ll = double_ll()
ll.append(10)
ll.append(20)
ll.append(30)
ll.insertAtPos(40,2)
ll.display()
ll.deletePos(3)
ll.display()
        