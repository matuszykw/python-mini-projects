import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "name-the-states/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

data = pandas.read_csv("name-the-states/50_states.csv")
states = data['state'].to_list()
x_cor = data['x'].to_list()
y_cor = data['y'].to_list()

correct = 0
guessed_states = []
while correct < 50:
    answer_state = screen.textinput(f"{correct}/50 States Correct", "Whats another state's name?").title()
    if answer_state in states and answer_state not in guessed_states:
        index = states.index(answer_state)
        state_x = x_cor[index]
        state_y = y_cor[index]
        pen.goto(state_x, state_y)
        pen.write(states[index])
        correct += 1
        guessed_states.append(answer_state)
    elif answer_state == 'Exit':
        not_guessed = [state for state in states if state not in guessed_states]
        to_learn = {
            "state": not_guessed
        }
        pandas.DataFrame(to_learn).to_csv("name-the-states/states_to_learn.csv")