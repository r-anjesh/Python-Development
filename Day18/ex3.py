from turtle import Turtle, Screen
from random import choice
kachhua = Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
kachhua.shape("classic")
def draw_shape(number_edge):
    angle = 360/number_edge
    for _ in range(number_edge):
        kachhua.forward(100)
        kachhua.right(angle)


for x in range(3,11):
    kachhua.color(choice(colours))
    draw_shape(x)

screen = Screen()
screen.exitonclick(9999999999999999968666666666666666666666666666666666666666666666666688888886666688888)