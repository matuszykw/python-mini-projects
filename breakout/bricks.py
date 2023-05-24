from turtle import Turtle

class Brick(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.shape('square')
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(position)
        
        self.left_wall = self.xcor() - 30
        self.right_wall = self.xcor() + 30
        self.upper_wall = self.ycor() + 10
        self.bottom_wall = self.ycor() - 10