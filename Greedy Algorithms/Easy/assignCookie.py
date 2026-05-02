def maxChildren( greed, cookie):
  greed.sort()
  cookie.sort()
  i=0
  j=0
  count=0
  while i<len(greed) and j<len(cookie):
    if cookie[j] >= greed[i]:
      i+=1
      j+=1
      count+=1
    else:
      j+=1
  return count

greed=[1,10,3]
cookie=[1,2,3]
print(maxChildren(greed,cookie))