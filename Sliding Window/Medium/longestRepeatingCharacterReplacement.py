class Solution:
    def characterReplacement(self, s, k):
      maxlen,l,r,maxf=0,0,0,0
      freq={}
      while(r < len(s)):
        freq[s[r]] = freq.get(s[r],0)+1
        maxf= max(maxf,freq[s[r]])
        while((r-l+1)-maxf > k):
          freq[s[l]]-=1
          for key in freq:
            maxf= max(maxf,freq[key])
          l+=1
        if((r-l+1)-maxf <= k):
          maxlen=max(maxlen,(r-l+1))
        r+=1
      return maxlen 