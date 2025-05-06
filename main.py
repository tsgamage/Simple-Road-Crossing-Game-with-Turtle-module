import random
import time
from turtle import Screen
from roads import Road
from player import Player
from car import Car

# Setting up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Road Crossing Game")

player = Player()
road = Road()

# Drawing the roads
for y_cord in range(-300, 300, 40):
    road.draw(y_cord, line_count=60)


# Spawn cars randomly
car_obj: list = list()
recent_y_cords = [0]
y_cords = (-280, -240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240, 280)
spawn_count = 0
spawn_rate = 4

def spawn_car():
    random_y_cord = random.choice(y_cords)

    car = Car()
    car_obj.append(car)
    car.teleport(400, random_y_cord)
    recent_y_cords.append(random_y_cord)

screen.listen()
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "s")

_game_running = True
while _game_running:
    time.sleep(0.1)

    if spawn_count % spawn_rate  == 0:
        spawn_car()

    for car in car_obj:
        if player.distance(car) < 40 and player.ycor() == car.ycor() :
            _game_running = False
            print("Game Over!")

        car.move_forward()


    screen.update()
    spawn_count += 1

screen.mainloop()