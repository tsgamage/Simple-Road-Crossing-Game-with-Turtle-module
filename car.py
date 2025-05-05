import random
from turtle import Turtle

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.shapesize(1,3)

    def move_forward(self):
        distance = random.randint(0,20)
        self.forward(distance)