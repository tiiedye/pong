# Pong
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen. bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle()
r_paddle.goto(350, 0)

l_paddle = Paddle()
l_paddle.goto(-350, 0)

screen.listen()
screen.onkeypress(r_paddle.up_arrow, "Up")
screen.onkeypress(r_paddle.down_arrow, "Down")
screen.onkeypress(l_paddle.up_w, "w")
screen.onkeypress(l_paddle.down_s, "s")

game_on = True
while game_on:
    screen.update()


# Exit after all code is complete
screen.exitonclick()
