class Solution {
    smallestPath(height,dp,ind){
        if(ind == 0) return dp[ind]=0;
        if(ind == 1) return dp[ind]=Math.abs(height[ind]-height[ind-1])
        if(dp[ind] != -1) return dp[ind];
        let jumpTwo = Infinity
        if(ind > 1){
            jumpTwo = this.smallestPath(height,dp,ind-2)+Math.abs(height[ind]-height[ind-2])
        }
        let jumpOne = this.smallestPath(height,dp,ind-1)+Math.abs(height[ind]-height[ind-1])
        dp[ind] = Math.min(jumpTwo,jumpOne)
        return dp[ind]
    }
    minCost(height) {
        let dp= new Array(height.length).fill(-1)
        const res= this.smallestPath(height,dp,height.length-1)
        return res
        // dp[0] = 0;
        // dp[1] = Math.abs(height[1]- height[0]);
        // for(i=2;i<height.length;i++){
        //   let jumpOne = dp[i-1]+Math.abs(height[i]-height[i-1])
        //   let jumpTwo = dp[i-2]+Math.abs(height[i]-height[i-2])
        //   dp[i] = Math.min(jumpOne,jumpTwo)
        // }
        // return dp[height.length-1]
    }
}

const sol = new Solution()
const height = [10,30,40,20,50]
console.log(sol.minCost(height));

