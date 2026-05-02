class Solution:
    def calcSum(self,ind,arr,target,dp):
      if(target == 0): return True
      if(ind == 0): return (arr[0] == target)
      if(dp[ind][target] != -1): return dp[ind][target]
      notTake=self.calcSum(ind-1,arr,target,dp)
      take= False
      if(target >= arr[ind]):
        take = self.calcSum(ind-1,arr,target-arr[ind],dp)
      dp[ind][target] = notTake or take
      return dp[ind][target]
      
    def isSubsetSum (self, arr, sum):
      dp=[]
      n=len(arr)
      
      for _ in range(n):
        row=[]
        for i in range(sum+1):
          row.append(False)
        dp.append(row)
      
      for ind in range(n):
        dp[ind][0] = True

      if(arr[0] <= sum):
        dp[0][arr[0]] = True
      
      for ind in range(1,n):
        for target in range(1,sum+1):
          notTake = dp[ind-1][target]
          take = False
          if(arr[ind] <= target): 
            take= dp[ind-1][target-arr[ind]]
          dp[ind][target] = notTake or take
      return dp[n-1][sum]
      # return self.calcSum(n-1,arr,sum,dp)
      
sol = Solution()
arr=[2,3,1,1]
print(sol.isSubsetSum(arr,4))