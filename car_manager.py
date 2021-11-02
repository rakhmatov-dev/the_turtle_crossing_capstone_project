import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []

    def create_car(self):
        self.cars.append(Car())

    def move_cars(self, level):
        for car in self.cars:
            car.move(level)
            if car.xcor() < -310:
                self.cars.remove(car)

    def is_game_over(self, player):
        for car in self.cars:
            if car.distance(player) < 16:
                return True
        return False


class Car(Turtle):
    def __init__(self):
        super(Car, self).__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.penup()
        self.goto(x=300, y=random.randint(-200, 250))
        self.setheading(180)

    def move(self, level):
        self.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*(level-1))


