menu={"pizza":250,
      "popcorn":500,
      "soda":50,
      "chocolate":25,
      "peanuts":20}

print("------------MENU------------")
for key,value in menu.items():
  print(f"{key:10} :₹{value :.2f}")
print("----------------------------")

cart=[]
total=0

while True:
  food=input("enter an item (q to quit)").lower()
  if food== "q":
    break
  elif menu.get(food) is not None:
    cart.append(food) 

for food in cart:
  total += menu.get(food)
  print(food,end=" ")

print(f"\ntotal is : ₹{total:.2f}")
