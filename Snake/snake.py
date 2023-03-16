from turtle import Turtle

START_POSITIONS = [(0, 0), (0, -20), (0, -40)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in START_POSITIONS:
            self.add_segment(position)
    
    def move(self):
        snake_segments = self.snake_segments
        for seg_num in range(len(snake_segments)-1, 0, -1):
            new_pos = snake_segments[seg_num-1].position()
            snake_segments[seg_num].goto(new_pos)
        snake_segments[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        segment = Turtle(shape='square')
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_segments.append(segment)

    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def up(self):
        if self.head.heading() != 270: 
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90: 
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0: 
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180: 
            self.head.setheading(0)