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
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    #Detect when player reaches top
    if player.ycor() > 280:
        player.start_position()
        car_manager.increase_speed()
        scoreboard.level_up()

    #Detect when player hits a car
    if car_manager.detect_collision(player):
        scoreboard.game_over()
        game_over = True


screen.exitonclick()