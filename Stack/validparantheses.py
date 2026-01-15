def valid(str):
  stack = []
  for ch in str:
    if ch == '(' or ch == "{" or ch == "[":
      stack.append(ch) 
    elif ch == ')':
      if stack.pop() != "(":
        return False 
    elif ch == '}':
      if stack.pop() != "{":
        return False 
    else:
      if stack.pop() != '[':
        return False
  return True
str=input("enter a string :")
print(valid(str))  
 