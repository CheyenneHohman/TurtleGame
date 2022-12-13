from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self): 
        super().__init__()
        print("creating scoreboard")
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-250, 250)
        self.hideturtle()
        self.update_scoreboard()

    #Update scoreboard 
    def update_scoreboard(self):
        self.write(f"LEVEL: {self.level}", move=False, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER. YOU MADE IT TO LEVEL: {self.level}", move=False, align="center", font=FONT)

    #Increase level after each successful reset 
    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()