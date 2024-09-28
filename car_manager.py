from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
COORDINATE=[-220,-160,-80,0,80,160]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
import random


class CarManager:
    def __init__(self):


        self.all_cars=[]
    def create_cars(self):
        rand_chance=random.randint(1,6)
        if rand_chance==1:
            new_car=Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_y=random.randint(-250,250)
            new_car.goto(270,new_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(MOVE_INCREMENT)


