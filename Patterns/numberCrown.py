def numberCrown(n:int) -> None:
  for i in range (1,n+1):
    temp=1
    for j in range (i):
      print(temp,end=" ")
      temp+=1
    for l in range ((n-i)*2):
      print(" ",end=" ")
    for k in range (i,0,-1):
      print(k,end=" ")
    print()

numberCrown(3)
    