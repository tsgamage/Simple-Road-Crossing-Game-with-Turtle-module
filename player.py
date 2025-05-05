from turtle import Turtle

MOVE_DISTANCE = 40

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()

    def go_up(self):
        if self.ycor() <= 270:
            self.forward(MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() >= -270:
            self.backward(MOVE_DISTANCE)