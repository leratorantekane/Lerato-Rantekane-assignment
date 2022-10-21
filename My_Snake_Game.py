import random
import turtle
import time


my_score = 0
high_scores = 0
snake_delay = 0.1
screen = turtle.Screen()
screen.title("My Snake Game")
screen.bgcolor("light blue")
screen.setup(width = 500, height = 500)
screen.tracer(0)

my_snake = turtle.Turtle()
my_snake.penup()
my_snake.goto(0,0)
my_snake.speed(0)
my_snake.shape("circle")
my_snake.color("blue")
my_snake.direction = "stop"

prey = turtle.Turtle()
prey.penup()
prey.goto(0,100)
prey.shape("circle")
prey.color("green")
prey.speed(0)
segments = []

board = turtle.Turtle()
board.penup()
board.hideturtle()
board.shape("square")
board.color("black")
board.goto(0,180)
board.speed(0)
board.write("Score: 0 High Scores: 0", align = "center", font=("ds-digital", 24, "normal"))

def move_up():
    if my_snake.direction != "down":
        my_snake.direction = "up"

def move_down():
    if my_snake.direction != "up":
        my_snake.direction = "down"

def move_right():
    if my_snake.direction != "left":
        my_snake.direction = "right"

def move_left():
    if my_snake.direction != "right":
        my_snake.direction = "left"

def snake_movements():
    if my_snake.direction == "up":
        y = my_snake.ycor()
        my_snake.sety(y+20)

    if my_snake.direction == "down":
        y = my_snake.ycor()
        my_snake.sety(y-20)

    if my_snake.direction == "right":
        x = my_snake.xcor()
        my_snake.setx(x+20)

    if my_snake.direction == "left":
        x = my_snake.xcor()
        my_snake.setx(x+20)

    screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")

while True:
    screen.update()
    if my_snake.xcor()  >290 or my_snake.xcor() < -290 or my_snake.ycor() > 290 or my_snake.ycor() < -290:
        time.sleep(1)
        my_snake.goto(0,0)
        my_snake.direction = "stop"

        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()
        my_score = 0
        delay = 0.1

        board.clear()
        board.write("score: {} High Score: {}".format(my_score, high_scores), align="center", font=("ds-digital", 24, "normal"))

    if my_snake.distance(prey) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        prey.goto(x,y)

        add_segment = turtle.Turtle()
        add_segment.shape("circle")
        add_segment.color("blue")
        add_segment.speed(0)
        add_segment.penup()
        segments.append(add_segment)

        delay -= 0.001
        my_score += 10

        if my_score > high_scores:
            high_scores = my_score
        board.clear()
        board.write("score: {} High Score: {}".format(my_score, high_scores), align="center", font=("ds-digital", 24, "normal"))

        for i in range(len(segments)-1,0,-1):
            x = segments[i-1].xcor()
            y = segments[i-1].ycor()
            segments[0].goto(x,y)

        snake_movements()

        for segment in segments:
            if segment.distance(my_snake) < 20:
                time.sleep(1)
                my_snake.goto(0,0)
                my_snake.direction = "stop"

                for segment in segments:
                    segment.goto(1000,1000)
                segments.clear()
                score = 0
                delay = 0.1

                board.clear()
                board.write("score: {} High Score: {}".format(my_score, high_scores), align="center", font=("ds-digital", 24, "normal"))

        time.sleep(delay)
        screen.mainloop()


            

