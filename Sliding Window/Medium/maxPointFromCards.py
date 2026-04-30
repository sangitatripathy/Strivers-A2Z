class Solution:
    def maxScore(self, cardPoints,k):
      lsum,rsum=0,0
      maxi=0
      for i in range(0,k):
        lsum+=cardPoints[i]
        maxi=max(maxi,lsum)
      rind=len(cardPoints)-1
      for i in range(k-1,-1,-1):
        lsum= lsum-cardPoints[i]
        rsum = rsum+cardPoints[rind]
        maxi=max(maxi,lsum+rsum)
        rind-=1
      return maxi
cardPoints = [1,2,3,4,5,6,1]
k = 3
sol= Solution()
print(sol.maxScore(cardPoints,k))
        
        