var subsequence = function(ind,nums,temp=[],res){
  if(ind === nums.length){
    res.push([...temp])
    return
  }
  temp.push(nums[ind])
  subsequence(ind+1,nums,temp,res)
  temp.pop()
  subsequence(ind+1,nums,temp,res)
}

var subsets = function(nums) {
  let res =[];
  subsequence(0,nums,[],res)
  return res
};

console.log(subsets([1,2,3]))