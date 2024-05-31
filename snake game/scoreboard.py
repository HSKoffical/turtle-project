from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.i = 0
        self.penup()
        self.color("white")
        self.goto(-10,200)
        self.hideturtle()
        self.score()
    def score(self):
        self.write(f"Score: {self.i}  ", False, "center", font=("Arial", 17, "normal"))

    def score_increment(self):
        self.clear()
        self.i+=1
        self.score()
    def game_over(self):
        self.goto(0,0)
        self.write("Game over",False,"center",font=("Arial", 15, "normal"))


