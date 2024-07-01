import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Object of all Class
player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up,"space")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect Car collision with Turtle
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_over = Turtle()
            game_over.goto(-100,0)
            game_over.write("GAME OVER",font=("Courier", 30, "normal"))
            game_is_on = False

    # Detect Collision with wall
    if player.ycor() > 280:
        player.go_to_start()
        car_manager.speedup_car()
        score.level_up()


screen.exitonclick()

    
