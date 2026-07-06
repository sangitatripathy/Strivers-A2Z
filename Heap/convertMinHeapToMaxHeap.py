def maxHeapify(arr,n,i):
  largest=i
  left = 2*i+1
  right = 2*i+2
  if left < n and arr[left] > arr[largest]:
    largest=left
  if right < n and arr[right] > arr[largest]:
    largest = right
  if largest != i:
    arr[i],arr[largest] = arr[largest],arr[i]
    maxHeapify(arr,n,largest)
    
def minToMaxHeap(arr):
  n=len(arr)
  for i in range((n-1)//2,-1,-1):
    maxHeapify(arr,n,i)

arr=[3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
minToMaxHeap(arr)
print(arr)