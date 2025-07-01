from turtle import Turtle
import time

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("PaleGoldenrod")
        self.r_score = 0
        self.l_score = 0
        self.display_score()

    def display_score(self):
        # Clear previous score and write updated scores
        self.clear()
        self.goto(120,200)
        self.write(f"{self.r_score}", align="center", font=("courier", 35, "bold"))
        self.goto(-120,200)
        self.write(f"{self.l_score}", align="center", font=("courier", 35, "bold"))