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
      temp=head
      while(temp.next):
        prev2=prev
        prev=temp
        temp=temp.next
        prev.next=prev2
      temp.next=prev
      return temp
    def isPalindrome(self, head):
      if head is None or head.next is None:
        return True
      slow=head
      fast=head
      while(fast.next and fast.next.next):
        slow=slow.next
        fast=fast.next.next
      head2=self.reverse(slow.next)
      temp=head
      while(head2 != None and temp != slow.next):
        if(head2.data != temp.data):
          return False
        head2=head2.next
        temp=temp.next
      self.reverse(slow.next)
      return True
      # stack=[]
      # temp=head
      # while(temp):
      #   stack.append(temp.data)
      #   temp=temp.next
      # temp=head
      # while(temp):
      #   if(temp.data == stack.pop()): 
      #     temp=temp.next
      #     continue
      #   else:
      #     return False
      # return True
        
        


ll1= single_ll()
ll1.append(1)
ll1.append(2)
ll1.display()
sol=Solution()
print(sol.isPalindrome(ll1.head))