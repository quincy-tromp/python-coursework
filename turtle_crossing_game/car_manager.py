from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
     
    def __init__(self):
        self.cars = []
        self.generate_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(x=300, y=random.randint(-250,250))
            self.cars.append(new_car)
        
    def move_cars(self):
        for car in self.cars:
            if car.xcor() > -320:
                car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
            
    