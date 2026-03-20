class Solution:
    def getIntersectionNode(self, headA, headB):
      #Brute Force
      # dict={}
      # temp=headA
      # while(temp):
      #     dict[temp]=1
      #     temp=temp.next
      # temp2=headB
      # while(temp2):
      #     if temp2 in dict:
      #         return temp2
      #     temp2=temp2.next

      # n1,n2=0,0
      # temp=headA
      # while(temp):
      #   n1+=1
      #   temp=temp.next
      # temp2=headB
      # while(temp2):
      #   n2+=1
      #   temp2=temp2.next
      # temp=headA
      # temp2= headB
      # if(n1 > n2):
      #   d=n1-n2
      #   while(d > 0):
      #     d-=1
      #     temp=temp.next
      # else:
      #   d=n2-n1
      #   while(d > 0):
      #     d-=1
      #     temp2=temp2.next
      # while(temp and temp2):
      #   if(temp == temp2):
      #     return
      #   temp=temp.next
      #   temp2=temp2.next

      temp1=headA
      temp2=headB
      while(temp1!=temp2):
        if(temp1 == temp2):
          return temp1
        if(temp1 == None):
          temp1=headA
        if(temp2 == None):
          temp2=headB
        temp1=temp1.next
        temp2=temp2.next
          