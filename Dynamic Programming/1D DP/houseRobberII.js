var maxMoney = (nums,ind,dp) =>{
  if(ind == 0) return nums[0];
  if(ind < 0) return 0;
  if(dp[ind] != -1) return dp[ind];
  let pick = nums[ind]+maxMoney(nums,ind-2,dp)
  let notPick = maxMoney(nums,ind-1,dp)
  dp[ind] = Math.max(pick,notPick)
  return dp[ind]
}
var rob = function(nums) {
  let n = nums.length;
  if(n===1) return nums[0]
  let dp1 = new Array(n-1).fill(-1);
  let dp2 = new Array(n-1).fill(-1);
  left=maxMoney(nums.slice(0,n-1),n-2,dp1)
  right=maxMoney(nums.slice(1),n-2,dp2)
  return Math.max(left,right)
};

// let nums = [1,2,3]
let nums = [1]
console.log(rob(nums));
