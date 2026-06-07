import math

class Solution:
  def minEatingSpeed(self, piles, h): 
      newPiles = sorted(piles)
      maxi=newPiles[-1]
      res=0
      def calctime(hr):
        total=0
        for i in piles:
          total+=math.ceil(i/hr)
        return total
      
      low=1
      high=maxi
      ans=0
      while(low <= high):
        mid=(low+high)//2
        res=calctime(mid)
        if res > h:
          low=mid+1
        elif res <= h:
          ans=mid
          high=mid-1
      return ans

sol = Solution()
piles = [3,6,7,11]
print(sol.minEatingSpeed(piles,8))
          
          
        