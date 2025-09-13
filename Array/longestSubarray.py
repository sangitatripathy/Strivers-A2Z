def longestSubarray(arr,k):
  len_max=0
  sum=0
  map={}
  for i in range (len(arr)):
    sum+=arr[i]
    if sum == k :
      len_max=max(len_max,i+1)
    if (sum-k) in map:
      len_max=max(len_max,i-map[sum-k])
    if sum not in map: 
      map[sum]=i
  return len_max

print(longestSubarray([3,0,1,1,2,4],4))
  