from turtle import Turtle
class level(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.goto(-250,250)
    def level_show(self):
        self.write(f"level {}",False,"center",font=("Arial",10,"normal"))
    def time_increase(self):
