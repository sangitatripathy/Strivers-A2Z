class Node:
  def __init__(self, data):
      self.data = data
      self.next = None
class Solution:
    def deleteNode(self, head, x):
      if head is None:
        return
      if x==1 :
        head=head.next
        return
      temp = head
      count=0
      while temp and count < x-2:
        temp=temp.next
        count+=1
      temp.next = temp.next.next