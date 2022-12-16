from turtle import Screen, Turtle
import turtle
import time

ball = turtle.Turtle()

height = 500
width = 500
screen = Screen()
screen.setup(height=height, width=width)


gravity = -9.82
velocity = 0
energyLossFactor = 0.9

ball.penup()
ball.shape('circle')
ball.color("red")

while True:
    ball.sety(ball.ycor()+velocity)
    velocity += gravity
    time.sleep(0.001)
    if ball.ycor() < -height/2:
        velocity = -velocity