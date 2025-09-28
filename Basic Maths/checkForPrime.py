from math import sqrt
def checkForPrime(n:int):
  count=0
  for i in range (2,int(sqrt(n))+1):
    if n%i == 0 :
      count+=1
      break
  if count >= 1 :
    return "not prime"
  return "prime"

print(checkForPrime(7))
      