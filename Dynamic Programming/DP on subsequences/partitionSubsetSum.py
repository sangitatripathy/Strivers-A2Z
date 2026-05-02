class Solution:
    def canPartition(self, nums):
      if(sum(nums)%2 != 0):
        return False
      target= sum(nums)//2
      dp=[]
      n=len(nums)
      
      for ind in range(n):
        row=[]
        for t in range(target+1):
          row.append(False)
        dp.append(row)

      for ind in range(n):
        dp[ind][0] = True

      if(nums[0] <= target):
        dp[0][nums[0]] = True

      for ind in range(1,n):
        for t in range(1,target+1):
          notTake=dp[ind-1][t]
          take=False
          if(nums[ind] <= t):
            take= dp[ind-1][t-nums[ind]]
          dp[ind][t] = notTake or take
      
      return dp[n-1][target]

sol= Solution()
nums = [1,5,11,5]
print(sol.canPartition(nums))