def alphaHill(n: int):
    for i in range (1,n+1):
      letter='A'
      for j in range (n-i):
        print(" ",end="")
      breakpoint=(2*i-1)//2
      for k in range (2*i-1):
        print(letter,end="")
        if (k >= breakpoint): letter=chr(ord(letter)-1)
        else: letter=chr(ord(letter)+1)
      print()

alphaHill(4)
      
