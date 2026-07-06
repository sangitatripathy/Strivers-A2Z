def heapify(arr,n,i):
  smallest=i
  left=2*i+1
  right = 2*i+2
  if left < n and arr[left] < arr[smallest]:
    smallest=left
  if right < n and arr[right] < arr[smallest]:
    smallest = right
  if smallest != i:
    arr[i],arr[smallest] = arr[smallest],arr[i]
    heapify(arr,n,smallest)

def heapSort(arr):
  n= len(arr)
  for i in range((n-1)//2,-1,-1):
    heapify(arr,n,i)
  for i in range(n-1,0,-1):
    arr[0],arr[i] = arr[i],arr[0]
    heapify(arr,i,0)
  
def kthSmallest(arr,k):
  heapSort(arr)
  n=len(arr)
  return arr[n-k]

arr = [7, 10, 4, 3, 20, 15]
print(kthSmallest(arr,3))