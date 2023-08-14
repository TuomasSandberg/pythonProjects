import random
from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")


def draw_picture():
    turns = 3
    while turns < 11:
        screen.colormode(255)
        timmy.pencolor(randint(0, 255),
                       randint(0, 255),
                       randint(0, 255))
        for _ in range(turns):
            timmy.forward(100)
            timmy.right(360 / turns)
        turns += 1


def random_walk():
    direction = [0, 90, 180, 270]
    for _ in range(200):
        timmy.pensize(15)
        timmy.forward(30)
        timmy.setheading(random.choice(direction))
        screen.colormode(255)
        timmy.pencolor(randint(0, 255),
                       randint(0, 255),
                       randint(0, 255))


def spirograph():
    for _ in range(36):

        timmy.pencolor(randint(0, 255),
                       randint(0, 255),
                       randint(0, 255))
        timmy.circle(100)
        timmy.left(10)



if __name__ == "__main__":
    screen.colormode(255)
    timmy.speed("fastest")
    spirograph()
    random_walk()
    draw_picture()
    screen.exitonclick()
