class Solution:
    def threeSum(self, nums):
      # s= set()
      # ans=[]
      # for i in range(len(nums)):
      #   for j in range(i+1,len(nums)):
      #     for k in range(j+1,len(nums)):
      #       if nums[i]+nums[j]+nums[k] == 0:
      #         triplet = tuple(sorted([nums[i],nums[j],nums[k]]))
      #         if triplet not in s:
      #           s.add(triplet)
      #           ans.append(list(triplet))
      # return ans

      # s= set()
      # for i in range(len(nums)):
      #   freq={}
      #   for j in range(i+1,len(nums)):
      #     third= -(nums[i]+nums[j])
      #     if third in freq:
      #       triplet= tuple(sorted([nums[i],nums[j],third]))
      #       if triplet not in s:
      #         s.add(triplet)
      #     freq[nums[j]] = 1
      # return [list(t) for t in s]

      n=len(nums)
      nums.sort()
      ans=[]
      for i in range(len(nums)):
        if(i>0 and nums[i] == nums[i-1]): continue
        j=i+1
        k= n-1
        while j < k:
          sum = nums[i]+nums[j]+nums[k]
          if sum < 0:
            j+=1
          elif sum > 0:
            k-=1
          else:
            ans.append([nums[i],nums[j],nums[k]])
            j+=1
            k-=1
            while(j < k and nums[j] == nums[j-1]): j+=1
            while(j < k and nums[k] == nums[k+1]): k-=1
      return ans
            
          
            
            
              
sol= Solution()
nums = [-1,0,1,2,-1,-4]
print(sol.threeSum(nums))