from turtle import Turtle
#from food import Food
ALIGMENT = "center"
FONT = ("Arial", 20, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(arg=f"Score: {self.score}", align=ALIGMENT, font=FONT)
        self.hideturtle()

    def game_over(self):
        self.write(arg=f"Score: {self.score}", align=ALIGMENT, font=FONT)
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", align=ALIGMENT, font=FONT)
