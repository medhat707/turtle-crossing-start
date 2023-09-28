from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# here we don't inherit from the turtle class
# instread we create a separate class
# because we don't want to inherit all turtle attribbutes
# instead we will use only few attributes
# and we need to create as many objects with different turtle
# properties as we want
# here we stored different turtle objects inside a list


class CarManager:
    def __init__(self):
         # defining an empty list containing alll car objects
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        # new_car must take a different color an be initiated
        # from the right vertical side of screen
        # to disallow creating cars too frequently
        random_chance = random.randint(1,6)
        if random_chance ==1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid= 1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
             car.backward(self.speed)

    # increase car speed if player levels up
    def car_speed(self):
        self.speed += STARTING_MOVE_DISTANCE

    # def refresh(self):
    #     new_x= self.xcor() - MOVE_INCREMENT
    #     # new_y=self.ycor() + self.ymov
    #     self.goto(new_x,0)
    #
    # def move_left(self):
    #     self.refresh()



