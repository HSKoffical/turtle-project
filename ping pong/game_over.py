from turtle import Turtle
class Game_over(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.write("game over",False,"center",font=("Arial",15,"normal"))
        self.hideturtle()
