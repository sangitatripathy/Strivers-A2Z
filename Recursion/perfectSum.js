class Solution {
    checkSum(ind,arr,target,sum){
      if (ind == arr.length){
        return sum === target ? 1: 0;
      }
      let choose= this.checkSum(ind+1,arr,target,sum+arr[ind])
      let notChoose = this.checkSum(ind+1,arr,target,sum)
      return choose+notChoose
    }
    perfectSum(arr, target) {
        let res = []
        return this.checkSum(0,arr,target,0);
    }
}

let sol = new Solution;
console.log(sol.perfectSum([3,2,1],3))