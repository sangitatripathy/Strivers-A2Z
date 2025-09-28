def leaders(arr):
  n=len(arr)
  i=n-2
  res=[]
  res.append(arr[n-1])
  while i >= 0 :
    if arr[i] >= res[-1]:
      res.append(arr[i])
    i-=1
  res.reverse()
  return res
print(leaders([30, 10, 10, 5]))
    
    
  