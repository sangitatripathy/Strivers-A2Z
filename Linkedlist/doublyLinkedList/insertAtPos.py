class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class Solution:
    def insertAtPos(self, head, p, x):
        newNode=Node(x)
        if not head:
            return None
        if p == 0:
            newNode.next=head.next
            newNode.prev=head
            if head.next:
                head.next.prev=newNode
            head.next= newNode
            return head
        temp = head
        count=0
        while temp and count < p:
            temp = temp.next
            count+=1
        newNode.prev=temp
        newNode.next=temp.next
        if temp.next:
            temp.next.prev=newNode
        temp.next=newNode
        return head
        
        # Code Here
        