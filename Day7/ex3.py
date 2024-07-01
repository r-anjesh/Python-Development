#  Step 3


import random
word_list = ["anjesh","sarang","kalpana"]
chosen_word = random.choice(word_list)

print(f'the solution is {chosen_word}')

display = []
for i in range(0,len(chosen_word)):
    display.append("_")

end_of_game = False
while not end_of_game:
  guess = input("Guess a letter : ").lower()

  for i in range(0,len(chosen_word)):
      if chosen_word[i] == guess :
          display[i] = guess

  print(display)

  if "_" not in display:
      end_of_game = True
      print("you won")