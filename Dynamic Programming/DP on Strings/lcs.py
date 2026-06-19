class Solution:
    def longestCommonSubsequence(self, text1, text2):
      # def calcSeq(dp,ind1,ind2):
      #   if ind1 < 0 or ind2 < 0:
      #     return 0
        
      #   if dp[ind1][ind2] != -1:
      #     return dp[ind1][ind2]
        
      #   if text1[ind1] == text2[ind2]:
      #     dp[ind1][ind2] = 1+calcSeq(dp,ind1-1,ind2-1)
      #     return dp[ind1][ind2]
      #   else:
      #     dp[ind1][ind2] = max(calcSeq(dp,ind1-1,ind2),calcSeq(dp,ind1,ind2-1))
      #     return dp[ind1][ind2]

      m=len(text1)
      n=len(text2)
      dp=[]
      for i in range(m+1):
        temp=[]
        for j in range(n+1):
          temp.append(-1)
        dp.append(temp)

      for i in range(m+1): dp[i][0] =0
      for j in range(n+1): dp[0][j] =0
      
      for i in range(1,m+1):
        for j in range(1,n+1):
          if text1[i-1] == text2[j-1]:
            dp[i][j] = 1+dp[i-1][j-1]
          else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])    
      return dp[m][n]

sol = Solution()
print(sol.longestCommonSubsequence("adebc","dcadb"))
          
          
        