def maxConsecutive(arr):
  max=0
  count =0
  for i in arr:
    if i == 1:
      count+=1
      if max < count:
        max=count
    else:
      count=0
  return max

print(maxConsecutive([1,1,0,1,1,1,0]))