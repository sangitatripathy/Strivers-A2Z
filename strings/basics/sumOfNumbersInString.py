class Solution:
  def findSum(self, s):
    ans=0
    temp=0
    for ch in s:
      if ch.isdigit():
        temp = temp*10+int(ch)
      else:
        ans+=temp
        temp=0
    ans+=temp
    return ans
        
                
