var countPath = function(i,j,matrix,dp){
  if( i < 0 || j < 0 || matrix[i][j]==1) return 0;
  if(i==0 && j==0) return dp[i][j] = 1;
  if(dp[i][j] != -1) return dp[i][j];
  let left= countPath(i,j-1,matrix,dp)
  let up = countPath(i-1,j,matrix,dp)
  return dp[i][j] = left+up
}

var uniquePathsWithObstacles = function(obstacleGrid) {
    r = obstacleGrid.length
    c = obstacleGrid[0].length
    const dp = Array.from({length:r},()=>Array(c).fill(-1))
    return countPath(r-1,c-1,obstacleGrid,dp)
};

const obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
console.log(uniquePathsWithObstacles(obstacleGrid))