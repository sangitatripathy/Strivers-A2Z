def search(nums,target):
  low=0
  high=len(nums)-1
  while low<=high:
    mid=(low+high)//2
    if nums[mid] == target:
      return True
    if nums[mid] == nums[low] == nums[high]:
      low=mid+1
      high=mid-1
      continue
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
  return False
# print(search([7,8,1,2,3,3,3,4,5,6],3))
print(search([1,0,1,1,1],0))
  
      