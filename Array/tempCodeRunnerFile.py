n=len(arr)
  i=n-2
  res=[]
  res.append(arr[n-1])
  while i >= 0 :
    if arr[i] >= res[-1]:
      res.append(arr[i])
    i-=1
  return res.reverse()