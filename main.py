import time
from turtle import Screen, Turtle
import pandas

df = pandas.read_csv("50_states.csv")

states_list = df["state"].to_list()
x_positions = df["x"].tolist()
y_positions = df["y"].tolist()

data_dict = []

for i in range(50):
    temp_tuple = (x_positions[i], y_positions[i])
    temp_dict = {"state": states_list[i], "position": temp_tuple}
    data_dict.append(temp_dict)

sc = Screen()
sc.title("US states quiz.")
sc.setup(width=725, height=491)
sc.bgpic("blank_states_img.gif")

state_name = Turtle()
state_name.hideturtle()
state_name.penup()

game_on = True
correct_guesses = 0
while game_on:
    user_guess = (sc.textinput(title=f"{correct_guesses}/50", prompt="Type an state's name:")).title()
    for state in data_dict:
        if user_guess == state["state"]:
            state_name.goto(state["position"])
            state_name.write(
                arg=f"{state['state']}",
                align="center",
                move=False,
                font=("Gautami", 8, "normal")
            )
            correct_guesses += 1
            time.sleep(1)


sc.mainloop()
