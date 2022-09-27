
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_right():
    tim.right(15)

def turn_left():
    tim.left(15)

def clear():
    screen.clear()
    tim.penup()
    tim.home()
    tim.pendown()


tim.pencolor("blue")
tim.pensize(10)


screen.listen()

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()


