class Solution:
    def subArrayRanges(self, nums):
      def subArrayMaxs(nums):
        n=len(nums)
        left=[0]*n
        right=[0]*n
        stack=[]
        total=0
        for i in range(n):
          count=1
          while stack and stack[-1][0] < nums[i]:
            count+=stack.pop()[1]
          stack.append((nums[i],count))
          left[i] = count
        stack=[]
        for i in range(n-1,-1,-1):
          count=1
          while stack and stack[-1][0] <= nums[i]:
            count+=stack.pop()[1]
          stack.append((nums[i],count))
          right[i] = count
        for i in range(n):
          total+=(nums[i]*left[i]*right[i])
        return total
      
      def subArrayMins(nums):
        n=len(nums)
        left=[0]*n
        right=[0]*n
        stack=[]
        total=0
        for i in range(n):
          count=1
          while stack and stack[-1][0] > nums[i]:
            count+=stack.pop()[1]
          stack.append((nums[i],count))
          left[i] = count
        stack=[]
        for i in range(n-1,-1,-1):
          count=1
          while stack and stack[-1][0] >= nums[i]:
            count+=stack.pop()[1]
          stack.append((nums[i],count))
          right[i] = count
        for i in range(n):
          total+=(nums[i]*left[i]*right[i])
        return total

      return subArrayMaxs(nums)-subArrayMins(nums)

sol=Solution()
nums = [1,2,3]
print(sol.subArrayRanges(nums))