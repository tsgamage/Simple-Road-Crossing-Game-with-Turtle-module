import time
from turtle import Screen
from roads import Road
from player import Player
from car import Car

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
road = Road()

car_obj: list = list()
for y_pos in range(-280,300,40):
    car = Car()
    car.teleport(300, y_pos)
    car_obj.append(car)


for i in range(-300, 300, 40):
    road.draw(y_coordinates=i, line_count=60)

screen.listen()
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "s")

_game_running = True
while _game_running:
    for car in car_obj:
        car.move_forward()
    time.sleep(0.1)
    screen.update()

screen.mainloop()
