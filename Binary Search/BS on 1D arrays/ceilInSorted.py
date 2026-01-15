def ceilInSorted(arr, target):
  low=0
  high=len(arr)-1
  ans=-1
  while low <= high :
    mid=(high+low)//2
    if arr[mid] < target :
      low=mid+1
    else:
      ans=mid
      high=mid-1    
  return ans
      
print(upperBound([1, 2, 8, 10, 10, 12, 19],3))