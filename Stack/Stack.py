class Stack:
  def __init__(self):
    self.stack=[]
  def isEmpty(self):
    return len(self.stack) == 0
  def push(self,element):
    self.stack.append(element)
    print("After push: ",self.__str__())
  def pop(self):
    if self.isEmpty():
      return "stack is empty"
    popped_el=self.stack.pop()
    print("After pop: ",self.__str__())
    return f"Popped element is {popped_el}"
  def peek(self):
    if self.isEmpty():
      return "stack is empty"
    return self.stack[-1]
  def size(self):
    return len(self.stack)
  def __str__(self):
    return "Stack: "+str(self.stack)

mystack= Stack()

while(1):
  print("\nenter your choice :")
  print("1.PUSH :")
  print("2.POP :")
  print("3.PEEK :")
  print("4.Quit")
  choice=int(input("enter your choice :"))
  if choice == 1:
    num=int(input("Enter an element you want to push :"))
    mystack.push(num)
  elif choice == 2:
    print(mystack.pop())
  elif choice == 3:
    print(mystack.peek())
  elif choice == 4:
    print("Exiting Program")
    break
  else:
    print("Enter a valid choice")
  
    