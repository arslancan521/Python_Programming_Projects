from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

starting_positions = [(0,0), (-20,0), (-40,0)]
segments = []


for position in starting_positions:
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.goto(position)
    segments.append(snake)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.5)

    for snake in segments:
        snake.forward(20)





screen.exitonclick()