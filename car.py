from turtle import Turtle

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.shapesize(1,3)
        self.moving_speed = 10

    def move_forward(self):
        self.forward(self.moving_speed)