from turtle import Turtle
import random 

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    
    def __init__(self):
        self.all_cars = []
        self.create_cars()
        self.new_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        random_choice = random.randint(1,6)
        if random_choice == 1 :
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.new_speed)
        
    def speedup_car(self):
        self.new_speed += MOVE_INCREMENT
        for car in self.all_cars:
            car.backward(self.new_speed)