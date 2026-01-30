class Solution {
    binaryString(cur,n,res){
      if (cur.length === n){
        res.push(cur)
        return 
      }
      this.binaryString(cur+"0",n,res)
      this.binaryString(cur+"1",n,res)
    }
    binstr(n) {
      let res=[]
      this.binaryString("",n,res)
      return res
    }
}

let sol = new Solution()
console.log(sol.binstr(3))