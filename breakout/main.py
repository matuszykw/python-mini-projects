from turtle import Screen, Turtle
from paddle import Paddle
from bricks import Brick
from ball import Ball
import time

screen = Screen()
screen.setup(width=730, height=800)
screen.bgcolor('black')
screen.title('Breakout Game')
screen.tracer(0)

paddle = Paddle()
ball = Ball()

bricks = []
colors = ['red', 'orange', 'green', 'yellow']
color = colors[0]
color_iterator = 1
pos = (-320, 300)
for i in range(8):
    if i % 2 == 0 and i != 0:
        color = colors[color_iterator]
        color_iterator += 1
    for j in range(10):
        bricks.append(Brick(color, pos))
        x = pos[0]
        y = pos[1]
        pos = (x+70, y)
    y = pos[1] - 30
    pos = (-320, y)


screen.listen()
screen.onkeypress(paddle.go_right, 'Right')
screen.onkeypress(paddle.go_left, 'Left')


game_over = False
while not game_over:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    
    #* Detect collision with wall
    if ball.xcor() >= 345 or ball.xcor() <= -345:
        ball.bounce_x()
    if ball.ycor() >= 380:
        ball.bounce_y()
    
    #* Detect collision with paddle 
    if ball.ycor() <= -280 and ball.distance(paddle) < 50:
        ball.bounce_y()
        
    #* Detect collision with bricks
    for brick in bricks:
        if ball.distance(brick) < 25:
            brick.goto(3000, 3000)
            bricks.remove(brick)
            ball.bounce_y()
            
            if ball.xcor() < brick.left_wall:
                ball.bounce_x()
            elif ball.xcor() > brick.right_wall:
                ball.bounce_x()
            elif ball.ycor() < brick.bottom_wall:
                ball.bounce_y
            elif ball.ycor() > brick.upper_wall:
                ball.bounce_y()
    
    if ball.xcor() <= -380:
        game_over = True
    if len(bricks) == 0:
        game_over = True