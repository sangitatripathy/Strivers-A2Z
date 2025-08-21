def armstrongNumber (n):
  org=n
  res=0
  while n  > 0 :
    temp=n%10
    res+=temp**3
    n=n//10
  return res == org

print(armstrongNumber(153))
