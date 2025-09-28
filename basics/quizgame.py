questions=("How many elemnts are there in periodic table",
      "Which animal lays largest egg",
      "What is the most abundant gas in the Earth's atmosphere",
      "how many bones are there in the human body",
      "Which planet in the solar system is the hottest")

options=(("A.116","B.117" ,"C.118 ","D.119" ),
         ("A.Whale","B.Crocodile" ,"C.Elephant ","D.Ostrich"),
         ("A.Nitrogen","B.Oxygen" ,"C.Carbon-dioxide ","D.Hydrogen"),
         ("A.206","B.207" ,"C.208 ","D.209"),
         ("A.Mercury","B.Venus" ,"C.Earth ","D.Mars"))

answers=("C","D","A","A","B")
guesses=[]
score=0
question_num = 0

for question in questions :
  print("---------------------------------------")
  print(question) 
  for option in options[question_num]:
    print(option)
  guess=input("Enter (A,B,C,D) : ").upper()
  guesses.append(guess)  
  if guess == answers[question_num]:
    score+=1
    print("Correct")
  else:
    print(f"Wrong !! the right answer is {answers[question_num]} ")
  question_num += 1

