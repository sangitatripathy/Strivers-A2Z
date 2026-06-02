class Solution:
    def fourSum(self, nums, target):
      # s=set()
      # for i in range(len(nums)):
      #   for j in range(i+1,len(nums)):
      #     freq={}
      #     for k in range(j+1,len(nums)):
      #       fourth = target-(nums[i]+nums[j]+nums[k])
      #       if fourth in freq:
      #         quadra = tuple(sorted([nums[i],nums[j],nums[k],fourth]))
      #         if quadra not in s:
      #           s.add(quadra)
      #       freq[nums[k]] = 1
      # return [list(t) for t in s]

      nums.sort()
      n=len(nums)
      ans=[]
      for i in range(n):
        if (i > 0 and nums[i] == nums[i-1]): continue
        for j in range(i+1,n):
          if (j > i+1 and nums[j] == nums[j-1]): continue
          k=j+1
          l=n-1
          while k <l:
            sum = nums[i]+nums[j]+nums[k]+nums[l]
            if sum < target:
              k+=1
            elif sum > target:
              l-=1
            else:
              ans.append([nums[i],nums[j],nums[k],nums[l]])
              k+=1
              l-=1
              while (k < l and nums[k] == nums[k-1]):k+=1
              while(k < l and nums[l] == nums[l+1]):l-=1
      return ans
              
              
              

sol = Solution()
print(sol.fourSum([1,0,-1,0,-2,2],0))
                