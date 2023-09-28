FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()  # turtle hidden
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-270, 270)
        self.write(f"the score is: {self.score}", align="left",
                   font=("Courier", 20, "normal"))

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-0, 0)
        self.write("GAME OVER", align="center",
                   font=("Courier", 20, "normal"))





