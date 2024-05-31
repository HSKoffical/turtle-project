import random
from turtle import Turtle,Screen
import time
s=Screen()
s.setup(600,600)
s.tracer(0)
l=[]



game_on=True
while game_on:
    tim = Turtle()
    x=300
    y=random.randrange(-200,300,70)
    tim.penup()
    tim.goto(x,y)
    tim.setheading(180)
    tim.shape("square")
    tim.shapesize(stretch_wid=1,stretch_len=2)
    l.append(tim)
    s.update()
    time.sleep(0.1)
    for j in l:

        j.forward(10)
s.exitonclick()
