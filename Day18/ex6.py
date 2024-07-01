import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    rgb = (r,g,b)
    return rgb

def draw_graph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.speed("fastest")
        tim.color(random_color())
        tim.circle(150)
        tim.setheading(tim.heading() + gap_size)

draw_graph(5)

screen = t.Screen()
screen.exitonclick()
