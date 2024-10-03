from turtle import Turtle
from random import choice, randint


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.CARS = []
        self.create_cars()

    def create_cars(self):
        r_choice = randint(1, 6)
        if r_choice == 6:
            car = Turtle("square")
            car.penup()
            car.speed("fastest")
            car.turtlesize(stretch_len=3, stretch_wid=1)
            car.color(choice(COLORS))
            car.goto(350, randint(-240, 240))
            self.CARS.append(car)

    def move(self):
        for car in self.CARS:
            car.backward(STARTING_MOVE_DISTANCE)
