#  Step 2


import random
word_list = ["anjesh","sarang","kalpana"]
chosen_word = random.choice(word_list)

print(f'the solution is {chosen_word}')

display = []
for i in range(0,len(chosen_word)):
    display.append("_")

guess = input("Guess a letter : ").lower()

for i in range(0,len(chosen_word)):
    if chosen_word[i] == guess :
        display[i] = guess

print(display)