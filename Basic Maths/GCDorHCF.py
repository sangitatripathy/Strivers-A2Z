def lcmandgcd(a:int,b:int):
  if a==b :
    return a
  else:
    temp=min(a,b)
    gcd=1
    for i in range (1,temp+1):
      if a%i == 0 and b%i == 0:
        gcd=i
    lcm=(a*b)//gcd
    return [lcm,gcd]

print(lcmandgcd(1000,1000))
  