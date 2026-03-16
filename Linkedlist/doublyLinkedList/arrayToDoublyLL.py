class Node:
  def __init__(self, data):   
      self.data = data
      self.next = None
      self.prev = None

class Solution:
  def constructDLL(self, arr):
    if not arr:
      return None
    head = Node(arr[0])
    tail= head
    for i in range(1,len(arr)):
      newNode=Node(arr[i])
      newNode.prev= tail
      tail.next = newNode
      tail= newNode
    return head