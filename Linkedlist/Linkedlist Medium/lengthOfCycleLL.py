class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

nodes = [ListNode(i) for i in range(1, 10)]
for i in range(8):
    nodes[i].next = nodes[i + 1]
nodes[8].next = nodes[2]
head = nodes[0]

class Solution:
    def lengthOfLoop(self, head):
      # Brute Force
      # dict={}
      # temp=head
      # t=0
      # while(temp):
      #   if temp in dict:
      #     looplen= t-dict[temp]
      #     return looplen
      #   dict[temp] =t
      #   temp=temp.next
      #   t+=1
      # return 0

      slow=head
      fast=head
      count=0
      while(fast!= None and fast.next != None):
        slow=slow.next
        fast=fast.next.next
        if(slow == fast):
          count=1
          slow=slow.next
          while(slow != fast):
            slow=slow.next
            count+=1
          return count
      return count
      


sol=Solution()
print(sol.lengthOfLoop(head))
        