from turtle import Turtle

class Ball(Turtle):
    def __init__ (self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.9)
        self.penup() # Prevent drawing when the ball moves
        self.x_move = 10  # Horizontal movement step
        self.y_move = 10  # Vertical movement step