import turtle as t

def move_forward():
    tim.forward(20)

def move_back():
    tim.back(20)

def move_left():
    tim.left(15)

def move_right():
    tim.right(15)

def clear_screen():
    tim.screen.resetscreen()
    # tim.reset()
    # tim.home()  and many more option 




tim = t.Turtle()
screen = t.Screen()
screen.listen()

screen.onkey(fun = move_forward, key = "w")
screen.onkey(fun = move_back, key = "s")
screen.onkey(fun = move_left, key = "a")
screen.onkey(fun = move_right, key = "d")
screen.onkey(fun = clear_screen, key = "c")


screen.exitonclick()