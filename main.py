# Pong
from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen. bgcolor("black")
screen.title("Pong")

paddle_1 = Paddle()
paddle_1.goto(350, 0)

paddle_2 = Paddle()
paddle_2.goto(-350, 0)

screen.listen()
screen.onkeypress(paddle_1.up_arrow, "Up")
screen.onkeypress(paddle_1.down_arrow, "Down")
screen.onkeypress(paddle_2.up_w, "w")
screen.onkeypress(paddle_2.down_s, "s")


# Exit after all code is complete
screen.exitonclick()
