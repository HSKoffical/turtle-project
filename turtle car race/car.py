import random
from turtle import Turtle
class Car():
    def __init__(self):
        self.color=["yellow","green","red","orange","blue","black","pink"]
        self.move_speed=0.1
        self.car_list=[]
    def turtle_car(self):
            random_num=random.randint(1,4)
            if random_num==1:
                self.car = Turtle()
                self.car.penup()
                # x = random.randint(200,300)
                y=random.randrange(-240,240)
                self.car.goto(300,y)
                self.car.shape("square")
                self.car.shapesize(stretch_len=2, stretch_wid=1)
                self.car.color(random.choice(self.color))
                self.car.setheading(180)
                self.car_list.append(self.car)
    def speed(self):
        self.move_speed*=0.5






