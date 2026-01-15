class Solution:
    def singleNonDuplicate(self, nums):
        if nums[0] != nums[1]:
            return nums[0]
        low=1
        if nums[-1] != nums[-2]:
            return nums[-1]
        high=len(nums)-2
        while(low <= high):
            mid=(low+high)//2
            if nums[mid] != nums[mid-1] and nums[mid] !=nums[mid+1]:
                return nums[mid]
            if (mid%2 == 1 and nums[mid] == nums[mid-1]) or (mid%2 == 0 and nums[mid] == nums[mid+1]): low=mid+1 
            else: high=mid-1

sol= Solution()
print(sol.singleNonDuplicate([1,1,2,3,3,4,4,8,8]))    
      