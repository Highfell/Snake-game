#create a food class that spawns food at random coordinates using the random and turtle modules

# Path: food.py

from turtle import Turtle
import random



class Food:

    foodcount = int(0)

    def __init__(self):
        self.snacks = Turtle("circle")
        self.snacks.penup()
        self.snacks.shapesize(stretch_len=0.9, stretch_wid=0.9)
        self.snacks.color("yellow")
        self.snacks.speed("fastest")
        self.create_snack()
    
    def create_snack(self):
        if Food.foodcount < 1:
            random_x = random.randint(-14, 14) * 20
            random_y = random.randint(-14, 14) * 20
            self.snacks.goto(random_x, random_y)
            Food.foodcount =+ 1
            print("Food Cordinate: ({}, {})".format(random_x, random_y))    # FOR DEBUGGING
