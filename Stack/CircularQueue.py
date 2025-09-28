class CircularQueue:
  def __init__(self,k):
    self.size=k
    self.circularQ=[None]*k
    self.front=self.rear=-1
    
  def isEmpty(self):
      return len(self.circularQ)== 0

  def enqueue(self,element):
    if ((self.rear+1)% self.size == self.front):
      print("Queue Overflow")
      return
    elif self.front ==-1:
      self.front=self.rear=0
    else:
      self.rear=(self.rear+1)%self.size
    self.circularQ[self.rear]=element
    print("Queue after enqueueing :"+self.__str__())
    
  def dequeue(self):
    if self.front == -1:
      print("Queue is empty")
      
    removed=self.circularQ[self.front]
    if self.front == self.rear:
      self.front=-1
      self.rear= -1
    else : 
      self.front=(self.front+1)%self.size
    print("Queue after dequeueing :"+self.__str__())
    return removed  
  
  def peek(self):
    if self.isEmpty():
      return "Queue is Empty"
    return self.circularQ[self.rear]

  def __str__(self):
    return f"Circular Queue :" + str(self.circularQ)

size=int(input("enter the size of Circular queue"))
myqueue=CircularQueue(size)

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
          
      
    