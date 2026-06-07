class Solution:
    def removeOuterParentheses(self, s):
      open=0
      close=0
      start=0
      result=""
      for i,char in enumerate(s):
        if char =='(':
          open+=1
        if char == ')':
          close+=1
        if open == close:
          result+=s[start+1:i]
          start=i+1
      return result
          
s = "(()())(())"
sol= Solution()
print(sol.removeOuterParentheses(s))