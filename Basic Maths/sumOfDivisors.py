def sumOfdivisors(num:int):
  res=0
  for i in range (1,num+1):
    res+=(num//i)*i
  return res

print(sumOfdivisors(1000))