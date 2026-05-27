class Solution:
  def findTargetSumWays(self, nums, target):
    
    def tarSum(ind,tar,dp):
      if ind < 0:
        if tar == target:
          return 1
        return 0   
      if (ind,tar) in dp:
        return dp[(ind,tar)]    
      plus = tarSum(ind-1,tar+nums[ind],dp)
      minus = tarSum(ind-1,tar-nums[ind],dp)
      dp[(ind,tar)]=plus+minus
      return dp[(ind,tar)]
     
    n=len(nums)
    count=0
    dp={}
    
    return tarSum(n-1,0,dp)

nums = [1,1,1,1,1]
target = 3
sol=Solution()
print(sol.findTargetSumWays(nums,target))

    
    
        