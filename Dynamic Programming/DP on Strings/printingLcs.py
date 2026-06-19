class Solution:
  def longestCommonSubsequence(self, text1, text2):
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

      i,j=m,n
      ans=[]
      while(i > 0 and j > 0):
        if text1[i-1] == text2[j-1]:
          ans.append(text1[i-1])
          i-=1
          j-=1
        else:
          if dp[i-1][j] > dp[j-1][i]:
            i-=1
          else:
            j-=1
      ans.reverse()
      print("".join(ans))

sol = Solution()
sol.longestCommonSubsequence("abaaa","baabaca")
