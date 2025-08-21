def reversedBits(x):
  rev=0
  for i in range (32):
      bit = x & 1
      rev= (rev << 1)| bit
      x=x>>1
      print(bit,end="")
  return rev

print("\n",reversedBits(5))