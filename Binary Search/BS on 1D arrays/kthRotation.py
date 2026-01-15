def findKRotation(nums):
  n=len(nums)-1
  ans=0
  if nums[0] < nums[n]:
    return 0
  else:
    minimum=float('inf')
    low=0
    high=len(nums)-1
    while(low <= high):
      mid=(low+high)//2
      if(nums[low] <= nums[mid]):
        if nums[low] < minimum:
          minimum=nums[low]
          ans=low
        low=mid+1
      else:
        if nums[mid] < minimum:
          minimum=nums[mid]
          ans=mid
        high=mid-1
    return ans

# nums = [4,5,6,7,0,1,2]

nums=[5,1,2,3,4]
print(findKRotation(nums))