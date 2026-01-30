class Solution {
    reversepush(st,x){
      if (st.length === 0){
        st.push(x)
        return
      }
      let top = st.pop()
      this.reversepush(st,x)
      st.push(top)
    }
    reverseStack(st) {
        if (st.length == 0) return 
        let top= st.pop()
        this.reverseStack(st)
        this.reversepush(st,top) 
    }
}

let num = new Solution()
let stack = [41,3,32,11,2]
num.reverseStack(stack)
console.log(stack)