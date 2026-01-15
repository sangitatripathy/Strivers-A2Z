class Solution:
    def findPeakElement(self, nums) -> int:
      n=len(nums)
      if n == 1:
        return 0
      if nums[0] > nums[1]:
        return 0
      if nums[n-1] < nums[n-2]:
        return n-1   
      low=1
      high=n-2
      while (low <= high):
        mid=(low+high)//2
        if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1] :
          return mid
        elif(nums[mid] > nums[mid-1]):
          low=mid+1
        else:
          high=mid-1
      return -1

sol=Solution()
print(sol.findPeakElement([1,2,1,3,2]))
            