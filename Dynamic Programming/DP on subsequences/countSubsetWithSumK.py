class Solution:
  def checkSum(self,ind,arr,target,dp):
    if ind == 0:
      if target == 0 and arr[0] == 0:
          return 2
      if target == 0 or target == arr[0]:
          return 1
      return 0
    if(dp[ind][target] != -1): return dp[ind][target]
    notPick=self.checkSum(ind-1,arr,target,dp)
    pick=0
    if(arr[ind] <= target):
      pick = self.checkSum(ind-1,arr,target-arr[ind],dp)
    dp[ind][target]=pick+notPick
    return dp[ind][target]
  
  def perfectSum(self,arr,target):
    dp=[]
    n=len(arr)
    for ind in range(n):
      row=[]
      for j in range(target+1):
        row.append(-1)
      dp.append(row)
    return self.checkSum(n-1,arr,target,dp)

sol = Solution()
arr=[28,4,3,27,0,24,26]
print(sol.perfectSum(arr,24))