def removeDuplicates(arr):
  count=0
  for i in range (1,len(arr)):
    if arr[i] == arr[count]:
        continue
    else:
        count+=1
        arr[count]=arr[i]
  return arr[0:count+1]

print(removeDuplicates([2,2,3,4,5,7]))