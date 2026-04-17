class Solution:
    def nextGreaterElement(self, nums1, nums2):
      res=[]
      for i in nums1:
        x= nums2.index(i)
        found= -1
        for j in range(x+1,len(nums2)):
          if nums2[j] > i:
            found= nums2[j]
            break
        res.append(found)
      return res
sol = Solution()
nums1 = [2,4]
nums2 = [1,2,3,4]
print(sol.nextGreaterElement(nums1,nums2))
