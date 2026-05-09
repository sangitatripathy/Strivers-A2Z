class Solution:
    def calcSum(self,nums,goal):
      if goal < 0:
        return 0
      left,right,s,count=0,0,0,0
      while(right < len(nums)):
        s+=(nums[right] %2)
        while s > goal:
          s-=(nums[left] %2)
          left+=1
        count+=right-left+1
        right+=1
      return count
    def numSubarraysWithSum(self, nums, goal):
      return self.calcSum(nums,goal)-self.calcSum(nums,goal-1)

sol= Solution()
nums = [1,0,1,0,1]
goal = 2
print(sol.numSubarraysWithSum(nums,goal))
        