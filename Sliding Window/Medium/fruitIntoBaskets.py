class Solution:
    def totalFruit(self, fruits):
      # maxlen,l,r=0,0,0
      # freq={}
      # while r <len(fruits):
      #   freq[fruits[r]] = freq.get(fruits[r],0)+1
      #   while len(freq) > 2:
      #     freq[fruits[l]]-=1
      #     if freq[fruits[l]] == 0:
      #       del freq[fruits[l]]
      #     l+=1
      #   maxlen=max(maxlen,r-l+1)
      #   r+=1
      # return maxlen
      maxlen,r,l=0,0,0
      freq={}
      while r < len(fruits):
        freq[fruits[r]] = freq.get(fruits[r],0)+1
        if len(freq) > 2:
          freq[fruits[l]]-=1
          if freq[fruits[l]] == 0:
            del freq[fruits[l]]
          l+=1
        if len(freq) <=2:
          maxlen= max(maxlen,r-l+1)
        r+=1
      return maxlen
        
fruits = [1,2,3,2,2]
sol = Solution()
print(sol.totalFruit(fruits))