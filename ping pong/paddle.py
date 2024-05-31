from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position ):
        super().__init__()
        self.position=position
    def create_paddle1(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(350, 0)
    def move_up(self):
        new_y=self.ycor()+20
        self.goto(350,new_y)
    def move_down(self):
        new_y=self.ycor()-20
        self.goto(350,new_y)