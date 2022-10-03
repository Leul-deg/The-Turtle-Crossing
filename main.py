import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
manager = CarManager()
screen.listen()
screen.onkey(player.up,"Up")
game_is_on = True
while game_is_on:
    if player.ycor() >= 280:
        player.starting_position()
        scoreboard.update()
        manager.increase_speed()
    time.sleep(0.1)
    manager.create_car()
    manager.move_cars()
    for car in manager.all_cars:
        if player.distance(car) < 40:
            game_is_on = False
            scoreboard.game_over()

    screen.update()
screen.exitonclick()