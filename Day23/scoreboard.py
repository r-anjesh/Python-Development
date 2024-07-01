from turtle import Turtle
FONT = ("Courier", 24, "normal")
STARTING_LEVEL = 0

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = STARTING_LEVEL
        self.color("black")
        self.hideturtle()
        self.penup()
                
        self.goto(-250,250)
        self.write(f"level : {self.level}",font=FONT)


    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"level : {self.level}",font=FONT)
