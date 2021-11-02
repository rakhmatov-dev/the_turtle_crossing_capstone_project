from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.reset_turtle()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_turtle(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def is_it_finish(self):
        return self.ycor() >= FINISH_LINE_Y
