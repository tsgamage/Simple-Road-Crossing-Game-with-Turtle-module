import random
import time
from turtle import Screen
from roads import Road
from player import Player
from car import Car
from scoreboard import Scoreboard

# Setting up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0) # stops the screen from updating automatically.
screen.title("Road Crossing Game")

# Creating the objects
player = Player() # Create the player object.
scoreboard = Scoreboard() # Add the level counter to the screen.
road = Road() # Draw the roads on the screen

# Drawing the roads
for y_cord in range(-300, 300, 40):
    road.draw(y_cord, line_count=60)


# Spawn cars randomly
car_obj: list = list()
recent_y_cords = [0] # Tracks the recent y coordinates of cars spawned.
y_cords = (-240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240)
spawn_count = 0 # Number of times the cars have been spawned. Used to control the number of cars spawn.
spawn_rate = 3 # Just a number to control the car spawn amount by dividing the spawn_count by this number

# Generate random y coordinates for cars to spawn on
def generate_random_y_cord():
    cord = random.choice(y_cords)
    if cord == recent_y_cords[-1]:
        generate_random_y_cord()
    return cord

# Spawn cars randomly on the screen and move them to a random y coordinate from the list of y coordinates.
def spawn_car():
    car = Car()
    car_obj.append(car)
    random_y_cord = generate_random_y_cord()
    car.teleport(400, random_y_cord)
    recent_y_cords.append(random_y_cord)

# Control the player with keyboard keys.
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_down, "s")

_game_running = True
_game_tick_speed = 0.1 # The speed that updates the whole game. Increased when the player reaches the next level.
spawned_car_count = 0 # Count the number of cars spawned. Used to update the screen
while _game_running:

    # If the number of cars spawned is more than 70, update the screen. It's always cars when the game launched.
    if spawned_car_count >70:
        screen.update()
        time.sleep(_game_tick_speed)

    # Check whether the player has reached the top of the screen. If so, update the game level and increase the game speed.
    if player.ycor() == 280:
        player.go_to_start() # reset the player to the start position.
        scoreboard.level_up()
        _game_tick_speed *= 0.7 # Decrease the game speed.

    # Spawn the cars only if the spawn_count is divisible by the spawn_rate.
    # This ensures that the cars spawn at regular intervals.
    if spawn_count % spawn_rate  == 0:
        spawn_car()

    for obj in car_obj:
        # Check if the player hit a car. If true, stop the game loop and show the game over
        if int(player.distance(obj)) < 40 and player.ycor() == obj.ycor() :
            _game_running = False
            print("Game Over!")
            scoreboard.game_over()

        # Check if a car passes the game window. If it, then remove that car object from the object list
        # so it's straightforward to move cars when the game goes further
        if obj.xcor() < -450:
            car_obj.remove(obj)
            obj.hideturtle()

        # move the cars forward
        obj.move_forward()

    spawn_count += 1
    spawned_car_count += 1

screen.mainloop()