def symmetricButterfly(n:int):
  for i in range (1,n+1):
    for j in range (i):
      print("*",end="")
    for k in range (2*n-2*i):
      print(" ",end="")
    for l in range (i):
      print("*",end="")
    print()
  for i in range (n,0,-1):
    for j in range (i):
      print("*",end="")
    for k in range (2*n-2*i):
      print(" ",end="")
    for l in range (i):
      print("*",end="")
    print()

symmetricButterfly(5)