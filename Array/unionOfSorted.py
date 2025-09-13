def findUnion(a, b):
  i,j=0,0
  res=[]
  while(i<len(a) and j <len(b)):
    if a[i] < b[j]:
      if not res or res[-1]!=a[i]:
        res.append(a[i])
      i+=1
    elif b[j] < a[i]:
      if not res or res[-1]!=b[j]:
        res.append(b[j])
      j+=1
    else:
      if not res or res[-1]!=a[i]:
        res.append(a[i])
      i+=1
      j+=1
  while i < len(a):
    if not res or res[-1]!=a[i]:
        res.append(a[i])
    i+=1
  while j < len(b):
    if not res or res[-1]!=b[j]:
        res.append(b[j])
    j+=1
  return res

print(findUnion([4,5,7,7,7],[3,4,6,8]))
      