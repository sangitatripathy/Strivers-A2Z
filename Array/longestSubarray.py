def longestSubarray(arr,k):
  # maxi=0
  # for i in range(len(arr)):
  #   for j in range(i,len(arr)):
  #     count,curr_sum=0,0
  #     for l in range(i,j+1):
  #       curr_sum+=arr[l]
  #       count+=1
  #       if curr_sum == k:
  #         maxi=max(maxi,count)
  # return maxi

  # left=0
  # right=0
  # sum=0
  # maxi=0
  # while right < len(arr):
  #   sum+=arr[right]
  #   while sum > k:
  #     sum-=arr[left]
  #     left+=1
  #   if sum == k:
  #     maxi=max(maxi,right-left+1)
  #   right+=1
  # return maxi

  prefSum=0
  prefDict={}
  maxi=0
  for i in range(len(arr)):
    prefSum+=arr[i]
    
    if prefSum == k:
      maxi=max(maxi,i+1)
      
    if(prefSum-k) in prefDict:
      length= i-prefDict[prefSum-k]
      maxi=max(maxi,length)

    if prefSum not in prefDict:
      prefDict[prefSum] = i
      
  return maxi
    
print(longestSubarray([3,0,1,1,2,4],4))
  