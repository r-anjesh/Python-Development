name1 = input("What is your name : ")
name1 = name1.upper()
name2 = input("What is your lover name : ")
name2 = name2.upper()
score1 = 0
score2 = 0
score1 += name1.count('T')
score1 += name2.count('T')
score1 += name1.count('R')
score1 += name2.count('R')
score1 += name1.count('U')
score1 += name2.count('U')
score1 += name1.count('E')
score1 += name2.count('E')
score2 += name1.count('L')
score2 += name2.count('L')
score2 += name1.count('O')
score2 += name2.count('O')
score2 += name1.count('V')
score2 += name2.count('V')
score2 += name1.count('E')
score2 += name2.count('E')

score = str(score1) + str(score2)
score = int(score)

if score < 10  and score > 90:
    print(f'Your score is {score}, you go together like coke and mentos')

elif score > 40 and score < 50:
    print(f'Your score is {score}, you are alright together.')

else:
    print(f'your score is {score}')
