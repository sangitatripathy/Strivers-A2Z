def symmetricVoid(n :int):
  for i in range (n):
    for j in range (n-i):
      print("* ",end="")
    for j in range (2*i):
      print("  ",end="")
    for j in range (n-i):
      print("* ",end="")
    print()
  for i in range (n):
    for j in range (i+1):
      print("* ",end="")
    for j in range (2*(n-i-1)):
      print("  ",end="")
    for j in range (i+1):
      print("* ",end="")
    print()
# def hollow_symmetric_void(n: int):
#     # Top half
#     for i in range(n):
#         print("* " * (n - i), end="")  # left stars
#         print("  " * (2 * i), end="")  # middle spaces
#         print("* " * (n - i))           # right stars

#     # Bottom half
#     for i in range(n):
#         print("* " * (i + 1), end="")  # left stars
#         print("  " * (2 * (n - i - 1)), end="")  # middle spaces
#         print("* " * (i + 1))           # right stars


symmetricVoid(5)

