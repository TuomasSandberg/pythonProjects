import time
from turtle import Screen
from player import Player
from car_manager import CarManager

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
level = Scoreboard()

# move player
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_car()
    if player.ycor() == 280:
        player.new_level()
        level.level_up()
        car_manager.increase_car_speed()
    for car in car_manager.cars:
        if (player.distance(car) < 25 and player.xcor() < car.xcor() - 10
                or player.distance(car) < 25 and player.ycor() < car.ycor() - 10):
            game_is_on = False
            level.game_over()

screen.exitonclick()
