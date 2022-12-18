import turtle
import time

window = turtle.Screen()

ball = turtle.Turtle()

height = 500
width = 500
window.setup(height=height, width=width)
window.tracer(0)

gravity = -9.82
yVelocity = 0
xVelocity = -1
energyLossFactor = 0.85
friction = 0.9
speed = 0.01

ball.penup()
ball.shape('circle')
ball.color("red")

while True:
    ball.sety(ball.ycor()+yVelocity)
    ball.setx(ball.xcor()+xVelocity)
    yVelocity += gravity/100

    time.sleep(speed)
    if ball.ycor() < -height/2.2:
        yVelocity = -yVelocity * energyLossFactor
        xVelocity = xVelocity * friction
        ball.sety(-height/2.19) # The ball gets stuck sometime in the floor. This eliminates the problem.
    if ball.xcor() > width/2: 
        xVelocity = -xVelocity * friction
        ball.setx(width/2) # The ball gets stuck sometime in the wall. This eliminates the problem.
    if ball.xcor() < -width/2:
        xVelocity = -xVelocity*friction
        ball.setx(-width/2) # The ball gets stuck sometime in the wall. This eliminates the problem.

    window.update()
s