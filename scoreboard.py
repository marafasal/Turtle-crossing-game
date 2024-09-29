from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.goto(-200,250)
        self.hideturtle()
        self.level=1
        self.score()

    def score(self):
        self.clear()
        self.write(f"Level:{self.level}", font=FONT)
    def score_increment(self):
        self.level+=1
        self.score()

