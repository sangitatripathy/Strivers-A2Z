def fibonacci(n,memo=None):
  if memo is None:
    memo=[-1]*(n+1)
  if memo[n] != -1:
    return memo[n]
  if n <= 1:
    memo[n]=1
  else:
    memo[n]=fibonacci(n-1)+fibonacci(n-2)
  return memo[n]  

num=int(input("enter a number :"))
print(fibonacci(num))
  
  