def jump(num):
  dp=[0]*(num+1)
  dp[0]=1
  dp[1]=1
  for i in range(2,num+1):
    dp[i]=dp[i-1]+dp[i-2]
  return dp[num]  
  
print(jump(3))
  