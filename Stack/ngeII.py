class Solution:
    def nextGreaterElements(self, nums):
      res=[]
      n=len(nums)
      for i in range(n):
        found=False
        for j in range(i+1,i+n):
          ind= j%n
          if nums[ind] > nums[i]:
            found=True
            res.append(nums[ind])
            break
        if not found:
          res.append(-1)
      return res
sol = Solution()
nums1 = [1,2,3,4,3]
print(sol.nextGreaterElements(nums1))
          