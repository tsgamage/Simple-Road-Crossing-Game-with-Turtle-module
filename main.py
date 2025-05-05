import time
from turtle import Screen
from player import Player

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "s")


_game_running = True
while _game_running:
    time.sleep(0.1)
    screen.update()

screen.mainloop()