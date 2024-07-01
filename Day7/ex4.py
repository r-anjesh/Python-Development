#  Step 4
import random
from angra import angry
from logos import logo
print(logo)
print(angry)
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["anjesh","sarang","kalpana"]
chosen_word = random.choice(word_list)

print(f'the solution is {chosen_word}')

display = []
for i in range(0,len(chosen_word)):
    display.append("_")

current_stage = stages[5]
end_of_game = False
life = 6
while not end_of_game or life == 0:
    guess = input("Guess a letter : ").lower()

    if guess in display:
        print(f'You have already guessed {guess}')

    for i in range(0,len(chosen_word)):
        if chosen_word[i] == guess :
            display[i] = guess
    
    str = ''
    for i in display:
        
        str += i + ' '

    print(str)

    if guess not in chosen_word:
        life = life - 1
        current_stage = stages[life - 1]
        print(f"You have guessed {guess}, that's not in the word , You lose a life")
    
    print(current_stage)
    if current_stage == stages[0]:
        print('You lost')
        end_of_game = True

    if "_" not in display:
        end_of_game = True
        print("you won")