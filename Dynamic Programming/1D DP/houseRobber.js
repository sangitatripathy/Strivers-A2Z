var maxCost = function(ind,nums,dp){
  if(ind == 0) return nums[0]
  if(ind < 0) return 0;
  if(dp[ind] != -1) return dp[ind]
  let pick = nums[ind]+maxCost(ind-2,nums,dp)
  let notpick= maxCost(ind-1,nums,dp)
  dp[ind] = Math.max(pick,notpick)
  return dp[ind]
}
var rob = function(nums) {
    let dp = new Array(nums.length).fill(-1)
    return(maxCost(nums.length-1,nums,dp))
};

num = [2,7,9,3,1]
nums = [0]
console.log(rob(nums));
console.log(rob(num));
