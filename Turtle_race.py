from turtle import Turtle, Screen
import random

s = Screen()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]   
s.setup(width=500, height=400)
user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ") # This is a pop-up window
all_turtles = []

race_is_on = False
for t_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[t_index])
    new_turtle.penup()
    new_turtle.goto(x=-200, y=y_positions[t_index])
    all_turtles.append(new_turtle)
if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print(f"You've won! The {wining_color} turtle is the winner!")
            else:
                print(f"You've lost! The {wining_color} turtle is the winner!")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

s.exitonclick()
