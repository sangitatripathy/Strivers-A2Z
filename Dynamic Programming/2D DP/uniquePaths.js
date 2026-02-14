//Memoization
var countPath = function (i, j, dp) {
  if (i == 0 && j == 0) {
    dp[i][j] = 1;
  }
  if (i < 0 || j < 0) return 0;
  if (dp[i][j] != -1) return dp[i][j];
  let left = countPath(i, j - 1, dp);
  let up = countPath(i - 1, j, dp);
  return dp[i][j] = left + up;
};

var uniquePaths = function (m, n) {
  const dp = Array.from({ length: m }, () => Array(n).fill(-1));
  return countPath(m - 1, n - 1, dp);
};

//Tabulation
var uniquePaths2 = function(m,n){
  const dp= Array.from({length:m},()=>Array(n).fill(0));
  dp[0][0] = 1
  for(let i=0;i<m;i++){
    for(let j=0; j < n; j++){
      if( i==0 && j==0 ) continue;
      let right= j > 0 ? dp[i][j-1] : 0
      let down = i > 0 ? dp[i-1][j] : 0
      dp[i][j] = right+down
    }
  }
  return dp[m-1][n-1]
}

console.log(uniquePaths(3, 7));
console.log(uniquePaths2(3, 7));
