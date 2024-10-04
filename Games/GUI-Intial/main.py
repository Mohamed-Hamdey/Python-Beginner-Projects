from turtle import Turtle, Screen
from prettytable import PrettyTable

table= PrettyTable()
table.add_column("Names", ["Mohamed_Hamdy" , "Marwan_Mohamed" ,"Ahmed_Alaa" ,"Omar_Osama"])
table.add_column("Ages" ,["18" ,"19" ,"18" ,"19"])
print(table.align)
print(table)

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)

print(timmy)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
