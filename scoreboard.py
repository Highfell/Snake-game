#create a scoreboard class that keeps track of the score and displays it on the top of the screen, inherits from the turtle class
# Path: scoreboard.py

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    
        def __init__(self):
            super().__init__()
            self.score = 0
            self.color("white")
            self.penup()
            self.hideturtle()
            self.goto(0, 400)
            self.update_scoreboard()
    
        def update_scoreboard(self):
            self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    
        def increase_score(self):
            self.score += 1
            self.clear()
            self.update_scoreboard()
    
        def game_over(self):
            self.goto(0, 100)
            self.write("GAME OVER", align='center', font=FONT)

        def reset_scoreboard(self):
            self.score = 0
            self.clear()
            self.goto(0, 400)
            self.update_scoreboard()

