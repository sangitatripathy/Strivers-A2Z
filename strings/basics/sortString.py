class Solution:
  def sortString(self, s: str) -> str:
    res= list(s)
    res.sort()
    return ''.join(res)

        