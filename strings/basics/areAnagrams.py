class Solution:
  def areAnagrams(self, s1, s2):
    freq={}
    for ch in s1:
      freq[ch] = freq.get(ch,0)+1
    
    for ch in s2:
      if ch not in freq:
        return False
      freq[ch]-=1
      if freq[ch] < 0:
        return False
    return True