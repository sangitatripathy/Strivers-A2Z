class Solution:
    def coinChange(self, coins, amount):
        def coin(ind,coins,amount,dp):
            if amount == 0:
                return 0
            
            if ind == 0:
                if amount%coins[ind] == 0:
                    return amount//coins[ind]
                return float('inf')

            if dp[ind][amount] != -1:
                return dp[ind][amount]

            take=float('inf')
            notTake = coin(ind-1,coins,amount,dp)
            if coins[ind] <= amount:
                take = 1+coin(ind,coins,amount-coins[ind],dp)
            dp[ind][amount] = min(notTake,take)
            return dp[ind][amount]
        
        n=len(coins)
        dp=[]
        for _ in range(n):
            row=[]
            for _ in range(amount+1):
                row.append(-1)
            dp.append(row)             
        res=coin(n-1,coins,amount,dp)
        return res

coins =[411,412,413,414,415,416,417,418,419,420,421,422]
amount = 9864
sol= Solution()
print(sol.coinChange(coins,amount))