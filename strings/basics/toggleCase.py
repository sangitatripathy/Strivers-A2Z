class Solution:
  def toggleCase(self, s):
    res=[]
    for ch in s:
      res.append(ch.swapcase())
    return ''.join(res)
            
        
