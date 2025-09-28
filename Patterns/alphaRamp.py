def alphaRamp(n: int) -> None:
  letter='A'
  for i in range (1,n+1):
    for j in range (i):
      print(letter,end=" ")
    letter=chr(ord(letter)+1)
    print()

alphaRamp(3)
