class Solution:
    def myAtoi(self, s: str) -> int:
        # if len(s) == 0:
        #   return 0
        # i=0
        # n=len(s)
        # sign=1
        # num=0
        # while i < n and s[i] == " ":
        #   i+=1
        # while i < n and( s[i] == '+' or s[i] =='-'):
        #   if s[i] == '-':
        #     sign = -1
        #   i+=1
        # while i < n and s[i].isdigit():
        #   digit = ord(s[i])-ord('0')
        #   if num > (2**31-1) // 10 or (num == (2**31 -1) // 10 and digit > 7):
        #     return 2**31-1 if sign==1 else -2**31
        #   num=num*10+digit
        #   i+=1
        # return sign*num
        n=len(s)
        def findNum(i,started,num,sign):
          if i == n:
            return sign*num
          if not started and s[i] ==" ":
            return findNum(i+1,False,num,sign)
          if not started and (s[i] == '+' or s[i] =='-'):
            if s[i] == '-':
              sign=-1
            return findNum(i+1,True,num,sign)
          if s[i].isdigit():
            digit = ord(s[i])-ord('0')
            if num > (2**31-1)//10 or (num == (2**31-1)//10 and digit > 7):
              return 2**31-1 if sign == 1 else -2**31
            return findNum(i+1,True,num*10+digit,sign)
          return sign*num
        return findNum(0,False,0,1)
            
        