from turtle import Screen
import time
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

CAR_SPEED = 0.1

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

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_score()


screen.exitonclick()
