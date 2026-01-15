def findMin(nums):
  minimum=float('inf')
  low=0
  high=len(nums)-1
  while(low <= high):
    mid=(low+high)//2
    if(nums[low] <= nums[mid]):
      minimum=min(nums[low],minimum)
      low=mid+1
    else:
      minimum=min(nums[mid],minimum)
      high=mid-1
  return minimum

nums = [4,5,6,7,0,1,2]
print(findMin(nums))