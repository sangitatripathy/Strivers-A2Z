class Solution {
    appendString(curr,n,res){
      if (curr.length === n ){
        res.push(curr)
        return 
      }
      this.appendString(curr+"0",n,res)
      if (curr.length === 0 || curr[curr.length-1]!=1){
        this.appendString(curr+"1",n,res)
      }
    }
    countStrings(n) {
      let res=[]
      this.appendString("",n,res)
      return res
    }
}

let sol = new Solution()
console.log(sol.countStrings(3))