import turtle as t
import random


kachhua  = t.Turtle()
t.colormode(255)
direction = [0,90,180,270]
kachhua.pensize(10)
kachhua.speed("fastest")


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

for i in range(200):
    kachhua.color(random_color())
    kachhua.forward(30)
    kachhua.right(random.choice(direction))

screen = t.Screen()
screen.exitonclick()