from turtle import Turtle, Screen
import time

screen = Screen()
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        # self.head_mod()

# creates the initial snake
    def create_snake(self):
        for sn in range(3):
            snake = Turtle("square")
            snake.color("medium sea green")
            snake.penup()
            snake.setpos(STARTING_POSITIONS[sn])
            self.segment.append(snake)

# when food is eaten, it extends the snake
    def extend(self):
        for sn in range(1):
            snake = Turtle("square")
            snake.color("medium sea green")
            snake.penup()
            self.segment.append(snake)

# causes the snake to move in the chosen direction
    def movement(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)

    def snake_stripe(self):
        snake_length = len(self.segment)
        if snake_length % 5 == 0:
            stripe = self.segment[snake_length - 1]
            stripe.color("white")

    def reset_snake(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.__init__()

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)



