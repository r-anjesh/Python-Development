# Step 1

import random
word_list = ["anjesh",'sarang',"kalapna"]
choosen_word = random.choice(word_list)
guess = input("Guess a letter : ").lower()
for i in range(0,len(choosen_word)):
    if choosen_word[i] == guess:
        print("Right")
    else:
        print("Wrong")