from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        #Generate food in random position
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("yellow")
        self.speed("fastest")
        self.new_position()
    
    def new_position(self):
        #Generate new position of food
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)    