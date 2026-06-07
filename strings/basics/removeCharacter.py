class Solution:
  def removeChars (ob, str1, str2):
    res=[]
    for st in str1:
      if st in str2:
        continue
      res.append(st)
    return ''.join(res)

sol = Solution()
sol.removeChars("computer","cat")
            
        