def moveZeroToEnd(arr):
  count=0
  for i in range (len(arr)):
    if arr[i] == 0:
      continue
    else:
      arr[count] = arr[i]
      count+=1
  arr[count:]=[0]*(len(arr)-count)
  return arr
print(moveZeroToEnd([1,0,2,3,2,0,0,4,5,1]))
      