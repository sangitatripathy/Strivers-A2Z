class Stack:
  def __init__(self):
    self.stack=[]
    
  def isEmpty(self):
    return len(self.stack) == 0

  def push(self,element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return
    return self.stack.pop()

def valid(str):
  mystack=Stack()
  
  for s in str:
    if s== '(' or s=='[' or s=='{':
      mystack.push(s)
    elif s==')': 
      if mystack.isEmpty() or mystack.pop() != '(':
        return False
    elif s==']': 
      if mystack.isEmpty() or mystack.pop() != '[':
        return False
    elif s=='}': 
      if mystack.isEmpty() or mystack.pop() != '{':
        return False  
    return mystack.isEmpty()  
    
str=input("enter a string")
print(valid(str))  
 