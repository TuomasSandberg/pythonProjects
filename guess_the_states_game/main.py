import turtle
import pandas
from io import StringIO

screen = turtle.Screen()
screen.title("U.S States Game")
img = "blank_states_img.gif"

screen.addshape(img)
turtle.shape(img)


"""How to get x and y values"""
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()
guesses = []
correct_guess_count = 0
while len(guesses) < 50:
    states = pandas.read_csv("50_states.csv")
    states_list = states["state"].to_list()
    answer_state = screen.textinput(title=f"{correct_guess_count}/{len(states)} correct answers", prompt="Whats another states name?").title()
    if answer_state == "Exit":
        break
    #for state in states["state"]:
    if answer_state in states_list:
        answer = states[states["state"] == answer_state]
        x = int(answer["x"].iloc[0]) # https://stackoverflow.com/questions/76256618/how-to-deal-with-futurewarning-regarding-applying-int-to-a-series-with-one-item
        y = int(answer["y"].iloc[0]) # https://stackoverflow.com/questions/76256618/how-to-deal-with-futurewarning-regarding-applying-int-to-a-series-with-one-item
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(x, y)
        text.write(answer_state, move=True)
        guesses.append(answer_state)
        correct_guess_count += 1

for guess in guesses:
    if guess in states_list:
        states_list.remove(guess)
# states_dict = {
#     "Learn these states": states_list
# }
table_states = pandas.DataFrame(states_list)
table_states.to_csv("states_to_learn.csv")
