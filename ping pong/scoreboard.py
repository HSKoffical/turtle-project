from turtle import Turtle
class Scoreboard():
    def __init__(self):
        self.right_tim=Turtle()
        self.left_tim=Turtle()
        self.right_tim_score=0
        self.left_tim_score=0
    def right_turtle(self):
        self.right_tim.hideturtle()
        self.right_tim.color("white")
        self.right_tim.penup()
        self.right_tim.goto(100,250)
    def right_score(self):

        self.right_tim.write(f"{self.right_tim_score}",False,"center",font=("Arial",40,"normal"))
    def rightscoreupdate(self):
        self.right_tim.clear()
        self.right_tim_score=self.right_tim_score+1
        self.right_score()
    def left_turtle(self):
        self.left_tim.hideturtle()
        self.left_tim.color("white")
        self.left_tim.penup()
        self.left_tim.goto(-50,250)
    def left_score(self):

        self.left_tim.write(f"{self.left_tim_score}",False,"center",font=("Arial",40,"normal"))
    def leftscoreupdate(self):
        self.left_tim.clear()
        self.left_tim_score=self.left_tim_score+1
        self.left_score()