def factorial(n):
  if n ==0:
    return 1
  return n*factorial(n-1)

def factorialNumbers(n):
  res=[]
  for i in range (1,n+1):
    ans=factorial(i)
    if ans <= n :
      res.append(ans)
  return res

print(factorialNumbers(24))

def factorialNumbers(n):
  res=[]
  fact=1
  i=1
  while fact <=n:
    res.append(fact)
    i+=1
    fact*=i
  return res

print(factorialNumbers(24))