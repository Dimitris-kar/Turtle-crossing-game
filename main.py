from turtle import Screen
from player import Player
from score import Score
from car_manager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossing Game')
screen.bgpic('background.png')

screen.tracer(0)  # pause the animation

player = Player()
car_manager = CarManager()
score = Score()

screen.listen()
screen.onkeypress(player.go_up, 'w')
screen.onkeypress(player.go_down, 's')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()  # start the animation again
    car_manager.create_new_car()
    car_manager.move_cars()

    # detect when change stage
    if player.ycor() > 240:
        player.next_stage()
        score.update_score()
        car_manager.level_up()

    # detect collision with a car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.game_over()


screen.exitonclick()
