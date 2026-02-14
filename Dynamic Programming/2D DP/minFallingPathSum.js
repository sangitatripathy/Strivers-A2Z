var calMinPath =(matrix,dp)=>{
  const n = matrix.length
  const r = matrix[0].length
  for(let j=0;j<r;j++){
    dp[n-1][j] = matrix[n-1][j]
  }
  for(let i=n-2; i>=0; i--){
    for(let j=0;j<r;j++){
      let down = dp[i+1][j]
      let left = j > 0 ? dp[i+1][j-1] : Infinity;
      let right = j < r-1 ?  dp[i+1][j+1] : Infinity;
      dp[i][j] = matrix[i][j] + Math.min(down,Math.min(left,right))
    }
  }
  return Math.min(...dp[0])
}

var minFallingPathSum = function(matrix) {
    const dp = matrix.map(row => Array(row.length).fill(-1))
    return calMinPath(matrix,dp)
};

const matrix = [[2,1,3],[6,5,4],[7,8,9]]
console.log(minFallingPathSum(matrix))