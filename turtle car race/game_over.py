from turtle import Turtle
class Game_over(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.num=1
        self.penup()
    def gameover_show(self):
        self.goto(0,0)
        self.write("Game over",False,"center",font=("Arial",20,"normal"))
    def level_show(self):
        self.goto(-250,250)
        self.write(f"level {self.num}",False,"center",font=("Arial",15,"normal"))
    def clear_level(self):
        self.clear()
        self.level_show()