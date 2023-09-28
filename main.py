import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car = CarManager()
the_player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(the_player.go_up,"Up")
screen.onkey(the_player.go_down,"Down")

game_is_on = True
while game_is_on:
    # every 0.1 sec a new car must be created
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()

    #detect car collision
    for index in car.all_cars:
        if index.distance(the_player)<20:
            scoreboard.game_over()
            game_is_on = False
    #detect collision with wall end
    if the_player.ycor() >= 290:
        the_player.go_to_start()
        scoreboard.clear()
        scoreboard.increase_score()
        car.car_speed()

screen.exitonclick()