import time
from turtle import Screen

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

screen.listen()

_game_running = True
while _game_running:
    time.sleep(0.1)
    screen.update()

screen.mainloop()