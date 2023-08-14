from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.level_up()

    def level_up(self):
        self.clear()
        self.penup()
        self.goto(x=-150, y=250)
        self.hideturtle()
        self.write(f"Level:{self.score}", False, align="right", font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", move=False, align="center", font=FONT)
