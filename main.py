# TODO 1. Create screen | DONE
# TODO 2. Create player and move it | DONE
# TODO 3. Create scoreboard | DONE
# TODO 4. Create cars | DONE

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager()
scoreboard = Scoreboard()
player = Player()

screen.listen()
screen.onkey(key="Up", fun=player.move)

is_game_on = True
create_car = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    # create car
    if create_car:
        car_manager.create_car()
        create_car = False
    else:
        create_car = True

    # move cars
    car_manager.move_cars(scoreboard.level)

    # is it finish
    if player.is_it_finish():
        scoreboard.level_up()
        player.reset_turtle()

    # game over
    if car_manager.is_game_over(player):
        scoreboard.game_over()
        is_game_on = False

screen.exitonclick()
