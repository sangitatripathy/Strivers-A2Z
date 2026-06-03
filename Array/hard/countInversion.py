class Solution:
  def inversionCount(self, arr):
    count=0
    def mergesort(low,high):
      if low >= high:
        return
      mid=(low+high)//2
      mergesort(low,mid)
      mergesort(mid+1,high)
      merge(low,mid,high)
      
    def merge(low,mid,high):
      nonlocal count
      left=low
      right=mid+1
      temp=[]
      
      while(left <= mid and right <= high):
        if arr[left] <= arr[right]:
          temp.append(arr[left])
          left+=1
        else:
          temp.append(arr[right])
          count+=(mid-left+1)
          right+=1
        

      while left <= mid:
        temp.append(arr[left])
        left+=1

      while right <= high:
        temp.append(arr[right])
        right+=1

      for i in range(low,high+1):
        arr[i] = temp[i-low]

    mergesort(0,len(arr)-1)
    return count

arr= [2, 4, 1, 3, 5]   
sol = Solution()
print(sol.inversionCount(arr))
        