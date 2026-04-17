class Solution:
    def sumSubarrayMins(self, arr):
      # ans=0
      # mod=1e9+7
      # for i in range(len(arr)):
      #   mini=arr[i]
      #   for j in range(i,len(arr)):
      #     mini=min(arr[j],mini)
      #     ans=(ans+mini)%mod
      # return ans
      n=len(arr)
      left=[0]*n
      right=[0]*n
      stack=[]
      total=0
      mod=1e9+7
      for i in range(len(arr)):
        count=1
        while stack and stack[-1][0] > arr[i]:
          count+=stack.pop()[1]
        stack.append((arr[i],count))
        left[i]=count
        
      stack=[]
      for i in range(n-1,-1,-1):
        count=1
        while stack and stack[-1][0] >= arr[i]:
          count+=stack.pop()[1]
        stack.append((arr[i],count))
        right[i] = count
      for i in range(n):
        total=(total+(arr[i]*left[i]*right[i]))%mod
      return total
arr = [3,1,2,4]
sol = Solution()
print(sol.sumSubarrayMins(arr))
          