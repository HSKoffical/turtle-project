import random
from turtle import Turtle

class Eggs(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("orange")
        self.penup()
        x = random.randint(-240, 240)
        y = random.randint(-240, 240)
        self.goto(x, y)
    def move_egg(self):
        x=random.randint(-240,240)
        y=random.randint(-240,240)
        self.goto(x,y)

