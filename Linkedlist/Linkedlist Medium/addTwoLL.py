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
    def addTwoLists(self, head1, head2):
      dummy=Node(-1)
      curr=dummy
      carry=0
      while head1 and head2 or carry:
        val1=head1.data if head1 else 0
        val2=head2.data if head2 else 0

        res=val1+val2+carry
        curr.next=Node(res%10)
        carry=res//10
        curr=curr.next
        if head1:
          head1=head1.next
        if head2:
          head2=head2.next
      self.display(dummy.next)
      return dummy.next
    def display(self,head):
      last=head
      while last:
        print(last.data)
        last=last.next

ll1=single_ll()
ll1.append(3)
ll1.append(4)
ll1.append(5)

ll2=single_ll()
ll2.append(4)
ll2.append(5)

sol=Solution()
sol.addTwoLists(ll2.head,ll1.head)