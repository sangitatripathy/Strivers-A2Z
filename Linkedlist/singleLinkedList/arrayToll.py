class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Brute Force
# class Linkedlist:
#   def __init__(self):
#     self.head = None
#   def append(self,data):
#     newNode = Node(data)
#     if not self.head:
#       self.head = newNode
#       return
#     curr=self.head
#     while curr.next:
#       curr = curr.next
#     curr.next= newNode
    
# class Solution:
    # def arrayToList(self, arr):
    #   ll=Linkedlist()
    #   for n in arr:
    #     ll.append(n)
    #   return ll.head

# Optimal approach
class Solution:
    def arrayToList(self, arr):
      if not arr:
        return None
      head = Node(arr[0])
      tail=head
      for i in range(1,len(arr)):
        newNode = Node(arr[i])
        tail.next=newNode
        tail= newNode
      return head

sol = Solution()
sol.arrayToList([10,20,30,40,50])