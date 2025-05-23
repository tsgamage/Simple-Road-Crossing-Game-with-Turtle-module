from turtle import Turtle

MOVE_DISTANCE = 40

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.teleport(0,-280)

    def go_to_start(self):
        self.teleport(0,-280)

    def go_up(self):
        if self.ycor() <= 270: # Check if the player is not going out of bounds.
            self.forward(MOVE_DISTANCE)

    def go_down(self):
        if self.ycor() >= -270: # Check if the player is not going out of bounds.
            self.backward(MOVE_DISTANCE)