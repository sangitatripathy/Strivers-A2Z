class Solution:
    def isMaxHeap(self, arr):
      def checkHeap(arr,i,n):
        if i >= n:
          return True
        left = 2*i+1
        right = 2*i+2
        if left < n and arr[left] > arr[i]:
          return False
        if right < n and arr[right] > arr[i]:
          return False
        return checkHeap(arr,left,n) and checkHeap(arr,right,n)
      checkHeap(arr,0,len(arr))
sol = Solution()
print(sol.isMaxHeap([90, 15, 10, 7, 12, 2]))