def subarraySum(nums,k):
  # count=0
  # for i in range (len(nums)):
  #   sum=nums[i]
  #   if sum == k :
  #     count+=1
  #   for j in range (i+1,len(nums)):
  #       sum+=nums[j]
  #       if sum == k :
  #         count+=1
  # return count
  seen={0:1}
  prefix=0
  count=0
  for i in range (len(nums)):
    prefix+=nums[i]
    if prefix-k in seen:
      count+=seen[prefix-k]
    seen[prefix]=seen.get(prefix,0)+1
  return count
          

print(subarraySum([1, 2, 3, -3, 1, 1, 1, 4, 2, -3],3))
      