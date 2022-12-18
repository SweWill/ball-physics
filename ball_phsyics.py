# Author: William Espegren
import turtle
import time

# initialize the window
window = turtle.Screen()

# initialize the ball
ball = turtle.Turtle()

# set the height and width of the window
height = 500
width = 500
window.setup(height=height, width=width)
window.tracer(0)

# set the gravity, y velocity, x velocity, energy loss factor, friction, and speed of the simulation
gravity = -9.82
yVelocity = 0
xVelocity = -1
energyLossFactor = 0.85
friction = 0.9
speed = 0.01

# display the current gravity on the screen
gravityDisplay = turtle.Turtle()
gravityDisplay.hideturtle()
gravityDisplay.penup()
gravityDisplay.sety(height/2.2)
gravityDisplay.write("Gravity: " + str(gravity), font=("Arial", 16, "normal"))

# display the current energy loss factor on the screen
energyLossFactorDisplay = turtle.Turtle()
energyLossFactorDisplay.hideturtle()
energyLossFactorDisplay.penup()
energyLossFactorDisplay.sety(height/2.2 - 20)
energyLossFactorDisplay.write("Energy Loss Factor: " + str(energyLossFactor), font=("Arial", 16, "normal"))

# display the current friction on the screen
frictionDisplay = turtle.Turtle()
frictionDisplay.hideturtle()
frictionDisplay.penup()
frictionDisplay.sety(height/2.2 - 40)
frictionDisplay.write("Friction: " + str(friction), font=("Arial", 16, "normal"))

# display the current speed on the screen
speedDisplay = turtle.Turtle()
speedDisplay.hideturtle()
speedDisplay.penup()
speedDisplay.sety(height/2.2 - 60)
speedDisplay.write("Speed of Sim: " + str(speed), font=("Arial", 16, "normal"))

# make the ball
ball.penup()
ball.shape('circle')
ball.color("red")

# main loop
while True:

    # show the current x and y velocity with 3 decimals on the screen with each update of the screen
    velocityDisplay = turtle.Turtle()
    velocityDisplay.hideturtle()
    velocityDisplay.penup()
    velocityDisplay.sety(height/2.2 - 80)
    velocityDisplay.write("Velocity: " + str(round(xVelocity,3)) + ", " + str(round(yVelocity,3)), font=("Arial", 16, "normal")) # round to 3 decimals to make it easier to read

    # move the ball
    ball.sety(ball.ycor()+yVelocity)
    ball.setx(ball.xcor()+xVelocity)
    yVelocity += gravity/100

    # speed up or slow down the simulation
    time.sleep(speed)

    # check for collisions
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

    velocityDisplay.clear() # clear the velocity display so it can be updated with the new velocity

    # update the screen
    window.update()