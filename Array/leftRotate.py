def leftRotate(arr, k):
  d= k%len(arr)
  temp=arr[:d]
  for i in range (d,len(arr)):
    arr[i-d]=arr[i]
  j=0
  for i in range (len(arr)-d,len(arr)):
    arr[i]=temp[j]
    j+=1
  return arr

print(leftRotate([41,67,27,26,69,72,8,2,64,96,8,78,19,48,60],13))
    
  