def findFloor(arr, x):
  low=0
  high=len(arr)-1
  ans=-1
  while low <= high :
    mid=(low+high)//2
    if (arr[mid] == x):
      ans=mid
      low=mid+1
    elif(arr[mid] >= x):
      high=mid-1
    else:
      ans=mid
      low=mid+1   
  return ans
print(findFloor([1,3,5,5,5,6],5))

    
  