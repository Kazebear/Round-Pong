import turtle
import winsound
import keyboard
import sys

''' Credits to Christian Thompson for the Pong tutorial!

I have adjusted a few lines of code in order to make:
     -The turtle objects round;
     -Fixed the Ball overlapping over the Score;
     -Fixed the Paddles going out of bounds;
     -New Chime added when scoring a point;
     -sys.exit(0) on keyboard press to gracefully exit the game. '''




window = turtle.Screen()
window.title("Round Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score variables
score_1 = 0
score_2 = 0



# Setting up Paddle_1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("circle")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.color("white")
paddle_1.penup()
paddle_1.goto(-350, 0)

# Setting up Paddle_2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("circle")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.color("white")
paddle_2.penup()
paddle_2.goto(350, 0)

# Printing the score, Setting up Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player One: 0 | 0 :Player Two", align="center", font=("Courier", 24, "normal"))

# Setting up the Ball and its speed
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Paddle movement functions
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

# Key bind for the Paddle movement
window.listen()
window.onkeypress(paddle_1_up, "w")
window.onkeypress(paddle_1_down, "s")
window.onkeypress(paddle_2_up, "Up")
window.onkeypress(paddle_2_down, "Down")

# Game infinite loop
while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


# Border restrictions for Paddles and Ball
    # Lowered the ycor to stop the ball from overlapping over the score
    if ball.ycor() > 260:
        ball.sety(260)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        winsound.PlaySound("bing.wav", winsound.SND_ASYNC)
        pen.write(f"Player One: {score_1} | {score_2} :Player Two", align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        winsound.PlaySound("bing.wav", winsound.SND_ASYNC)
        pen.write(f"Player One: {score_1} | {score_2} :Player Two", align="center", font=("Courier", 24, "normal"))

# Fix for the Paddles going out of the window bounds
    if paddle_1.ycor() > 269:
        paddle_1.sety(269)

    if paddle_1.ycor() < -269:
        paddle_1.sety(-269)

    if paddle_2.ycor() > 269:
        paddle_2.sety(269)

    if paddle_2.ycor() < -269:
        paddle_2.sety(-269)


# Paddle to Ball Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


# Keyboard bind to gracefully exit the game at any time
    if keyboard.is_pressed("Esc"):
        sys.exit(0)

# Printing out the Winner of the Pong round and clearing out the turtle objects
    if score_1 == 5 or score_2 == 5:
        ball.reset()
        paddle_1.reset()
        paddle_2.reset()
        pen.clear()
        if score_1 > score_2:
            pen.write("Player One Won! Press ESC to exit.", align="center", font=("Courier", 24, "normal"))
        elif score_1 < score_2:
            pen.write("Player Two Won! Press ESC to exit.", align="center", font=("Courier", 24, "normal"))