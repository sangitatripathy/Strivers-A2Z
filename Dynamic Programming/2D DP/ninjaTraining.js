class Solution {
  calcMax(ind, last, arr, dp) {
    if (dp[ind][last] != -1) return dp[ind][last];
    if (ind == 0) {
      let max = 0;
      for (let i = 0; i <= 2; i++) {
        if (i != last) max = Math.max(max, arr[0][i]);
      }
      return (dp[ind][last] = max);
    }
    let maxi = 0;
    for (let i = 0; i <= 2; i++) {
      if (i != last) {
        const pt = arr[ind][i] + this.calcMax(ind - 1, i, arr, dp);
        maxi = Math.max(maxi, pt);
      }
    }
    return (dp[ind][last] = maxi);
  }
  computeMax(n, dp, arr) {
    dp[0][0] = Math.max(arr[0][1], arr[0][2]);
    dp[0][1] = Math.max(arr[0][0], arr[0][2]);
    dp[0][2] = Math.max(arr[0][0], arr[0][1]);
    dp[0][3] = Math.max(arr[0][0], Math.max(arr[0][1], arr[0][2]));

    for (let day = 1; day < n; day++) {
      for (let last = 0; last < 4; last++) {
        dp[day][last] = 0;

        for (let task = 0; task <= 2; task++) {
          if (task !== last) {
            const point = arr[day][task] + dp[day - 1][task];
            dp[day][last] = Math.max(dp[day][last], point);
          }
        }
      }
    }
    return dp[n - 1][3];
  }
  maximumPoints(arr) {
    const rows = arr.length;
    const col = 4;
    const dp = Array.from({ length: rows }, () => new Array(col).fill(-1));
    const res = this.calcMax(arr.length - 1, 3, arr, dp);
    const res2= this.computeMax(rows,dp,arr)
    return [res,res2];
  }
}

const sol = new Solution();

const mat = [
  [1, 2, 5],
  [3, 1, 1],
  [3, 3, 3],
];

console.log(sol.maximumPoints(mat));
