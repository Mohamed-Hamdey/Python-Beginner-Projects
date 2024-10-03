from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as d:
            self.h_score = d.read()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.h_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > int(self.h_score):
            self.h_score = self.score
            with open("data.txt", mode="w") as d:
                d.write(str(self.score))
            self.score = 0
            self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
