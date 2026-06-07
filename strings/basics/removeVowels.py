class Solution:
  def removeVowels(self,s):
    res=[]
    vowels={'A','E','I','O','U','a','e','i','o','u'}
    for st in s:
      if st in vowels:
        continue
      res.append(st)
    return ''.join(res)

sol = Solution()
print(sol.removeVowels("welcome to geeksforgeeks"))