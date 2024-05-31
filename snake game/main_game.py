from snake import Snake
from turtle import Turtle,Screen
import time
from eggs import Eggs
from scoreboard import Scoreboard
screen = Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.tracer(0)
snake=Snake()
snake.creat_snake()
egg=Eggs()
game_on = True
score_board=Scoreboard()
screen.listen()
screen.onkey(key="Left", fun=snake.move_left)
screen.onkey(key="Right", fun=snake.move_right)
screen.onkey(key="Up", fun=snake.move_up)
screen.onkey(key="Down", fun=snake.move_down)

while game_on:
    screen.update()
    time.sleep(0.3)
    snake.move()
    if snake.list_snake[0].distance(egg)<15:
        egg.move_egg()
        snake.extend()
        score_board.score_increment()
    if snake.list_snake[0].xcor()>240  or snake.list_snake[0].xcor()<-240 or snake.list_snake[0].ycor()>240 or snake.list_snake[0].ycor()<-240:
        score_board.game_over()
        game_on=False
    for segment in snake.list_snake:
        if snake.list_snake[0]==segment:
            pass
        elif snake.list_snake[0].distance(segment)<10:
            score_board.game_over()
            game_on=False

screen.exitonclick()