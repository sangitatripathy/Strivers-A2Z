class Solution:
    def calcCost(self,n,cost,dp):
      dp[0] = cost[0]
      dp[1] = cost[1]
      for i in range(2,n+1):
        dp[i] = cost[i] + min(dp[i-1],dp[i-2])

      return min(dp[n],dp[n-1])
    
    def minCostClimbingStairs(self, cost) -> int:
      dp= [0]*len(cost)
      return self.calcCost(len(cost)-1,cost,dp)
      


cost =[10,15,20]
sol= Solution()
print(sol.minCostClimbingStairs(cost))