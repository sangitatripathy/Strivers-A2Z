class Solution:
  def calcItems(self,W,val,wt,ind,dp):
    if ind == 0:
      if wt[0] <= W:
        return val[0]
      return 0
    if dp[ind][W] != -1:
      return dp[ind][W]
    take =0
    if wt[ind] <= W:
      take = val[ind]+self.calcItems(W-wt[ind],val,wt,ind-1,dp)
    notTake= self.calcItems(W,val,wt,ind-1,dp)
    dp[ind][W] = max(take,notTake)
    return dp[ind][W]
     
  def knapsack(self, W, val, wt):
    n=len(wt)
    dp=[]
    
    for _ in range(n):
      row=[]
      for _ in range(W+1):
        row.append(-1)
      dp.append(row)
      
    return self.calcItems(W,val,wt,len(val)-1,dp)

sol = Solution()
W = 5
val= [10, 40, 30, 50]
wt= [5, 4, 2, 3]
print(sol.knapsack(W,val,wt,))

