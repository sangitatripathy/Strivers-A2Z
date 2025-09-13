def sortedOrNot(arr):
  for i in range (len(arr)-1):
    if (arr[i]<=arr[i+1]):
      continue
    else:
      return False
  return True

print(sortedOrNot([90, 80, 100, 70, 40, 30]))