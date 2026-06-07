class Solution:
  def smallerAndLarge(self, s):
    arr=s.split()
    mini=arr[0]
    maxi=arr[0]
    res=[]
    for st in arr:
      if len(st) < len(mini):
          mini=st
      if len(st) >= len(maxi):
          maxi=st
    res.append(mini)
    res.append(maxi)
    return res
        
                
        