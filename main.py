import turtle
from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
screen.title("Turtle Race")
userbet=screen.textinput(title="Make your bet",prompt="Who will win the bet? Choose a color")

colors=['red','yellow','green','purple','orange']
y_cord=[-100,-50,0,50,100]
all_turtle=[]
is_game_on=True

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230, y_cord[i])
    all_turtle.append(new_turtle)

if userbet:
    is_game_on=True

while is_game_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_game_on=False
            winning_color=turtle.pencolor()
            if winning_color==userbet:
                print(f"Youve won, the winning color is {winning_color}")
            else:
                print(f"Youve Lost, the winning color is {winning_color}")

        turtle.forward(random.randint(0,10))




screen.exitonclick()