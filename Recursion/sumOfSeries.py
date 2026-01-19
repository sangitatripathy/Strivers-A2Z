def sumOfSeries(n:int):
  if n==0:
    return 0
  return (n**3)+sumOfSeries(n-1)
print(sumOfSeries(5))