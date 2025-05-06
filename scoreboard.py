from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(0,270)
        self.score = 0
        self.update_scoreboard()

    # Increase the level by 1
    def level_up(self):
        self.score += 1
        self.update_scoreboard()

    # Show a game over message when the player loses
    def game_over(self):
        self.box_beside_text()
        self.goto(0,-20)
        self.color("white")
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

    # Show a box besides the game over message when the player loses
    def box_beside_text(self):
        self.color("red")
        self.goto(-100,-25)
        self.begin_fill()
        for _ in range(2):
            self.forward(200)
            self.left(90)
            self.forward(50)
            self.left(90)
        self.end_fill()

    # Clear the previous score and write a new score
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=("Courier", 18, "bold"))