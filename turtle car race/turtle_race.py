from turtle import Turtle
class Turtle_move(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
    def reset_turtle(self):
        self.goto(0,-280)
        self.setheading(90)
    def move_turtle(self):
        self.forward(10)
    def move_left(self):
        self.setheading(180)
        self.forward(10)
        self.setheading(90)
    def move_right(self):
        self.setheading(0)
        self.forward(10)
        self.setheading(90)
    def move_backward(self):
        self.backward(10)


