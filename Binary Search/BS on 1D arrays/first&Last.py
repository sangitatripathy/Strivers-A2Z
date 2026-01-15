class Solution:
  def lowerBound(self,arr,x):
    high=len(arr)-1
    low=0
    ans=len(arr)
    while(low <= high):
      mid=(low+high)//2
      if arr[mid] >= x:
        ans = mid 
        high=mid-1
      else :
        low=mid+1
    return ans
  def upperBound(self,arr,x):
    high=len(arr)-1
    low=0
    ans=len(arr)
    while(low <= high):
      mid=(low+high)//2
      if(arr[mid] > x):
        ans=mid
        high=mid-1
      else:
        low=mid+1
    return ans
  def searchRange(self,nums,target):
    first=self.lowerBound(nums,target)
    if(first == len(nums) or nums[first] != target): return 0
    second=self.upperBound(nums,target)
    return (second-first)

arr=[8,9,10,12,12,12]
sol=Solution()
print(sol.lowerBound(arr,12))
print(sol.upperBound(arr,12))
print(sol.searchRange(arr,12))


      