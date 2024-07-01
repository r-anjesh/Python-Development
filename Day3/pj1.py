print('''
                 =_-___
                    o    \__ \
                   o       __| \
                    o      \__  \
                      oooo    \  \
                               \  \
 __________________             |   \
|__________________|             \   |
 \/\/\/\/\/\/\/\/\/     _----_    |   |
  \/\/\/\/\/\/\/\/     |      \   |   |
   \/\/\/\/\/\/\/      |       |    |  |
    |/\/\/\/\/\|        |       \__/    |
    |/\/\/\/\/\|         __---          |
    |/\/\/\/\/\|       /   \            |
                      |     |          |
                      |   /            |
                      |   \            |
                      |   | \          |
                      |   |   \____-----\
                      |   |    \____-----
                       |  |    |          \
                       |  |   |             \
                        \  \_|_      |       |
                         \____/  ___/ \_____/\
                            /    /       \     \
                          /     /          \     \
                         /    /              \    \
                       /    /                  \    \
                      /   /                      \   \
                /\   /  /                          \  |
               |  \/ \/                              \/ \
                \    |                             __/   |
                  \_/                            /______/
''')
print("Welcome to Treasure Island.\nYour mission is to find the Treasure.")
cross = input('''You're at a cross road. Where do you want to go? Type "left" or "right"\n''').lower()
if cross == 'left':
    lake = input('''You came ot lake. There is an island in the middle of the lake. Type "wait" to wit for a boat or "swim" to swim accross\n''').lower()
    if lake == 'wait':
        door = input('''You arrived at the island unharmed, there is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? red, blue or yellow\n''').lower()
        if door == 'yellow':
            print("You Win !!")
        else:
            print("Game over")
    else:
        print("Game over")

else:
    print("Game over")