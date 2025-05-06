from turtle import Turtle

class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    # Draw a dash line on given y coordinates.
    def draw(self, y_coordinates = 0, line_length = 10, space_length = 5, line_count = 10):
        self.teleport(400,y_coordinates)
        self.setheading(180)
        for _ in range(line_count):
            self.pendown()
            self.forward(line_length)
            self.penup()
            self.forward(space_length)