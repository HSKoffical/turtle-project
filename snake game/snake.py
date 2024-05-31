
from turtle import Turtle
MOVE_DISTANCE=20
POSITION=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake():
    def __init__(self):
        self.list_snake = []
        # self.creat_snake()
        
    def creat_snake(self):
        for i in POSITION:
            self.add_segment(i)
    def add_segment(self,i):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(i)
        self.list_snake.append(snake)
    def extend(self):
        self.add_segment(self.list_snake[-1].position())
    def move(self):
        for seg_num in range(len(self.list_snake) -1, 0, -1):
            new_x = self.list_snake[seg_num - 1].xcor()
            new_y = self.list_snake[seg_num - 1].ycor()
            self.list_snake[seg_num].goto(new_x, new_y)

        self.list_snake[0].forward(MOVE_DISTANCE)

    def move_left(self):
        if self.list_snake[0].heading() != RIGHT:
            self.list_snake[0].setheading(LEFT)
    def move_right(self):
        if self.list_snake[0].heading() != LEFT:
            self.list_snake[0].setheading(RIGHT)
    def move_up(self):
        if self.list_snake[0].heading() != DOWN:
            self.list_snake[0].setheading(UP)
    def move_down(self):
        if self.list_snake[0].heading() != UP:
            self.list_snake[0].setheading(DOWN)



snakes=Snake()