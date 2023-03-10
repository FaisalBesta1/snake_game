from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Creates the screen to allow the game to be played

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
position = [0, 20, 40]
segment = []

# Creates the snake and scoreboard on screen and allows movement of snake when specific keys have been pressed.

snake = Snake()
food = Food()
screen.update()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

scoreboard = Scoreboard()
screen.update()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.movement()
    snake.snake_stripe()

    # checks if food has been eaten

    if snake.head.distance(food) < 20:
        food.new_location()
        snake.extend()
        scoreboard.score_increase()

    # checks if snake has gone outside designated screen

    if snake.head.xcor() > 295 or snake.head.ycor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()
        scoreboard.reset()
        snake.reset_snake()

    # checks if snake has collided with itself

    for segment in snake.segment[2:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            scoreboard.reset()
            snake.reset_snake()


























screen.exitonclick()


