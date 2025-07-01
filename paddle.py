from turtle import Turtle

class Paddle(Turtle):
    def __init__ (self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position) # Start position (left or right)
        self.shapesize(5,0.5)

    def goup(self):
        # Move the paddle up by 40 pixels (only if within bounds)
        new_y = self.ycor() + 40
        if new_y < 260:
            self.goto(self.xcor(), new_y)

    def godown(self):
        # Move the paddle down by 40 pixels (only if within bounds)
        new_y = self.ycor() - 40
        if new_y > -260:
            self.goto(self.xcor(), new_y)
