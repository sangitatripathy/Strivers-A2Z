def largest(arr):
  largest=arr[0]
  for i in range (1,len(arr)):
      if arr[i] >largest:
          largest=arr[i]
  return largest

print(largest([1, 8, 7, 56, 90]))