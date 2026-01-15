def searchInsert(arr, x):
  low=0
  high=len(arr)-1
  ans=len(arr)
  while low <= high :
    mid=(low+high)//2
    if arr[mid] == x:
      return mid
    elif(arr[mid] > x):
      high=mid-1
    else:
      low=mid+1
  return low 

print(searchInsert([1,3,5,6],7))
