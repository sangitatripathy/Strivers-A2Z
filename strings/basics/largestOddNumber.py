class Solution:
    def largestOddNumber(self, num):
      for i in range(len(num)-1,-1,-1):
        if(int(num[i])%2 == 1):
          return num[:i+1]
      return ""
sol= Solution()
print(sol.largestOddNumber("35427"))
          
      