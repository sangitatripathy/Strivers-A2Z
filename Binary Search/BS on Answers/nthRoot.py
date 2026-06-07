class Solution:
  def nthRoot(self, n, m):
    if m==0:
      return 0
    low=1
    high=m
    ans=-1
    while low <= high:
      mid=(low+high)//2
      val=1
      for _ in range(n):
        val*=mid
        if val > m:
          break
        
      if val < m:
        low=mid+1
      elif val > m:
        high=mid-1
      else:
        return mid
    return ans
    
        
sol = Solution()
print(sol.nthRoot(4,16))
      

       
