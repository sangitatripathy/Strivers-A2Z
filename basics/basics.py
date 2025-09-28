
#strings
# print("hello world")
# first_name= "ninu"
# last_name="tripathy"
# print(first_name+" "+last_name)
# print(f"i love {first_name}")
# age=20
# print(f"you are {age} years old")

# input() =prompts the user to enter data and returns data as a string
# name =input("what is your name")
# print(f"my name is {name}")
# age=input("enter your age")
# age =int(age)
# age=age+1
# print(f"my age is {age}")

#Rectangle area
# length=int(input("enter length"))
# width=int(input("enter width"))
# area=length*width
# print(f"area is {area} cm")

# age=int(input("enter your age: "))
# if age >= 18 :
#   print("you can drive")
# elif age <= 0:
#     print("invalid age")
# else:
#     print("you must be 18+")

# response= input("would you like nay food (Y/N) ")
# if response=="Y":
#   print("have some food")
# else:
#   print("no food for you")

#calculator
# a=int(input("enter 1st number"))
# b=int(input("enter 2nd number"))
# op=input("enter the operation you want to perform")
# if op== "+":
#   print(a+b)
# elif op=="-":
#   print(a-b)
# elif op=="/":
#   print(a/b)
# elif op=="%":
#   print(a%b)
# elif op=="*":
#   result=a*b
#   print(round(result,1))
# else:
#   print(f"{op}is not valid")
  
# temp=int(input("enter the temp"))
# is_raining=True

# if temp>35 or temp < 0 or is_raining:
#   print("stay at home")
# else:
#   print("go out")

# temp=int(input("enter temp"))
# is_sunny=False
# if temp > 30 and is_sunny:
#   print("it is hot outside 🥵")
# elif temp > 30 and not is_sunny:
#   print("it is cloudy ☁️")
# else:
#   print("good weather 😊")

# num=5
# print("positive" if num > 0 else "negative")

# num=int(input("enter a number"))
# result="EVEN" if num%2 == 0 else "ODD"
# print(f"entered number is {result}")

#strings
# name=input("enter your fullname:")
#result=len(name)
# result=name.find("t")# returns first occurence searched character
# result=name.rfind("a")# returns last occurence of searched character
# result=name.capitalize()# only capitalizes first letter of a string
# result=name.upper()
# result=name.lower()
# result=name.isdigit()# returns false
# result=name.isalpha()#It checks whether a given character or all characters within a string are alphabetic
#phonenumber=input("enter your phone number")
# result=phonenumber.count("9")# counts the characters in string
# result=name.replace("a","o")
# print(result)

# username=input("enter username: ")
# if len(username) > 12:
#   print("can't be more than 12 characters")
# elif (username.find(" ") != -1):
#   print("can't contain spaces")
# elif (username.isalpha() == False):
#   print("can't contain digits")
# else:
#   print(username)

#indexing operator [start : end : step]
# credit_card="1234-5678-9012-5617"
# print(credit_card[0])
# print(credit_card[0:])
# print(credit_card[5:9])#[5:9] first one is exclusive and second one is inclusive (9-1)
# print(credit_card[:4])
# print(credit_card[-1])#prints the last character of string
# print(credit_card[::-2])
# print(credit_card[::2])
# last_digits=credit_card[-4:]
# print(last_digits)
# print(f"XXXX-XXXX-XXXX-{last_digits}")
# credit_card=credit_card[::-1]#reverse the string
# print(credit_card)

#format-specifiers
# price1=300000.14519
# price2=-570000.68
# price3 = 34000
# print(f"price 1 is {price1:.2f}")#prints value upto 2 floating point numbers
# print(f"price 2 is {price2:.2f}")
# print(f"price 3 is {price3:.2f}")
# print(f"price 1 is {price1:10}")#adjust number with padding between 10 spaces
# print(f"price 2 is {price2:10}")
# print(f"price 3 is {price3:10}")
# print(f"price 1 is {price1:010}")#adjust number with padding between 10 spaces with inserting 0
# print(f"price 2 is {price2:010}")
# print(f"price 3 is {price3:010}")
# print(f"price 1 is {price1:<10}")#left justified
# print(f"price 2 is {price2:<10}")
# print(f"price 3 is {price3:<10}")
# print(f"price 1 is {price1:>10}")#right justified
# print(f"price 2 is {price2:>10}")
# print(f"price 3 is {price3:>10}")
# print(f"price 1 is {price1:^20}")#central line
# print(f"price 2 is {price2:^20}")
# print(f"price 3 is {price3:^20}")
# print(f"price 1 is {price1:+}")#display the positive values with plus sign
# print(f"price 2 is {price2:+}")
# print(f"price 3 is {price3:+}")
# print(f"price 1 is {price1:,}")#1000 separator
# print(f"price 2 is {price2:,}")
# print(f"price 3 is {price3:,}")
# print(f"price 1 is {price1:+,.2f}")# we can combine format sppecifiers
# print(f"price 2 is {price2:+,.2f}")
# print(f"price 3 is {price3:+,.2f}")

#while loop
# name=input("enter your name: ")
# while name=="":
#   print("you didn't enter your name")
#   name=input("enter your name: ")
# print(f"hello {name}")  

# food=input("enter food you like (q to quit) : ")
# while not food == "q":
#   print(f" you like {food}")
#   food=input("enter food you like (q to quit) : ")
# print("bye")
  
#compound interest
# principal=0
# rate=0
# time=0

# while principal<=0:
#   principal=float(input("enter your principal amount : "))
#   if principal <= 0:
#     print("principal can't be negative or 0")

# while rate<=0:
#   rate=float(input("enter your rate amount : "))
#   if rate <= 0:
#     print("rate can't be negative or 0")

# while time <= 0:
#   time=int(input("enter time : "))
#   if time <= 0:
#     print("time can't be negative or 0")
    
# print(principal)
# print(rate)
# print(time)   
# total=principal * pow((1+rate/100),time )
# print(f"compound interest is {total}")

# import time

# my_time=int(input("enter time in second"))
# for x in range(my_time,0,-1):
#   print(x)
#   time.sleep
# print("Happy Birthday")

# for x in range(1,11):
#   print(x,end=" ")

# for x in range(3):
#   for y in range(1,10):
#     print(y,end=" ")
#   print()


# list=[] ordered and changeable duplicates ok
# fruits=["kiwi","grapes","coconut","apple","banana"]
# fruits[0]="pomelo"
# for fruit in fruits:
#   print(fruit,end=" ")
# for x in fruits[::-1]:#prints in reverse order
#   print(x)
# fruits.append("litchi")
# fruits.remove("coconut")
# fruits.insert(0,"mango")
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("apple"))
# fruits.append("apple")
# print(fruits.count("apple"))
# print(fruits)

#set={} unordered and immutable ,but add/remove ok,no duplicates
# fruits={"kiwi","grapes","coconut","apple","banana"}
# fruits.add("pomelo")
# for x in fruits:
#   print(x)
# fruits.remove("kiwi")
# print(fruits)
# print(fruits.pop())
# fruits.add("coconut")    

# Tuples=() ordered,unchangeable,duplicates ok
# fruits=("kiwi","grapes","coconut","apple","banana","coconut")
# print(fruits.index("apple"))
# print(fruits.count("coconut"))
# for x in fruits:
#   print(x)

#shopping cart
# foods=[]
# prices=[]
# total=0
# while True:
#   food=input("enter the food you want : ")
#   if food.lower()=='q':
#     break
#   else:
#     price=float(input(f"enter the price of {food} : "))
#     foods.append(food)
#     prices.append(price)
    
# print("-----your cart value is -----")
# for food in foods:
#   print(food,end=" ")
# print() 
# for price in prices:
#   total+=price
# print(total) 
 
#user input in a list
# n=int(input("enter the number of elements you want"))
# my_list=[]
# for i in range(n):
#   num=int(input(f"enter the {i+1} element"))
#   my_list.append(num)
# print(my_list)

# matrix user input
# r=int(input("enter the number of rows"))
# c=int(input("enter the number of columns"))
# my_list=[]
# for i in range(r):
#   row=[]
#   for j in range(c):
#     num=int(input(f"enter a number for row {i+1} and column {j+1} :"))
#     row.append(num)
#   my_list.append(row)  
  
# for i in range (r):
#   for j in range(c):
#     print(my_list[i][j],end=" ")
#   print()  

# numpad=((1,2,3),
#         (4,5,6),
#         (7,8,9),
#         ("*",0,"#"))
# for nums in numpad:
#   for char in nums:
#     print(char,end=" ")
#   print()  

# dictionary:- ordered,changeable,exist in key: value pair 
capitals= {"USA" :"Washington D.C",
            "India" : "New Delhi",
            "Pakistan" : "Islamabad",
            "Germany": "Berlin",
            "South Korea" : "Seoul",
            "Sweden" : "Stockholm"}

# if capitals.get("USA"):
#   print("that capital exists")

# else :
#   print("that capital doesn't exists")

# capitals.update({"Japan" : "Tokyo"})
# capitals.pop("Pakistan")
# capitals.popitem()
# capitals.clear()

# key=capitals.keys()
# print(key)
for key in capitals.keys():
  print(key)

# value=capitals.values()
for  value in capitals.values():
  print(value)
# print(value)

# item=capitals.items()
# print(item)
# for x in capitals.items():
#   print(x)

# for key, value in capitals.items():
#   print(f"{key},{value}")

# import random

# low =1
# high =100
# number=random.randint(low,high)
# number =random.random()
# options=("puchka","pizza","pasta","burger","sandwich")
# choice=random.choice(options)
#print(choice)
# cards=["2","3","4","5","6","7","8","9","10","J","K","Q","A"]
# random.shuffle(cards)
# print(cards)

#------------------------------------------------------------------

# functions

# def net_price(list_price,discount=0,tax=0.05):
#   return list_price*(1-discount)*(1+tax)

# print(net_price(500))
# print(net_price(500,0.1,0.7))

# print("1","2","3","4","5",sep="-")

# def selection_sort(arr,n):
#   for i in range(0,n-1):
#     min= i
#     for j in range(i+1,n):
#       if arr[j] <arr[min] :
#         min=j
#     temp=arr[i]
#     arr[i]=arr[min]
#     arr[min]=temp

#------------------------------------------------------------------
# args and kwargs
# def add(*args):
#   total=0
#   for arg in args:
#     total+=arg
#   return total  
# print(add(1,2,3))

# def address(**kwargs):
#   for value in kwargs.values():
#     print(value)
#   for key in kwargs.keys():
#     print(key)
#   for key,value in kwargs.items():
#     print(f"{key}:{value}")     

# address(country="India",state="odisha",district="cuttack",zip="754008")

# membership-operator
# word="sangita"
# letter=input("guess a letter in the secret word :")
# if letter not in word:
#   print("not found") 
# else:
#    print(f"there's a {letter}")

# if letter in word:
#   print(f"there's a {letter}")
# else:
#   print("not found") 

# doubles=[]
# for x in range(1,11):
#   doubles.append(x*2)
# print(doubles)   

# doubles=[(x*2) for x in range(1,11)]
# print(doubles)

# numbers=[-1,2,-3,-4,5,6]
# positive_num=[num for num in numbers if num>0]
# negative_num=[num for num in numbers if num<0]
# print(positive_num)
# print(negative_num)

# def switch_example(day):
#   match day:
#     case 1:
#       return "Sunday"
#     case 2:
#       return "Monday"
#     case 3:
#       return "Tuesday"
#     case 4:
#       return "Wednesday"
#     case 5:
#       return "Thursday"
#     case 6:
#       return "Friday"
#     case 7:
#       return "Saturday"
#     case _:
#       return "invalid"

# print(switch_example(5))