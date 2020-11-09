# Pressure Pong


# By Roya


import turtle

import os

wn = turtle.Screen()

wn.title("Pressure Pong")

wn.bgcolor("white")

wn.setup(width=1000, height=700)

wn.tracer(0)

user_input = input(
    "Hello, would you like to play the easy or hard version of pressure pong? For the easy version please type in 2 "
    "otherwise, type in a 1: ")

if user_input == "1":

    speed = 1

    difficulty_level = 1  # I moved the difficulty level, as having it above was doing nothing

else:

    speed = 2

    difficulty_level = 2

# Score


score_1 = 0

score_2 = 0

# Paddle A (Triangle on left)


paddle_a = turtle.Turtle()

paddle_a.speed(0)

paddle_a.shape("triangle")

paddle_a.color("blue")

paddle_a.shapesize(stretch_wid=3, stretch_len=2)

paddle_a.penup()

paddle_a.goto(-350, 0)

# Paddle B (Triangle on right)


paddle_b = turtle.Turtle()

paddle_b.speed(0)

paddle_b.shape("triangle")

paddle_b.color("red")

paddle_b.shapesize(stretch_wid=3, stretch_len=2)

paddle_b.penup()

paddle_b.goto(350, 0)

# Ball


ball = turtle.Turtle()

ball.speed(0)

ball.shape("circle")

ball.color("black")

ball.penup()

ball.goto(0, 0)

ball.dx = 2

ball.dy = 2

# Pen


pen = turtle.Turtle()

pen.speed(0)

pen.shape("circle")

pen.color("black")

pen.penup()

pen.hideturtle()

pen.goto(0, 260)

pen.write("Player A: 0  Player B: 0", align="center", font=("Arial", 24, "normal"))


# Functions


def paddle_a_up():
    y = paddle_a.ycor()

    y += 20

    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()

    y -= 20

    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()

    y += 20

    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()

    y -= 20

    paddle_b.sety(y)


# Keyboard bindings for movement of paddles


wn.listen()

wn.onkeypress(paddle_a_up, "w")

wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")

wn.onkeypress(paddle_b_down, "Down")

# Main game loop

# Decided to use the count of loops, instead of actual seconds itself. 10,000 loops is roughly 12 seconds
seconds = 150000  # Sets timer, changed timer to 3 minutes (phase 4) as it felt more suitable than the previous time of 5 minutes (250 000 loops)

for k in range(seconds):  # Constant value to keep the loop going, the loop ends when it changes

    seconds -= 1

    wn.update()

    # Move the ball

    ball.setx(ball.xcor() + ball.dx * speed)

    ball.sety(ball.ycor() + ball.dy * speed)

    if difficulty_level <= 1:

        ball_speed = +1

    else:

        ball_speed = 0

        # Border checking

        # Top and bottom

    if ball.ycor() > 290:

        ball.sety(290)

        ball.dy *= -1

        os.system("afplay bounce.wav&")

    elif ball.ycor() < -290:

        ball.sety(-290)

        ball.dy *= -1

        os.system("afplay bounce.wav&")

        # Left and right

    if ball.xcor() > 350:

        score_1 += 1

        pen.clear()

        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center",
                  font=("Courier", 24, "normal"))

        ball.goto(0, 0)

        ball.dx *= -1

    elif ball.xcor() < -350:

        score_2 += 1

        pen.clear()

        pen.write("Player 1: {}  Player 2: {}".format(score_1, score_2), align="center",
                  font=("Courier", 24, "normal"))

        ball.goto(0, 0)

        ball.dx *= -1

        # Paddle and ball collisions

    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:

        ball.dx *= -1

        os.system("afplay bounce.wav&")

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:

        ball.dx *= -1

        os.system("afplay bounce.wav&")

    if seconds / 10000 == 10:
        print("10 seconds remaining")

    if seconds == 1:
        print("Time is up!") # Tells player that the time to complete the game has finished

    if seconds == 0:
        turtle.clearscreen() # Clears the graphic once the timer ends so that the player knows the time has finished and cannot continue progressing through once the allocated time is up

# Resources used: Christian Thompson via https://youtu.be/C6jJg9Zan7w
# Credits: Lucas Bird 
        
