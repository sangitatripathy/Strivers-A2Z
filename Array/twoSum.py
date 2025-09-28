arr=[3,2,4]
def twosum(arr,k):
  map1={}
  for i,v in enumerate(arr):
    if k-v in map1:
      return [map1[k-v],i]
    map1[v]=i
  return []
print(twosum(arr,6))

def twosumopt(arr,k):
  arr=[(v,i) for i,v in enumerate(arr) ]
  arr.sort(key=lambda x:x[0])
  left=0
  right=len(arr)-1
  while left <= right:
    temp=arr[left][0]+arr[right][0]
    if temp < k:
      left+=1
    elif temp > k:
      right-=1
    else:
      return [arr[left][1],arr[right][1]]
  return []

print(twosumopt(arr,6))

