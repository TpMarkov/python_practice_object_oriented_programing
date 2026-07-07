import turtle

import pandas

# Screen Setup
screen = turtle.Screen()
screen.setup(width=720, height=500)
shape = "blank_states_img.gif"
screen.addshape(shape)
turtle.shape(shape)

# Import game data from the csv
data = pandas.read_csv("50_states.csv")
# Get all the states names from the CSV file
states_names = data.state.tolist()

# Game settings
game_is_on = True
correct_answers = 0
correct_states = []

# Ask user input
while game_is_on or correct_answers < 50:

    user_answer = screen.textinput(
        title=f"{correct_answers} / 50 States",
        prompt="Please type in your guess"
    ).title()

    if user_answer == "Exit":
        missing_states = []

        for state in states_names:
            if state not in correct_states:
                missing_states.append(state)

        missing_states = {
            "Missing States": missing_states
        }
        missing_states = pandas.DataFrame(missing_states)
        missing_states.to_csv("./missing_states/missing_states.csv")
        break

    if correct_answers == 50:
        print("Great! Game Over! You win!")
        game_is_on = False

    if user_answer in states_names:
        print("Correct!")
        if user_answer in correct_states:
            print("Already entered!")
        else:
            correct_answers += 1
            correct_states.append(user_answer)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == user_answer]

            t.goto(state_data.x.item(), state_data.y.item())
            t.color("blue")
            t.write(user_answer, font=("Arial", 10, "bold"))
    else:
        print("Wrong!")

screen.mainloop()
