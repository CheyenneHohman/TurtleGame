import time 
from turtle import Screen 
# first created import statement 
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) #has everything move to its starting position

# Create our objects to manipulate 
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

#listen() detects inputs 
screen.listen()
# onkey = takes two inputs, what to do, what key does that 
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    # Sleep keeps the program from running too fast
    time.sleep(0.1)
    # This keeps the screen continuously updating; doesn't exit on click until the while loop is over
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.crossed_finish():
        player.reset_turtle()
        scoreboard.increase_level()
        car_manager.increase_speed()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()