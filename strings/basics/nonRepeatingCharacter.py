class Solution:
  def nonRepeatingChar(self,s):
    freq={}
    ans="$"
    for ch in s:
      freq[ch] = freq.get(ch,0)+1
    for key,value in freq.items():
      if value == 1:
        ans=key
        break
    return ans
    