const numMap={
  "1":"",
  "2":["a","b","c"],
  "3":["d","e","f"],
  "4":["g","h","i"],
  "5":["j","k","l"],
  "6":["m","n","o"],
  "7":["p","q","r","s"],
  "8":["t","u","v"],
  "9":["w","x","y","z"]
}
var combArray = function(ind,key,res,seq){
  if(ind == key.length){
    res.push(seq)
    return
  }
  let letters = numMap[key[ind]]
  for(let ch of letters){
    combArray(ind+1,key,res,seq+ch)
  }
}

var letterCombinations = function(digits) {
    let res=[]
    combArray(0,digits,res,"")
    return res
};

console.log(letterCombinations("234"));