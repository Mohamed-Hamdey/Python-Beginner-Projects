from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.s_count = 1
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.color("black")
        self.update_score()
        self.m_speed = 0.1

    def update_score(self):
        self.goto(-270, 260)
        self.write(f"Level {self.s_count} :", align="left", font=FONT)

    def point(self):
        self.s_count += 1
        self.clear()
        self.update_score()

    def game_speed(self):
        self.m_speed *= 0.6

    def game_over(self):
        over = Turtle()
        over.color("red")
        over.penup()
        over.hideturtle()
        over.speed("fastest")
        over.write("Game Over !", align="center", font=("Courier", 27, "normal"))
