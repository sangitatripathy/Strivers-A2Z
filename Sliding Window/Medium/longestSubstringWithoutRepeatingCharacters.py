class Solution:
    def lengthOfLongestSubstring(self, s):
      # maxlen=0
      # for i in range(len(s)):
      #   seen=set()
      #   for j in range(i,len(s)):
      #     if s[j] in seen:
      #       break
      #     seen.add(s[j])
      #     maxlen= max(maxlen,j-i+1)
      # return maxlen

      seen={}
      left,right,maxlen=0,0,0
      n=len(s)
      while(right < n):
        if s[right] in seen and seen[s[right]] >=left:
          left=seen[s[right]]+1
        seen[s[right]]=right
        maxlen=max(maxlen,right-left+1)
        right+=1
      return maxlen

s = "abcabcbb"  
sol = Solution()
print(sol.lengthOfLongestSubstring(s))
         
          