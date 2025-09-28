# from math import *
# from collections import *
# from sys import *
# from os import *

# def nthfibonaccinum(n):
#   a=0
#   b=1
#   for i in range (1,n):
#       if n==1:
#           return 0
#       elif n==2:
#           return [0,1]
#       else:
#           a,b=b,a+b
#   return a

# res=nthfibonaccinum(int(input("enter which fibonacci number you want to see"))) 
# print(res)    

# from typing import List
# class Solution:
#     def lcmAndGcd(self, a : int, b : int) -> List[int]:
#         def gcd(a,b):
#             num = a if a > b else b
#             for i in range(1,num):
#                 if a%i==0 and b%i ==0:
#                     g=i
#             return g
#         def lcm(a,b):
#             l=(a*b)//gcd(a,b)
#             return l
#         gcd_value=gcd(a,b)
#         lcm_value=lcm(a,b)
#         return [gcd_value,lcm_value]
        
# sol=Solution()
# result=sol.lcmAndGcd(5,2)
# print(result)     

def fibonacci(n):
  a=0
  b=1
  for i in range(1,n):
    print(a)
    next=a+b
    a=b
    b=next
  

            

  