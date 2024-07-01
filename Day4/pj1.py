import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
games = [rock,paper,scissors]
user = int(input("What do you want to choose? Tyoe 0 for rock, 1 for paper, 2 for scissors."))
if int(user) > 2:
    print("invalid number")

else:
    print(games[int(user)])
    computer = random.randint(0,2)

    print(f'Computer choose \n{games[computer]}')

    if user == 0 and computer ==2:
        print("You win!")
    elif computer == 0 and user ==2:
        print("You lose!")
    elif computer > user:
        print("You lose!")
    elif user > computer:
        print("You win!")
    elif computer == user:
        print("It's a draw")

