class Queue:
  def __init__(self):
    self.queue=[]
    
  def enqueue(self,element):
    self.queue.append(element)
    print("after enqueing"+ self.__str__())
    
  def dequeue(self):
    if self.isEmpty():
      return "Queue is Empty"
    popped_el=self.queue.pop(0)
    print("after dequeing"+self.__str__())
    return popped_el
  
  def peek(self):
    if self.isEmpty():
      return "Queue is Empty"
    return self.queue[0]
  
  def isEmpty(self):
    return len(self.queue) == 0
  
  def __str__(self):
    return "Queue"+str(self.queue)  

myqueue=Queue()

while(1):
  print("\nenter your choice :")
  print("1.ENQUEUE :")
  print("2.DEQUEUE :")
  print("3.PEEK :")
  print("4.Quit")
  choice=int(input("enter your choice :"))
  if choice == 1:
    num=int(input("Enter an element you want to push :"))
    myqueue.enqueue(num)
  elif choice == 2:
    print(myqueue.dequeue())
  elif choice == 3:
    print(myqueue.peek())
  elif choice == 4:
    print("Exiting Program")
    break
  else:
    print("Enter a valid choice")  