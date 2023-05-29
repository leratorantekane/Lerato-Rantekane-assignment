import random
import turtle
import time

# scores
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
my_snake = turtle.Turtle()
my_snake.speed(0)
my_snake.shape("circle")
my_snake.color("blue")
my_snake.penup()
my_snake.goto(0, 0)
my_snake.direction = "stop"

# the snake's food
prey = turtle.Turtle()
prey.speed(0)
prey.shape("square")
prey.color("green")
prey.penup()
prey.goto(0, 100)

segments = []

# scoreboards
board = turtle.Turtle()
board.speed(0)
board.shape("square")
board.color("black")
board.penup()
board.hideturtle()
board.goto(0, 260)
board.write("Score: 0 High Scores: 0", align="center", font=("ds-digital", 24, "normal"))

# functionality
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
        my_snake.sety(y + 20)

    if my_snake.direction == "down":
        y = my_snake.ycor()
        my_snake.sety(y - 20)

    if my_snake.direction == "right":
        x = my_snake.xcor()
        my_snake.setx(x + 20)

    if my_snake.direction == "left":
        x = my_snake.xcor()
        my_snake.setx(x - 20)

# keyboard operations
screen.listen()
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_left, "a")

# looping
while True:
    snake_movements()  # Move the snake before updating the screen
    screen.update()

    # check collision with border
    if (
        my_snake.xcor() > 290
        or my_snake.xcor() < -290
        or my_snake.ycor() > 290
        or my_snake.ycor() < -290
    ):
        time.sleep(1)
        my_snake.goto(0, 0)
        my_snake.direction = "stop"

        # hide body segments
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        # reset score and delay
        my_score = 0
        delay = 0.1

        board.clear()
        board.write("Score: {} High Score: {}".format(my_score, high_scores), align="center",
                    font=("ds-digital", 24, "normal"))

    # check collision with the food
    if my_snake.distance(prey) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        prey.goto(x, y)

        # add a new segment to the head
        add_segment = turtle.Turtle()
        add_segment.speed(0.01)
        add_segment.shape("circle")
        add_segment.color("blue")
        add_segment.penup()
        segments.append(add_segment)

        # shorten the delay time
        delay -= 0.001
        # increase the score
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

        if len(segments) > 0:
            x = my_snake.xcor()
            y = my_snake.ycor()
            segments[0].goto(x, y)

    # check for collision with the body
    for segment in segments:
        if segment.distance(my_snake) < 20:
            time.sleep(1)
            my_snake.goto(0, 0)
            my_snake.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            my_score = 0
            delay = 0.1

            # update the score
            board.clear()
            board.write("Score: {} High Score: {}".format(my_score, high_scores), align="center",
                        font=("ds-digital", 24, "normal"))

    time.sleep(delay)


            

