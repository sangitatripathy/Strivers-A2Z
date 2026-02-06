class Solution {
    minimizeCost(k, arr) {
        let dp = new Array(arr.length).fill(Infinity);
        dp[0]=0;
        for(let i=1;i<arr.length;i++){
          for (let j=1;j<=k;j++){
            if(i-j >=0){
              dp[i] = Math.min(dp[i], dp[i-j]+Math.abs(arr[i]-arr[i-j]))
            }
          }
        }
        return dp[arr.length-1];
    }
}

const sol = new Solution();
const arr = [35, 1, 70, 25, 79, 59,63, 65];
const k =2;
console.log(sol.minimizeCost(k,arr));