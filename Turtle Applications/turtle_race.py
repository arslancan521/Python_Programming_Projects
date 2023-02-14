from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Bet For Winner",prompt="Bet Your Winner Turtle with Its Color :")
colors = ["red","orange","black","yellow","green","blue"]
y_coordinates = [-70, -40, -10, 20, 50, 80]


turtle_list = []
race_on = False

for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_coordinates[turtle_index])
    turtle_list.append(tim)

if user_bet:
    race_on = True

while race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won, the winner turtle is {winning_color}")
            else:
                print(f"You lost, the winning turtle is {winning_color}")
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()
