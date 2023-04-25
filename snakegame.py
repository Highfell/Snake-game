import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from tkinter import messagebox


screen = Screen()
screen.setup(width=1005, height=995)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.colormode(255)

snek = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True

new_game = True

while new_game:

    screen.onkey(snek.move_up, "Up")
    screen.onkey(snek.move_down, "Down")
    screen.onkey(snek.move_left, "Left")
    screen.onkey(snek.move_right, "Right")
    screen.listen()

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snek.move()
        food.create_snack()

        if snek.snake[0].distance(food.snacks) < 15:
            Food.foodcount -= 1
            scoreboard.increase_score()
            snek.extend()
            scoreboard.update_scoreboard()
            food.snacks.goto(1000, 1050)  # move the food off-screen

        #detect collision with self
        for segment in snek.snake[1:]:
            if snek.snake[0].distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()



        #detect collision with wall
        if snek.snake[0].xcor() > 481 or snek.snake[0].xcor() < -500 or snek.snake[0].ycor() > 501 or snek.snake[0].ycor() < -501:
            game_is_on = False
            scoreboard.game_over()

#ask user if they want to play again

    else:  
        play_again = messagebox.askyesno("Game over", f"You ate {scoreboard.score} foods\nDo you want to play again?")
        if play_again:
            scoreboard.reset_scoreboard()
            snek.reset()
            snek.create_snake()
            screen.update()
            game_is_on = True
        else:
            new_game = False
            screen.bye()


screen.exitonclick()