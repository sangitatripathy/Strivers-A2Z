class Solution:
    def singleNumber(self, nums):
      freq={}
      for i in range(len(nums)):
        if nums[i] in freq:
          freq[nums[i]] +=1
        else:
          freq[nums[i]] =1
      for key,value in freq.items():
        if value == 1:
          return key


sol= Solution()
sol.singleNumber([4,1,2,1,2])