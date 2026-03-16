class Solution:
    def reverse(self, head):
      if not head:
        return None
      curr=head
      while curr:
        temp=curr.prev
        curr.prev=curr.next
        curr.next=prev
        curr=curr.prev
      if temp:
        head = temp.prev
      return head