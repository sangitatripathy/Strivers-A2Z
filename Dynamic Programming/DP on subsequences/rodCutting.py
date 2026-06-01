class Solution:
  def cutRod(self, price):
    n=len(price)
    def countRod(ind,length):
      if ind == 0:
        return price[0]*length
      notTake= countRod(ind-1,length)
      rodlen=ind+1
      take=float("-inf")
      if rodlen <= length:
        take= price[ind]+countRod(ind,length-rodlen)
      return max(notTake,take)
    return countRod(n-1,n)
        