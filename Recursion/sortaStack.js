class Solution {
    insertStack(st,x){
        if (st.length === 0 || st[st.length -1] <= x){
            st.push(x)
            return
        }
        let top = st.pop()
        this.insertStack(st,x)
        st.push(top)
    }
    sortStack(st) {
        if (st.length === 0) return;
        let top = st.pop()
        this.sortStack(st)
        this.insertStack(st,top)
    }
}

let num = new Solution()
let stack = [41,3,32,11,2]
num.sortStack(stack)
console.log(stack)  