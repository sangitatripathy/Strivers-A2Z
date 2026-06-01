class Solution:
    def knapSack(self, val, wt, capacity):
      def calcProfit(ind,val,wt,capacity,dp):
        if capacity == 0:
          return 0
        
        if ind == 0:
          return (capacity//wt[0])*val[0]
        
        if dp[ind][capacity] != -1:
          return dp[ind][capacity]
        
        notTake= calcProfit(ind-1,val,wt,capacity)
        take=0
        if wt[ind] <= capacity:
          take= val[ind]+calcProfit(ind,val,wt,capacity-wt[ind])
        dp[ind][capacity]=max(take,notTake)
        return dp[ind][capacity]

      n= len(val)
      dp=[]
      
      for _ in range(n):
        row=[]
        for _ in range(capacity+1):
          row.append(0)
        dp.append(row)

      return calcProfit(n-1,val,wt,capacity,dp)

val= [6, 8, 7, 100]
wt= [6, 8, 7, 100]
capacity = 1
sol = Solution()
print(sol.knapSack(val,wt,capacity))
        