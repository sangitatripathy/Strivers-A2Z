def frogJump(n, heights,k):
  # if n == 0: return 0
  # mini = float('inf')
  # for j in range(1,k+1):
  #   if n-j >= 0:
  #     jumps = frogJump(n-j,heights,k) + abs(heights[n] - heights[n-j])
  #     mini = min(mini,jumps)
  # return mini
  dp=[float('inf')]*len(heights)
  dp[0] = 0
  for i in range(1,len(heights)):
    for j in range(1,k+1):
      if i-j >=0:
        dp[i] = min(dp[i-j]+abs(heights[i]-heights[i-j]),dp[i])
  return dp[-1]
      
        

heights=[15,4,1,14,15]
print(frogJump(len(heights)-1,heights,3))