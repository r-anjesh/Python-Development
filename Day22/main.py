from turtle import Turtle,Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Score

# Screen Setup
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title("PONG")
screen.tracer(0)


# Object ofall the imported Class
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()


# Screen Control
screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

# CopyRight Claim
ownership = Turtle()
ownership.color('pink')
ownership.hideturtle()
ownership.penup()
ownership.goto(240,-280)
ownership.write("MADE BY ANJESH", font=("italian", 10, "normal") )

game_is_on = True
while game_is_on:
    
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()  

    #  Detect Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #  detect collison with paddle 
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < 320:
        ball.bounce_x()

    # Missed Ball
    if ball.xcor() > 350:
        score.l_point()
        ball.reset_position()

    if ball.xcor() < -350:
        score.r_point()
        ball.reset_position()

screen.exitonclick()
