var calcMinpathSum = (i,j,grid,dp) => {
  if( i==0 && j== 0) return dp[i][j] = grid[i][j]
  if(i<0 || j<0) return Number.MAX_VALUE
  if( dp[i][j] != -1 ) return dp[i][j]
  let left = calcMinpathSum(i,j-1,grid,dp)
  let up = calcMinpathSum(i-1,j,grid,dp)
  return dp[i][j] = grid[i][j]+Math.min(left,up)
}
var minPathSum = function(grid) {
    let r = grid.length;
    let c = grid[0].length;
    const dp = Array.from({length:r},()=>Array(c).fill(-1))
    return calcMinpathSum(r-1,c-1,grid,dp)
};

const grid = [[1,3,1],[1,5,1],[4,2,1]]
console.log(minPathSum(grid))