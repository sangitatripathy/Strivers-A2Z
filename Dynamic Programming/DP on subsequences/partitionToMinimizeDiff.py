class Solution:
    def minDifference(self, arr):
        total = sum(arr)
        n = len(arr)
        dp = [[False]*(total+1) for _ in range(n)]

        for i in range(n):
            dp[i][0] = True

        if arr[0] <= total:
            dp[0][arr[0]] = True

        for ind in range(1, n):
            for target in range(1, total+1):
                notTake = dp[ind-1][target]
                take = False
                if arr[ind] <= target:
                    take = dp[ind-1][target-arr[ind]]

                dp[ind][target] = notTake or take

        mini = float('inf')
        for s1 in range(total//2 + 1):
            if dp[n-1][s1]:
                diff = abs(total - 2*s1)
                mini = min(mini, diff)

        return mini

sol= Solution()
print(sol.minDifference([2,-1,0,4,-2,-9]))
      