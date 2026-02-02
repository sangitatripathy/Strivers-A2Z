var subset = function(sum,ind,seq,k,res){
  if (sum === 0 && seq.length === k){
    res.push([...seq])
    return
  }
  if(sum < 0 || seq.length > k) return;
  for(let i=ind; i<=9; i++){
    seq.push(i)
    subset(sum-i,i+1,seq,k,res)
    seq.pop()
  }
}
var combinationSum3 = function(k, n) {
  let res=[]
  subset(n,1,[],k,res)
  return res
};

console.log(combinationSum3(3,9));

