def getSecondLargest(arr):
  largest=arr[0]
  secondLargest=-1
  for i in range (1,len(arr)):
    if arr[i] > largest :
      secondLargest=largest
      largest=arr[i]
    elif arr[i] < largest and arr[i] >secondLargest:
      secondLargest=arr[i]
  return secondLargest

print(getSecondLargest([10,10,10]))
    