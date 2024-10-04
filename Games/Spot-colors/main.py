import turtle as t
from random import choice

h = t.Turtle()
screen = t.Screen()
screen.bgcolor("black")

color_list = [(110, 170, 216), (214, 168, 75), (234, 223, 228), (12, 30, 74), (226, 215, 84), (175, 77, 28),
              (157, 19, 33), (8, 55, 27), (27, 180, 191), (38, 113, 136), (30, 131, 54), (15, 49, 134), (208, 159, 34),
              (234, 205, 11), (17, 97, 37), (228, 90, 36), (37, 176, 170), (101, 113, 192), (204, 73, 119),
              (68, 20, 10), (153, 19, 14), (132, 178, 158), (195, 139, 154), (138, 210, 232), (14, 92, 99),
              (158, 211, 195), (175, 186, 218), (223, 174, 185), (226, 178, 166), (100, 60, 21)]

h.penup()
h.hideturtle()
h.speed("fastest")
t.colormode(255)
h.setheading(255)
h.forward(300)
h.setheading(0)


def draw():
    for y in range(10):
        h.dot(10, choice(color_list))
        h.forward(30)


def moving():
    h.setheading(90)
    h.forward(30)
    h.setheading(180)
    h.forward(300)
    h.setheading(360)


for i in range(10):
    draw()
    moving()

screen.exitonclick()
