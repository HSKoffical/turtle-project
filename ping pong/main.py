import time
from turtle import Screen
from paddle import Paddle
from paddle2 import Paddle2
from ball import Ball
from scoreboard import Scoreboard
screen=Screen()
paddle1=Paddle((350,0))
paddle2=Paddle2((-350,0))
ball=Ball()
screen.setup(800,600)
screen.bgcolor("black")
screen.listen()
ball.move_ball()
score_board=Scoreboard()
screen.tracer(0)
paddle1.create_paddle1()
paddle2.create_paddle2()
score_board.right_turtle()
score_board.right_score()
score_board.left_turtle()
score_board.left_score()
screen.onkey(fun=paddle1.move_up,key="Up")
screen.onkey(fun=paddle1.move_down,key="Down")
screen.onkey(fun=paddle2.move_up,key="w")
screen.onkey(fun=paddle2.move_down,key="s")
game_on=True
x_axis=True
while game_on:


        time.sleep(ball.move_speed)
        screen.update()
        ball.move_ball()
        if ball.ycor() > 300 or ball.ycor() < -300:
            # time.sleep(0.2)
            # screen.update()
            ball.ball_bounce_y()
        if ball.xcor()>400 or ball.xcor()<-400:
            if ball.xcor()>400:
                score_board.leftscoreupdate()
                time.sleep(0.4)
                ball.reset_ball()
                ball.move_ball()
            if ball.xcor()<-400:
                score_board.rightscoreupdate()
                time.sleep(0.4)
                ball.reset_ball()
                ball.move_ball()
        if ball.distance(paddle1)<40 and ball.xcor()>340:
            ball.ball_bounce_x()

        if ball.distance(paddle2)<50 and ball.xcor()<-340:
            ball.ball_bounce_x()
        # if


screen.exitonclick()