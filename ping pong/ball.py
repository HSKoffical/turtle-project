from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_new=10
        self.y_new=10
        self.move_speed=0.1
    def move_ball(self):

        x=self.xcor()+self.x_new
        y=self.ycor()+self.y_new
        self.goto(x,y)
    def ball_bounce_y(self):

        self.y_new=self.y_new*-1
    def ball_bounce_x(self):
        self.x_new=self.x_new*-1
        self.move_speed*=0.9
    def reset_ball(self):
        self.goto(0,0)
        self.move_speed=0.1
        self.ball_bounce_x()


