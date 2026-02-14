function jump(num){
  if( num ==1 )return 1;
  const dp = new Array(num).fill(-1)
  dp[0]=1
  dp[1]=1
  for(let i=2;i<=num+1;i++)
    dp[i]=dp[i-1]+dp[i-2]
  return dp[num] 
}
  
console.log(jump(5));

  