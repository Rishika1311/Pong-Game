import time
import turtle as t
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
screen = t.Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.tracer(0)
screen.listen()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
r_paddle.speed("fastest")
l_paddle.speed("fastest")


screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
is_True = True
while is_True:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.inc_l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.inc_r_point()
screen.exitonclick()

