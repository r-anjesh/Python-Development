import turtle as t
import random

user_turtle = input("select your turtle (balck or blue)")

anjesh = t.Turtle()
ajju = t.Turtle()

ajju.color('blue')
ajju.shape('turtle')
anjesh.color('black')
anjesh.shape('turtle')
anjesh.speed('fastest')
ajju.speed('fastest')
anjesh.penup()
ajju.penup()
anjesh.setheading(90)
anjesh.forward(100)
anjesh.setheading(0)
anjesh.back(370)
ajju.back(370)

space = 5
distance_anjesh = 0
distance_ajju = 0
a = 0
b = 0

while a < 727 and b < 727:
    distance_anjesh = random.randint(0,space)
    distance_ajju = random.randint(0,space)

    anjesh.forward(distance_anjesh)
    ajju.forward(distance_ajju)

    a += distance_anjesh
    b += distance_ajju

if a>b and user_turtle == 'black':
    print(f"Yes, You won !  Black turle is the winner")
elif a>b and user_turtle == 'blue':
    print(f" you lose, Black turle is the winner")
elif b>a and user_turtle == 'blue':
    print(f"Yes, You won !  Black turle is the winner")

else :
    print(f" you lose, Black turle is the winner")




screen = t.Screen()
screen.exitonclick()



