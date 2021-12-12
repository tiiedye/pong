# Pong
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen. bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))

l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_on = True
while game_on:
    screen.update()


# Exit after all code is complete
screen.exitonclick()
