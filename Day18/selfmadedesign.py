import turtle as t
import random

color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
t.colormode(255)
kachhua = t.Turtle()
kachhua.speed('fastest')
kachhua.shape('turtle')
kachhua.penup()
kachhua.setheading(215)
kachhua.forward(350)
kachhua.setheading(0)
back_space = 500
no_of_dot = 11

for _ in range(6):
    for _ in range(no_of_dot):
        kachhua.dot(30,random.choice(color_list))
        kachhua.forward(50)
        
    no_of_dot -= 2
    kachhua.setheading(90)
    kachhua.forward(50)
    kachhua.setheading(180)
    kachhua.forward(back_space)
    kachhua.setheading(0)
    back_space -= 100

dot_increment = 3
reverse = 100
kachhua.setheading(180)
kachhua.forward(reverse)
kachhua.setheading(0)
while no_of_dot < 12:
    for _ in range(dot_increment):
        kachhua.dot(30,random.choice(color_list))
        kachhua.forward(50)

    dot_increment += 2
    reverse += 100
    kachhua.setheading(90)
    kachhua.forward(50)
    kachhua.setheading(180)
    kachhua.forward(reverse)
    kachhua.setheading(0)




screen = t.Screen()
screen.exitonclick()
