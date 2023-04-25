# Class that imports turtle and creates a snake object

from turtle import Turtle
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_snake = Turtle("square")
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            new_snake.color(r, g, b)
            new_snake.penup()
            new_snake.goto(position)
            self.snake.append(new_snake)

    def extend(self):
            new_snake = Turtle("square")
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            new_snake.color(r, g, b)
            new_snake.penup()
            new_snake.goto(self.snake[-1].xcor(), self.snake[-1].ycor())
            self.snake.append(new_snake)

    def move(self):
        for body in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[body -1].xcor()
            new_y = self.snake[body -1].ycor()
            self.snake[body].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)
        #print("Head coordinate: ({}, {})".format(self.snake[0].xcor(), self.snake[0].ycor())) # FOR DEBUGGING 
        #print("Tail coordinate: ({}, {})".format(new_x, new_y))    # FOR DEBUGGING

    def move_up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def move_down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)
    
    def move_left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)
    
    def move_right(self):  
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def reset(self):
        for body in self.snake:
            body.goto(1000, 1000)
        del self.snake[:]
        self.snake.clear()

    

