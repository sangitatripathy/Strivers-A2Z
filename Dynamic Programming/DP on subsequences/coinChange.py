class Solution:
    def coinChange(self, coins, amount):
        # def coin(ind,coins,amount,dp):
        #     if amount == 0:
        #         return 0
            
        #     if ind == 0:
        #         if amount%coins[ind] == 0:
        #             return amount//coins[ind]
        #         return float('inf')

        #     if dp[ind][amount] != -1:
        #         return dp[ind][amount]

        #     take=float('inf')
        #     notTake = coin(ind-1,coins,amount,dp)
        #     if coins[ind] <= amount:
        #         take = 1+coin(ind,coins,amount-coins[ind],dp)
        #     dp[ind][amount] = min(notTake,take)
        #     return dp[ind][amount]
        
        n=len(coins)
        dp=[]
        for _ in range(n):
            row=[]
            for _ in range(amount+1):
                row.append(-1)
            dp.append(row)             

        for t in range(amount+1):
            if t%coins[0] == 0:
                dp[0][t] = t//coins[0]
            else:
                dp[0][t] = float('inf')

        for i in range(1,n):
            for tar in range(amount+1):
                notTake = dp[i-1][tar]
                take = float('inf')
                if (coins[i] <= tar):
                    take = 1+ dp[i][tar-coins[i]]
                dp[i][tar] = min(take,notTake)
        return dp[n-1][amount]
            
        # res=coin(n-1,coins,amount,dp)
        # return res

coins =[411,412,413,414,415,416,417,418,419,420,421,422]
amount = 9864
sol= Solution()
print(sol.coinChange(coins,amount))