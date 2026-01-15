class Solution:
    def infixtoPostfix(self, s):
      ans=""
      stack=[]
      for char in s:
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z') or ('0' <= char <= '9'):
          ans+=char
        elif char == "*" or char == "/":
          while stack and stack[-1] in "*/^":
            ans+=stack.pop()
          stack.append(char)
        elif char == "+" or char=="-":
          while stack and stack[-1] in "*/^+-":
            ans+=stack.pop()
          stack.append(char)
        elif char == "(":
          stack.append(char)
        elif char == ")":
          while stack and stack[-1] != "(":
            ans+=stack.pop()
          stack.pop()
      while stack:
        ans+=stack.pop()
      return ans 
sol=Solution()
str="a+b*(c^d-e)^(f+g*h)-i"
print(sol.infixtoPostfix(str))