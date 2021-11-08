# turtleRace.py
#
# Python Bootcamp Day 19 - Turtle Race
# Usage:
#      Bet on which turtle will win a race using the Turtle module.
#      Learn about higher order functions and event listeners.
#
# Marceia Egler Nov 8, 2021


from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
game_on = False
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will enter the race? Enter a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = -70
for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y += 30
    all_turtles.append(new_turtle)

if user_bet:
    game_on = True

while game_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You Lost! The {winning_color} turtle is the winner!")
            game_on = False
        rand_distance = random.randint(0,10)
        turtle.fd(rand_distance)





screen.exitonclick()






