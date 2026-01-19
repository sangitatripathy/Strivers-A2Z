class Solution:
  def myPow(self, x: float, n: int):
    if n==0:
      return 1
    if n%2 == 0:
      self.myPow(x*x,n//2)
    elif n%2 == 1 :
      self.myPow(x*x,(n-1)//2)
      
      