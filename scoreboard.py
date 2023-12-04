from turtle import  Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        # self.highscore = 0
        self.color("white")
        self.penup()
        self.goto(0 , 280)
        self.hideturtle()
        with open("highscore.txt") as high:
            self.highscore = int(high.readline().rstrip())
        self.updatescore()






    def updatescore(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.highscore}" , align="center", font=("Courier", 14, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open('highscore.txt' , 'w') as high:
            high.write(f"{self.highscore}")
        self.score = 0
        self.updatescore()


    # def game_over(self):
    #     self.goto(0 , 0 )
    #     self.write(f"Game Over", align="center", font=("Courier", 14, "normal"))


    def increase_score(self):
        self.score += 1
        self.updatescore()