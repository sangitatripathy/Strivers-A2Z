class Solution:
  def merge(self, intervals):
    sortedInt=sorted(intervals)
    i=0
    n= len(intervals)
    ans=[]
    while i < n:
      start,end=sortedInt[i]
      j=i+1
      while j<n and end >= sortedInt[j][0]:
        end=max(end,sortedInt[j][1])
        j+=1
      ans.append([start,end])
      i=j
    return ans

sol = Solution()
arr=[[4,7],[1,4]]
print(sol.merge(arr))
      
        