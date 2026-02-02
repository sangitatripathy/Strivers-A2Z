var subsetsWithDup = function(nums) {

}

var subsets = function(nums,ind,seq,res){
  res.push([...seq])
  for(let i =ind ; i < nums.length ; i++){
    if (i > ind && nums[i] === nums[i - 1]) continue
    seq.push(nums[i])
    subsets(nums,i+1,seq,res)
    seq.pop()
  }
}

let res =[]
let nums = [1,2,2]
subsets(nums,0,[],res)
console.log(res)