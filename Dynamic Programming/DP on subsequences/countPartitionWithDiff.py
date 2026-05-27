class Solution:
  def checkSum(self,arr,target):
    dp=[]
    n=len(arr)
    
    for _ in range(n):
      row=[]
      for tar in range(target+1):
        row.append(0)
      dp.append(row)

    if arr[0] == 0:
      dp[0][0] = 2
    else:
      dp[0][0] = 1

    if arr[0] != 0 and arr[0] <= target:
      dp[0][arr[0]] = 1

    for i in range(1,n):
      for j in range(target+1):
        notTake = dp[i-1][j]
        take=0
        if arr[i] <= j:
          take = dp[i-1][j-arr[i]] 
        dp[i][j] = take+notTake
    return dp[n-1][target]    
  
  def countPartitions(self, arr, diff):
    totalSum = 0
    for el in arr:
      totalSum+=el
    if totalSum - diff < 0 or (totalSum-diff)%2 != 0:
      return 0
    else:
      return self.checkSum(arr,(totalSum-diff)//2)

sol = Solution()
arr= [5, 2, 6, 4]
diff = 3
print(sol.countPartitions(arr,diff))
       
        
