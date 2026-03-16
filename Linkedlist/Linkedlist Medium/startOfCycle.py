class ListNode:
  def __init__(self, x):
      self.val = x
      self.next = None

class Solution:
  def detectCycle(self, head):
    slow=head
    fast=head
    while(fast != None and fast.next != None):
        slow=slow.next
        fast=fast.next.next
        ptr=head
        if(slow == fast):
            while(ptr != slow):
                ptr=ptr.next
                slow=slow.next
            return ptr
    return None