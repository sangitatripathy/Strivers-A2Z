import random

options= ("rock","paper","scissor")
computer=random.choice(options)
playing =True
score=0
while playing:
  player= ""
  while player not in options:
    player=input("Enter a choice between (rock,paper,scissor) ")
  print(f"player : {player}")
  print(f"computer : {computer}")

  if player == computer:
    print("it's a tie")
  elif player == "rock "and computer == "scissor":
    print("you win")
    score += 1
  elif player =="paper" and computer == "rock":
    print("you win")
    score += 1
  elif player =="scissor" and computer == "paper":
    print("you win")
    score += 1
  else:
    print("you lose !")
  print(f"your score is {score}")  
  if not input("(play again (Y/N?)").lower() == "y":
    playing=False