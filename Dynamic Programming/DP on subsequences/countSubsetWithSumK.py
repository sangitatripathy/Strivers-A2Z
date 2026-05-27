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

  def checkSumRecur(self,arr,ind,target,count):
    if target == 0:
      return 1
    if ind == 0 :
      return target == arr[0]
    notPick= self.checkSumRecur(arr,ind-1,target,count)
    if arr[ind] <= target:
      pick=self.checkSumRecur(arr,ind-1,target-arr[ind],count)
    return pick+notPick

  def tabCheckSum(self,arr,target):
    dp=[]
    n=len(arr)
    for _ in range(len(arr)):
      row=[]
      for j in range(target+1):
        row.append(0)
      dp.append(row)

    if arr[0] == 0:
      dp[0][0] = 2
    else:
      dp[0][0] = 1

    if arr[0] != 0 and arr[0] <= target:
      dp[0][arr[0]] = 1

    for i in range(1,len(arr)):
      for j in range(target+1):
        notTake=dp[i-1][j]
        take=0
        if arr[i] <= j:
          take = dp[i-1][j-arr[i]]
        dp[i][j] = take+notTake
    return dp[n-1][target]
                 
sol = Solution()
arr=[28,4,3,27,0,24,26]
print(sol.tabCheckSum(arr,24))