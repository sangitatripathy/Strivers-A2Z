class Solution:
  def removeChars(self, s: str) -> str:
    res=[]
    for ch in s:
      if ch.isalpha():
        res.append(ch)
    return ''.join(res)

sol = Solution()
print(sol.removeChars("$Gee*k;s..fo, r'Ge^eks?"))
        