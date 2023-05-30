import random
from token import AMPER
import turtle
import time

# reset score and delay
my_score = 0
high_scores = 0
delay = 0.1

# screen setup
screen = turtle.Screen()
screen.title("My Snake Game")
screen.bgcolor("light blue")
screen.setup(width=700, height=700)
screen.tracer(0)

# the snake head
snake_head = turtle.Turtle()
snake_head.speed(0)
snake_head.shape("circle")
snake_head.color("blue")
snake_head.penup()
snake_head.goto(0, 0)
snake_head.direction = "stop"

# the snake's food
prey = turtle.Turtle()
prey.speed(0)
prey.shape("square")
prey.color("green")
prey.penup()
prey.goto(0, 100)

# scoreboards
board = turtle.Turtle()
board.speed(0)
board.shape("square")
board.color("black")
board.penup()
board.hideturtle()
board.goto(0, 260)
board.write("Score: 0 High Scores: 0", align="center", font=("ds-digital", 24, "normal"))



# functionality to move the snake
def move_up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def move_down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def move_right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

def move_left():
    if snake_head.direction != "right":
        snake_head.direction = "left"


#function to move the snake
def snake_movements():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)

# keyboard operations
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")

segments = []

# Main game loop
while True:
    
    screen.update()
    #check collision with border
    if (
        snake_head.xcor() > 290
        or snake_head.xcor() < -290
        or snake_head.ycor() > 290
        or snake_head.ycor() < -290
    ):
        time.sleep(1)
        snake_head.goto(0, 0)
        snake_head.direction = "stop"

        # hide body segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        board.clear()
        board.write("Score: {} High Score: {}".format(my_score, high_scores), align="center",
                    font=("ds-digital", 24, "normal"))
        
        # check collision with the food
    if snake_head.distance(prey) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        prey.goto(x, y)

        # add a new segment to the head
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay time
        delay -= 0.001
        #increase the score
        my_score += 10

        if my_score > high_scores:
            high_scores = my_score
        board.clear()
        board.write("Score: {} High Score: {}".format(my_score, high_scores), align="center",
            font=("ds-digital", 24, "normal"))
        
    # move the segments in reverse
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    #move the 1st segment to where the head is
    if len(segments) &AMPER:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x,y)
    snake_movements() 

    # check for collision with the body
    for segment in segments:
        if segment.distance(snake_head) < 20:
            time.sleep(1)
            snake_head.goto(0, 0)
            snake_head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

            # update the score
            my_score = 0
            delay = 0.1
            board.clear()
            board.write("Score: {} High Score: {}".format(my_score, high_scores), align="center",
                font=("ds-digital", 24, "normal"))

    time.sleep(delay)








        





            

