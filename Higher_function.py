#higher order function: Higher order function are the function which can be passed as an argument to another function

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()