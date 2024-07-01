import turtle
import pandas
import csv

tim = turtle.Turtle()
tim.penup()
tim.hideturtle()
tim.color("black")


screen = turtle.Screen()
screen.screensize(canvheight=600,canvwidth=600)
screen.title("U.S. States Game")
image = "./Day25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


df = pandas.read_csv("./Day25/us-states-game-start/50_states.csv")
state_list = df.state.to_list()
x_list = df.x.to_list()
y_list = df.y.to_list()

guessed_state = []
missed_state = []
correct_answer = 0
while len(guessed_state) < 50:

    answer_state = screen.textinput(title=f"{correct_answer}/50",prompt="What's another state's name? ").title()
    if answer_state == 'Exit':    
        break
    if answer_state in state_list:
        correct_answer += 1
        index = state_list.index(answer_state)
        tim.goto(x_list[index], x_list[index])
        tim.write(f"{answer_state}")
        guessed_state.append(answer_state)

# for state in state_list:
#     if state not in guessed_state:
#         missed_state.append(state)
missed_state ==[st for st in state_list if st  not in guessed_state]
    
missed_state_dict = {
    "state" : missed_state
}

missed_state_df = pandas.DataFrame(missed_state_dict)
missed_state_csv = missed_state_df.to_csv("./Day25/us-states-game-start/missed_states.csv")