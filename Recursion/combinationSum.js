var sum = function (ind,candidates,target,seq,res){
  if (ind === candidates.length) return ;
  if (target <= 0){
    res.push([...seq])
    return
  }
  if (candidates[ind] <= target){
    seq.push(candidates[ind])
    sum(ind,candidates,target-candidates[ind],seq,res)
    seq.pop()
  }
  sum(ind+1,candidates,target,seq,res)
}
var combinationSum = function(candidates, target) {
  res=[]
  sum(0,candidates,target,[],res) 
  return res
};

console.log(combinationSum([10,1,2,7,6,1,5],8))