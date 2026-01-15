class Solution:
    def nextGreaterElement(self, nums1):
      # ans=[]
      # for n in nums1 :
      #   x=nums2.index(n)
      #   found=-1
      #   for j in range(x+1,len(nums2)):
      #     if nums2[j] > n:
      #       found=nums2[j]
      #       break
      #   ans.append(found)
      # return ans   
      nge=[]
      stack=[]
      for item in nums1[::-1]:
        if not stack :
          nge.append(-1)
          stack.append(item)
          continue
        if stack and stack[-1] > item:  
          nge.append(stack[-1]) 
          stack.append(item)   
        else:
          while stack and stack[-1] <= item:
            stack.pop()
          if stack: nge.append(stack[-1])
          else: nge.append(-1)
          stack.append(item)
      nge.reverse()
      return nge       
sol=Solution()
nums1=[4,12,5,3,1,2,5,3,1,2,4,6]
print(sol.nextGreaterElement(nums1))       