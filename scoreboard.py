from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(x=-230, y=260)
        self.level = 0
        self.level_up()

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER!", align="center", font=FONT)
