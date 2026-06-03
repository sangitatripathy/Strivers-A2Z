class Solution:
  def maxLength(self, arr):
    seen={}
    maxi=0
    pSum=0
    seen[0] = -1
    for i in range(len(arr)):
        pSum+=arr[i]
        if pSum in seen:
            pInd= seen[pSum]
            length = i-pInd
            maxi=max(maxi,length)
        else:
            seen[pSum] = i
    return maxi

sol = Solution()
arr= [15, -2, 2, -8, 1, 7, 10, 23]
print(sol.maxLength(arr))