function backtrack(curr,ind,target,res,candidates){
  if (target == 0){
    res.push([...curr])
    return
  }
  if (target < 0) return;
  let prev = -1
  for (let i=ind;i<candidates.length;i++){
    if(candidates[i] === prev) continue;
    curr.push(candidates[i])
    backtrack(curr,i+1,target-candidates[i],res,candidates)
    curr.pop()
    prev = candidates[i]
  }
}

let arr=[10,1,2,7,6,1,5].sort((a, b) => a - b)
let res= []
backtrack([],0,8,res,arr)
console.log(res)