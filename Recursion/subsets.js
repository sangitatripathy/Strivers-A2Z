// var subsequence = function(ind,nums,temp=[],res){
//   if(ind === nums.length){
//     res.push([...temp])
//     return
//   }
//   temp.push(nums[ind])
//   subsequence(ind+1,nums,temp,res)
//   temp.pop()
//   subsequence(ind+1,nums,temp,res)
// }

// var subsets = function(nums) {
//   let res =[];
//   subsequence(0,nums,[],res)
//   return res
// };

var subsetsWithDup = function(nums) {
  let res=[]
  let subsets = 1 << nums.length
  for(let i=0;i<subsets;i++){
    let list=[]
    for(let j=0; j<nums.length;j++){
      if(i & 1<<j) list.push(nums[j])
    }
  let sum = list.reduce((acc,cv)=>acc+cv,0)
  res.push(sum)
  }
  return res
};

console.log(subsetsWithDup([1,2,3]))
// console.log(subsets([1,2,3]))