def halfDiamondStar(n :int) -> None:
  for i in range (1,n*2):
    stars=i
    if(i > n):
      stars=2*n-i
    for j in range (stars):
      print("*",end="")
    print()

halfDiamondStar(4)
    