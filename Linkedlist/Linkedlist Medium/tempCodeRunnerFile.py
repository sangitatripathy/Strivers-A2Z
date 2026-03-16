slow=head
      fast=head
      count=0
      while(fast!= None and fast.next != None):
        if(slow == fast):
          slow=slow.next
          while(slow != fast):
            slow=slow.next
            count+=1
          return count+1
        slow=slow.next
        fast=fast.next.next
      return count