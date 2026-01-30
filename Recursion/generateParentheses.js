var checkParenthesis = function (curr){
  balance = 0
  for (let i=0; i < curr.length;i++){
    if (curr[i] == "(") balance++;
    else balance --
    if (balance < 0) return false
  }
  return balance === 0
}
var validParenthesis = function(n,curr,res) {
  if (curr.length === 2*n){
    if (checkParenthesis(curr)) res.push(curr);
    return
  }
  validParenthesis(n,curr+"(",res)
  validParenthesis(n,curr+")",res)
};

var generateParenthesis = function(n) {
  let res = []
  validParenthesis(n,"",res)
  return res
}

console.log(generateParenthesis(3))