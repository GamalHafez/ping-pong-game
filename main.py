from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Set up screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=800, height=600)
screen.title("PingPong Game")
screen.tracer(0)  # Turn off automatic screen updates

# Create game objects
score = Score()
ball = Ball()
r_paddle = Paddle((350, 0))   # Right paddle
l_paddle = Paddle((-350, 0))  # Left paddle

# Keyboard controls
screen.listen()
screen.onkey(r_paddle.goup, "Up")
screen.onkey(r_paddle.godown, "Down")
screen.onkey(l_paddle.goup, "w")
screen.onkey(l_paddle.godown, "s")

default_sleep = 0.1  # Controls ball speed

# Game loop
game_on = True
while game_on:
    screen.update()
    score.display_score()

    # Move the ball
    ball.goto(ball.xcor() + ball.x_move, ball.ycor() + ball.y_move)

    # Bounce off paddles
    if (ball.xcor() >= 335 and ball.distance(r_paddle) <= 50 or 
        ball.xcor() <= -335 and ball.distance(l_paddle) <= 50):
        default_sleep *= 0.9  # Increase speed slightly
        ball.x_move *= -1     # Reverse direction

    # Bounce off top and bottom walls
    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.y_move *= -1

    # Right player misses
    if ball.xcor() > 400:
        score.l_score += 1
        ball.goto(0, 0)
        ball.x_move *= -1
        default_sleep = 0.1

    # Left player misses
    if ball.xcor() < -400:
        score.r_score += 1
        ball.goto(0, 0)
        ball.x_move *= -1
        default_sleep = 0.1

    # Check for winner
    if score.r_score == 3 or score.l_score == 3:
        score.display_score()
        game_on = False

    time.sleep(default_sleep)  # Control ball speed

# Close the game on click
screen.exitonclick()
