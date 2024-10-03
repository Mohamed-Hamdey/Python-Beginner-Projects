import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

user = Player()
screen = Screen()
car = CarManager()
scorem = Scoreboard()


screen.title("Turtle Crossing Game :")
screen.setup(width=600, height=600)
screen.listen()
screen.onkey(user.move, "Up")

screen.tracer(0)


game_is_on = True
while game_is_on:
    time.sleep(scorem.m_speed)
    screen.update()
    for ca in car.CARS:
        if user.distance(ca) < 35:
            scorem.game_over()
            game_is_on = False
    if user.ycor() > 280:
        user.o_position()
        scorem.point()
        scorem.game_speed()
    car.create_cars()
    car.move()

screen.exitonclick()
