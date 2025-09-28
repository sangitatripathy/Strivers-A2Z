# class Myclass:
#   x=5


# p1=Myclass()
# print(p1.x)  

#Write a class Person with attributes name and age. Add a method introduce() that prints "Hi, my name is {name} and I am {age} years old."

# class Person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age

#   def introduce(self):
#     print(f"Hi, my name is {self.name} and I am {self.age} years old.")  

# p1=Person("Sangita",20)
# p1.introduce()    

#create a class Book with attributes title and author. Implement a method get_info() that returns the book details
# class Book:
#   def __init__(self,title,author):
#     self.title=title
#     self.author=author
#   def get_info(self):
#     return {"title":self.title,"author":self.author}

# b1=Book("The Alchemist","Paulo Coelho")
# book_info=b1.get_info()
# title,author=book_info.values()
# print(f"title : {title}")
# print(f"Author :{author}")

# # Modify the Car class so that it initializes brand, model, and year using a constructor.
# class Car:
#   def __init__(self,brand,model,year):
#     self.brand=brand
#     self.model=model
#     self.year=year
#   def __str__(self):
#     return f"brand :{self.brand}\nmodel :{self.model}\nyear :{self.year}"

# car1=Car("Volkswagen","Volkswagen Jetta",1979)      
# print(car1)

# Create a class Student with attributes name, roll_number, and marks initialized using __init__.
# Modify the Student class to include a class variable school_name which is common for all students.
# class Student:
#   school_name="Jawahar Navodaya Vidyalaya"
#   def __init__(self,name,roll_number,marks):
#     self.name=name
#     self.roll_number=roll_number
#     self.marks=marks
#   def __str__(self):
#     return f"{self.name} of school {self.school_name} holding roll number {self.roll_number} scored {self.marks}"

# s1=Student("Sangita Tripathy",20,89)
# s1.school_name="Oneness International School"
# print(s1)

# Create a class Account with a method deposit(amount) that adds the given amount to the balance.
# class Account:
#   def __init__(self,bal):
#     self.bal=bal
#   def deposit(self,amount):
#     self.bal+=amount
#     return f"your current account balance is {self.bal}" 
# a1=Account(5000)
# print(a1.deposit(1300))
   
    
  
    