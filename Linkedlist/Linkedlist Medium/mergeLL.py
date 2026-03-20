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
    def sortedMerge(self, head1, head2):
        dummy = Node(-1)
        current=dummy
        while(head1 and head2):
            if(head1.data <= head2.data):
                current.next = Node(head1.data)
                head1=head1.next
            else:
                current.next = Node(head2.data)
                head2=head2.next
            current=current.next
        while(head1):
            dummy.next=Node(head1.data)
            dummy=dummy.next
            head1=head1.next
        while(head2):
            dummy.next=Node(head2.data)
            dummy=dummy.next
            head2=head2.next
        self.display(dummy.next)
        return dummy.next
    def display(self,head):
      last=head
      while last:
        print(last.data)
        last=last.next

sol=Solution()

ll1=single_ll()
ll1.append(1)
ll1.append(1)
ll1.append(3)
ll1.append(4)
ll1.append(5)

ll2= single_ll()
ll2.append(1)
ll2.append(2)
ll2.append(3)
ll2.append(4)
ll2.append(5)
ll2.append(6)

sol.sortedMerge(ll1.head,ll2.head)