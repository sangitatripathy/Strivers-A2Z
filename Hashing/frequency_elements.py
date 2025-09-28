def frequencyCount(arr):
  list=[0]*len(arr)
  for i in arr:
    list[i-1]+=1
  return list

arr= [3, 3, 3, 3]
print(frequencyCount(arr))