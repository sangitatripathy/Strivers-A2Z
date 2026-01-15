def search(nums,target):
  low=0
  high=len(nums)-1
  while low<=high :
    mid=(low+high)//2
    if nums[mid] == target:
      return mid
    elif nums[low] > nums[mid]:
      if nums[mid] < target <= nums[high]:
        low=mid+1
      else:
        high=mid-1
    else:
      if nums[low] <= target < nums[mid]:
        high=mid-1
      else:
        low=mid+1
  return -1
# print(search([7,8,1,2,3,3,3,4,5,6],3))
print(search([2,5,6,0,0,1,2],3))
  
      