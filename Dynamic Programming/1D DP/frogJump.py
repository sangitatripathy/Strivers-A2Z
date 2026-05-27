class Solution:
    def calcCost(self,height,n,dp):
      # if n == 0:
      #   return 0
      # if n==1:
      #   return abs(height[n]-height[n-1])
      # left = self.calcCost(height,n-1)+ abs(height[n]-height[n-1])
      # right = self.calcCost(height,n-2)+abs(height[n]-height[n-2])
      # return min(left,right)

      # if n == 0:
      #   return 0
      # if n == 1:
      #   dp[1] = abs(height[1]-height[0])
      #   return dp[1]
      # if dp[n] != -1: return dp[n]
      # left = self.calcCost(height,n-1,dp)+ abs(height[n]-height[n-1])
      # right = self.calcCost(height,n-2,dp)+abs(height[n]-height[n-2])
      # dp[n] = min(left,right)
      # return dp[n]

      dp[0] = 0
      dp[1] = abs(height[1]-height[0])
      for i in range(2,len(height)):
        jumpOne = dp[i-1] + abs(height[i]- height[i-1])
        jumpTwo = dp[i-2] + abs(height[i]- height[i-2])
        dp[i] = min(jumpOne,jumpTwo)
      return dp[n]
    
    def minCost(self, height):
      dp =[-1] * len(height)
      return self.calcCost(height,len(height)-1,dp)

s= Solution()
heights = [20, 30, 40, 20]
print(s.minCost(heights))
      