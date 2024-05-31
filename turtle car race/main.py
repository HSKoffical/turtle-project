from turtle_race import Turtle_move
from turtle import Turtle,Screen
from car import Car
from game_over import Game_over
import time
screen=Screen()
screen.tracer(0)
screen.listen()
tr=Turtle_move()
tr.reset_turtle()
car=Car()
game_over=Game_over()
car.turtle_car()
game_over.level_show()
screen.onkey(fun=tr.move_turtle,key="Up")
screen.onkey(fun=tr.move_left,key="Left")
screen.onkey(fun=tr.move_right,key="Right")
screen.onkey(fun=tr.move_backward,key="Down")
game_on=True

while game_on:
    car.turtle_car()
    screen.update()
    time.sleep(car.move_speed)
    for i in car.car_list:
        if i.distance(tr)<23:
            game_over.gameover_show()
            game_on = False
        if tr.ycor()==300:
            car.speed()
            tr.reset_turtle()
            game_over.num+=1
            game_over.clear_level()



        i.forward(10)


    # car.car_move()
screen.exitonclick()

