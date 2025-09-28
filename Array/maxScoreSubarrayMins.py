def maxSum(arr):
  if (len(arr) < 2):
    return 0
  max_sum=float("-inf")
  for i in range (len(arr)):
    for j in range (i+1,len(arr)):
      sub=arr[i:j+1]
      smallest=float("inf")
      sec_small=float("inf")
      for num in sub:
        if num < smallest :
          sec_small= smallest
          smallest=num
        elif num < sec_small :
          sec_small=num
      max_sum=max(max_sum,smallest+sec_small)
  return max_sum  
      
print(maxSum([4,3,5,1]))
      