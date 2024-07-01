import turtle as t
import random

kachhua = t.Turtle()
t.colormode(255)
kachhua.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g= random.randint(0,255)
    b = random.randint(0,255)
    rgb = (r,g,b)
    return rgb

def make_circle():
    i = 0
    while i< 72:
        kachhua.forward(10)
        kachhua.left(5)
        i += 1


for _ in range(72):
    kachhua.color(random_color())
    make_circle()
    kachhua.left(5)