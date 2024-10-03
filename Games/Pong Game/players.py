from turtle import Turtle


class Players(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.turtlesize(stretch_len=1, stretch_wid=5)

    def up(self):
        new_y = self.ycor() + 60
        self.sety(new_y)

    def down(self):
        new_y = self.ycor() - 60
        self.sety(new_y)
