def searchInSorted(arr, k):
  for i in arr:
    if i == k:
      return True
  return False
print(searchInSorted([2, 3, 5, 6],1))