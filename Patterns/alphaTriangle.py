def alphaTriangle(n:int) ->None:
  for i in range (1,n+1):
    for j in range (i,0,-1):
      print(chr(65+n-j),end=" ")
    print()

alphaTriangle(3)