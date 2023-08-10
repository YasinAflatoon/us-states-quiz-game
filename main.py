import time
from turtle import Screen, Turtle
import pandas
# import turtle

df = pandas.read_csv("50_states.csv")

states_list = df["state"].to_list()
x_positions = df["x"].tolist()
y_positions = df["y"].tolist()

data_dict = [{"state": states_list[i], "position":(x_positions[i], y_positions[i])} for i in range(0, 50)]

sc = Screen()
sc.title("US states quiz.")
sc.setup(width=1200, height=820)
sc.bgpic("usa-states-map-colors.gif")

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)

state_name = Turtle()
state_name.color("gray10")
state_name.hideturtle()
state_name.penup()

game_on = True
correct_guesses = 0
while game_on:
    user_guess = (sc.textinput(title=f"States guessed: {correct_guesses}/50", prompt="Type an state's name:")).title()
    if user_guess == "Exit":
        for state in data_dict:
            state_name.goto(state["position"])
            state_name.write(
                arg=f"{state['state']}",
                align="center",
                move=False,
                font=("Arial Black", 11, "normal")
            )
        time.sleep(5)
        not_guessed = [item["state"] for item in data_dict]
        new_data = pandas.DataFrame(not_guessed)
        new_data.to_csv("missed_states.csv")
        break
    for state in data_dict:
        if user_guess == state["state"]:
            state_name.goto(state["position"])
            state_name.write(
                arg=f"{state['state']}",
                align="center",
                move=False,
                font=("Arial Black", 11, "normal")
            )
            correct_guesses += 1
            data_dict.remove(state)
            time.sleep(1)
    if correct_guesses == 50:
        game_on = False
        time.sleep(4)
        sc.bye()

sc.mainloop()
