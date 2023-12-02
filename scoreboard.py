from turtle import  Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0 , 280)
        self.hideturtle()
        self.updatescore()

    def updatescore(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 14, "normal"))


    def game_over(self):
        self.goto(0 , 0 )
        self.write(f"Game Over", align="center", font=("Courier", 14, "normal"))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.updatescore()