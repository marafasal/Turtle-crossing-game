import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
carmanager=CarManager()
scoreboard=Scoreboard()


screen.listen()

screen.onkey(player.move_up,key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_cars()
    carmanager.move_cars()
    for car in carmanager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            screen.exitonclick()
    if player.reach_end():
        player.end()
        carmanager.level_up()
        scoreboard.score_increment()




