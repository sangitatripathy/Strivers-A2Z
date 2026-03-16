class Solution:
    def searchKey(self, head, key):
      curr= head
      while curr:
        if curr.data == key:
          return True
        curr=curr.next
      return False