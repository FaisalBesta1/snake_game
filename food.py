from turtle import Turtle
import random

# Creates food for turtle and function to relocate food once eaten.


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.speed(0)
        self.goto(random_x, random_y)

    def new_location(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)

