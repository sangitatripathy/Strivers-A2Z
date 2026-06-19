class Solution:
  def longestCommonSubstring(self, text1, text2):
    # m=len(text1)
    # n=len(text2)
    # def calcStr(ind1,ind2):
    #   if ind1 < 0 or ind2 < 0:
    #     return 0
    #   if text1[ind1] == text2[ind2]:
    #     return 1+ calcStr(ind1-1,ind2-1)
    #   else:
    #     return 0
    # ans=0
    # for i in range(m):
    #   for j in range(n):
    #     ans= max(ans,calcStr(i,j))
    # return ans

    m =len(text1)
    n=len(text2)
    dp = [[-1]*(n+1) for _ in range(m+1)]
    for i in range(m+1): dp[i][0] = 0
    for j in range(n+1): dp[0][j] = 0
    maxi=0
    for i in range(1,m+1):
      for j in range(1,n+1):
        if text1[i-1] == text2[j-1]:
          dp[i][j] = 1+dp[i-1][j-1]
          maxi = max(maxi,dp[i][j])
        else:
          dp[i][j] = 0
    return maxi
    

sol = Solution()
print(sol.longestCommonSubstring("abc","acb"))
      
      