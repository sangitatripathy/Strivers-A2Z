class Solution {
    floorSqrt(n) {
       let low=1
       let high=n
       let ans=1
       while(low <= high){
        let mid = Math.floor((low+high)/2)
        if(mid*mid <= n){
          ans=mid
          low=mid+1
        }
        else{
          high= mid-1
        }
       } 
      return ans
    }
}

const sol = new Solution()

console.log(sol.floorSqrt(28))