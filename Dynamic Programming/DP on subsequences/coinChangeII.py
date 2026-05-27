class Solution:
    def change(self, amount, coins):
      # def calcCoins(ind,amt,dp):
      #   if amt==0:
      #     return 1
        
      #   if ind == 0:
      #     if amt % coins[0] == 0:
      #       return 1
      #     return 0
        
      #   if dp[ind][amt] != -1:
      #     return dp[ind][amt]
        
      #   notTake= calcCoins(ind-1,amt,dp)
      #   take=0
      #   if coins[ind] <= amt:
      #     take = calcCoins(ind,amt-coins[ind],dp)
      #   dp[ind][amt] = take+notTake
      #   return dp[ind][amt] 
      # return calcCoins(n-1,amount,dp)
      n=len(coins)
      dp=[]
      
      for _ in range(n):
        row=[]
        for _ in range(amount+1):
          row.append(0)
        dp.append(row)

      for i in range(amount+1):
        if i%coins[0] == 0:
          dp[0][i] = 1

      for i in range(1,n):
        for tar in range(amount+1):
          notTake= dp[i-1][tar]
          take=0
          if coins[i] <= tar:
            take = dp[i][tar-coins[i]]
          dp[i][tar] = take+notTake

      return dp[n-1][amount]

amount = 500
coins = [3,5,7,8,9,10,11]
sol = Solution()
print(sol.change(amount,coins))
        