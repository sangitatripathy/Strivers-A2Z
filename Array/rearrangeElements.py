def rearrangeArray(nums):
  ans=[0]*len(nums)
  pos,neg=0,0
  for i in range(len(nums)):
      if nums[i] > 0:
          ans[pos*2]=nums[i]
          pos+=1
      else:
          ans[neg*2+1]=nums[i]
          neg+=1
  return ans

print(rearrangeArray([3,1,-2,-5,2,-4]))