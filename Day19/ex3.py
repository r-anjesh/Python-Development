from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500, height= 400)
user_bet = screen.textinput(title= "Make your Bet", prompt= "Which turtle will win the race? Enter a color : ")

colors = ['red','orange', 'yellow', 'green', 'blue', 'purple']

# tim.color(colors[1])
# tim.penup()
# tim.goto(-240,-100)

red = Turtle(shape='turtle')
orange = Turtle(shape='turtle')
yellow = Turtle(shape='turtle')
green = Turtle(shape='turtle')
blue = Turtle(shape='turtle')
purple = Turtle(shape='turtle')


def set_color_position(object):
    
    object.penup()
    global color_index
    global turtle_position
    object.color(colors[color_index])
    object.goto(-240,turtle_position)
    all_tirtle.append(object)
    color_index += 1
    turtle_position += 50


all_tirtle = []
color_index = 0
turtle_position = -120
set_color_position(red)
set_color_position(orange)
set_color_position(yellow)
set_color_position(green)
set_color_position(blue)
set_color_position(purple)

is_race_on = False

if user_bet:
    is_race_on  = True
    while is_race_on:
        for turtle in all_tirtle:
            if turtle.xcor() > 215:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won, {winning_color} is the winner...")
                else:
                    print(f"YOu've lost, {winning_color} is the winner...")
            else:
                random_distance = random.randint(0,10)
                turtle.forward(random_distance)
screen.exitonclick()