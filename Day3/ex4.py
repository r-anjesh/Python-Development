print("Welcome to python pizza Deliveries")
size = input("Whta size pizza do you want ")
add_pepperoni = input("Do you want extra pepperoni? ")
extra_cheese = input("Do you want extra cheese? ")

s = 15
m = 20
l = 25
pepperoni_small = 0
pepperoni_mediumLarge =0
cheese = 0
if (add_pepperoni == 'Y'):
    if (size == 'S'):
        pepperoni_small = 2
    else:
        pepperoni_mediumLarge = 3


if (extra_cheese == 'Y'):
    extra_cheese = 1

if (size == 'S'):
    print(f'Your final bill is: ${s+pepperoni_small+pepperoni_mediumLarge+cheese}')
elif (size == 'M'):
    print(f'Your final bill is: ${m+pepperoni_small+pepperoni_mediumLarge+cheese}')
elif (size == 'L'):
    print(f'Your final bill is: ${l+pepperoni_small+pepperoni_mediumLarge+cheese}')
else:
    print("enter right choice:")
    