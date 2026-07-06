def heapify(arr,n,i):
  largest=i
  left=2*i+1
  right = 2*i+2
  if left < n and arr[left] > arr[largest]:
    largest=left
  if right < n and arr[right] > arr[largest]:
    largest = right
  if largest != i:
    arr[i],arr[largest] = arr[largest],arr[i]
    heapify(arr,n,largest)

def heapSort(arr):
  n= len(arr)
  for i in range((n-1)//2,-1,-1):
    heapify(arr,n,i)
  for i in range(n-1,0,-1):
    arr[0],arr[i] = arr[i],arr[0]
    heapify(arr,i,0)
  
def kthLargest(arr,k):
  heapSort(arr)
  n=len(arr)
  return arr[n-k]

arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
print(kthLargest(arr,4))