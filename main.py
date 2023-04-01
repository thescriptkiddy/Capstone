import random
from turtle import Turtle, Screen
import time
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Capstone Project")
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
player.color("black")
car_manager = CarManager()


screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()


screen.exitonclick()
