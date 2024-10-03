from turtle import Turtle, Screen
from players import Players
from ball import Ball
from scoreboard import Score
import time

h = Turtle()
screen = Screen()
left_paddle = Players()
right_paddle = Players()
ball = Ball()
score = Score()

screen.setup(width=1100, height=750)
screen.bgcolor("black")
screen.title("**  Pong Game  **")
screen.tracer(0)
screen.listen()
screen.onkey(left_paddle.up, "Up")
screen.onkey(left_paddle.down, "Down")
screen.onkey(right_paddle.up, "w")
screen.onkey(right_paddle.down, "s")

left_paddle.goto(-530, 0)
right_paddle.goto(525, 0)

ball.move()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 355 or ball.ycor() < -355:
        ball.bounce_y()

    if ball.distance(left_paddle) < 35 and ball.xcor() < -360 or ball.distance(right_paddle) < 35 and ball.xcor() > 360:
        ball.bounce_x()

    if ball.xcor() > 560:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -560:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
