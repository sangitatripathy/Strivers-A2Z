class DecBin:
  def __init__(self,num):
    self.num=num

  def decimalToBinary(self,num,arr):
    if num == 0:
      return 
    self.decimalToBinary(num//2,arr)
    arr.append(num%2)

  def binToDecimal(self,num,p=0):
    if num <= 0:
      return 0
    return (num%10)*pow(2,p)+self.binToDecimal(num//10,p+1) 
    
    

number=DecBin(13)
arr=[]
number.decimalToBinary(number.num,arr)
print(''.join(map(str,arr)))
print(number.binToDecimal(1101))
    
    
    