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
y_cords = (-240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240)
spawn_count = 0
spawn_rate = 3

def generate_random_y_cord():
    cord = random.choice(y_cords)
    if cord == recent_y_cords[-1]:
        generate_random_y_cord()
    return cord

def spawn_car():
    car = Car()
    car_obj.append(car)
    random_y_cord = generate_random_y_cord()
    car.teleport(400, random_y_cord)
    recent_y_cords.append(random_y_cord)

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_down, "s")

_game_running = True
_game_tick_speed = 0.1
spawned_car_count = 0
while _game_running:
    if spawned_car_count >70:
        screen.update()
        time.sleep(_game_tick_speed)
    if player.ycor() == 280:
        player.go_to_start()
        _game_tick_speed *= 0.7

    if spawn_count % spawn_rate  == 0:
        spawn_car()

    for obj in car_obj:
        if player.distance(obj) < 40 and player.ycor() == obj.ycor() :
            _game_running = False
            print("Game Over!")

        if obj.xcor() < -450:
            car_obj.remove(obj)
            obj.hideturtle()
        obj.move_forward()

    spawn_count += 1
    spawned_car_count += 1
screen.mainloop()