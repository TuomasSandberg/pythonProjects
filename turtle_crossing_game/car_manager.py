import random
from turtle import Turtle
from random import randint, random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def move_car(self):
        for car in self.cars:
            car.backward(self.speed)
    def create_cars(self):
        random_chance = randint(1, 6)
        if random_chance == 1:  # roll the dice to create a car only when 1 or 5
            car = Turtle("square")
            car.penup()
            starting_position = randint(-250, 250)
            car.goto(x=300, y=starting_position)
            car.shapesize(1, 2)
            car.color(COLORS[randint(0, 5)])
            self.cars.append(car)

    def increase_car_speed(self):
        self.speed += MOVE_INCREMENT










