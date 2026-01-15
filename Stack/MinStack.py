class MinStack:
  def __init__(self):
    self.stack=[]
    self.minstack=[]
  def push(self,val):
    self.stack.append(val)
    if not self.minstack or val < self.minstack[-1]:
      self.minstack.append(val)
  def pop(self):
    if len(self.stack) == 0:
      return None
    x=self.stack.pop()
    if self.minstack and x == self.minstack[-1]:
      self.minstack.pop() 
  def top(self):
    if len(self.stack) == 0:
      return None
    self.stack[-1]
    
  def getMin(self):
    if len(self.stack) == 0:
      return None
    self.minstack[-1]