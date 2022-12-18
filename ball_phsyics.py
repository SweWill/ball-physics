from turtle import Screen, Turtle
import turtle
import time

window = turtle.Screen()

ball = turtle.Turtle()

height = 500
width = 500
window.setup(height=height, width=width)
window.tracer(0) # Results in smother animation but makes only half of the ball to render. The boost in performance compensates for the loss of render imo.

gravity = -9.82
velocity = 0
energyLossFactor = 0.9

ball.penup()
ball.shape('circle')
ball.color("red")

while True:
    ball.sety(ball.ycor()+velocity)
    velocity += gravity/100
    time.sleep(0.001)
    if ball.ycor() < -height/2:
        velocity = -velocity
    window.update()