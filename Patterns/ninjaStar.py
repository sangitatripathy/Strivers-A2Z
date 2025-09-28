def ninjaStar(n:int):
  for i in range(1,n+1):
    if (i==1 or i==n):
      for j in range (n):
        print("*",end="")
    else:
      print("*",end="")
      for j in range (n-2):
        print(" ",end="")
      print("*",end="")
    print()


ninjaStar(5)