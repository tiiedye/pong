from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up_arrow(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down_arrow(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def up_w(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down_s(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
