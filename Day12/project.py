from art import logo
import random
hard =5
easy = 10
print(logo)
print('Welcome to the number gussing game !')
print("I'm thinking of a number between 1 - 100")
dificulty = input("Choose dificulty Type 'easy' or 'hard' : ")
if dificulty == 'hard':
    attempt = hard
elif dificulty == 'easy':
    attempt = easy
else:
    print("invalid input")


computer_guess = random.randint(1,101)

while attempt != 0:
    print(f'You have {attempt} remaining to guess the number')
    print(computer_guess)
    user_guess = int(input(f'Make a guess : '))
    if user_guess == computer_guess:
        print("You have guessed it right, you win !")
        break
    elif user_guess > computer_guess:
        print("too high")
        attempt -= 1
        if attempt != 0:
            print("guess again")
    else:
        print("too low")
        attempt -= 1
        if attempt != 0:
            print("guess again")
    
if attempt == 0:
    print("You've run out of guesses, you lose")
    