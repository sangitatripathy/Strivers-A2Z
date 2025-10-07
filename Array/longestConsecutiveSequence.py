def longestConsecutive(nums):
  if not nums :
    return 0
  # nums.sort()
  # count=1
  # maxlen=1
  # for i in range (1,len(nums)):
  #   if nums[i] == nums[i-1]:
  #     continue
  #   elif nums[i-1] == nums[i]-1:
  #     count+=1 
  #     maxlen=max(maxlen,count)
  #   else:
  #     count=1
  # return maxlen
  numsSet=set(nums)
  maxlen=0
  for n in numsSet:
    if n-1 not in numsSet:
      length=1
      curr=n
      while curr+1 in nums:
        length+=1
        curr=curr+1
      maxlen=max(length,maxlen)
  return maxlen
      
print(longestConsecutive([102,4,100,1,101,3,2,1]))
print(longestConsecutive([0,0]))