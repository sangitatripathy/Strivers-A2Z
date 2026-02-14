function fibonacci(n,memo){
  if(memo[n] !== -1) return memo[n]
  if(n == 0) return 0;
  if(n == 1) return 1;
  memo[n]=fibonacci(n-1,memo)+fibonacci(n-2,memo);
  return memo[n]
}

function fibonacci2(num,arr){
  arr[0]=0;
  arr[1]=1;
  for(i=2;i<=num;i++){
    arr[i]= arr[i-1]+arr[i-2]
  }
  return arr[num]
}

let n = 4
const arr = new Array(n+1).fill(-1)
console.log(fibonacci(n,arr))
console.log(fibonacci2(n,arr))