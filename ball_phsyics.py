# Author: William Espegren
import turtle
import time
from tkinter import *
from tkinter import ttk
import tkinter

gui = tkinter.Tk()

gui.geometry("500x500")
gui.resizable(0, 0)
gui.title("Ball Physics")


def initalizeTurtle():
    # initialize the window
    window = turtle.Screen()
    # set the height and width of the window
    height = 500
    width = 500
    window.setup(height=height, width=width)
    window.tracer(0)

    # initialize the ball
    ball = turtle.Turtle()

    ball.hideturtle()

    ballPhysics(window, ball, height, width)


def ballPhysics(window, ball, height, width):

    # set the gravity, y velocity, x velocity, energy loss factor, friction, and speed of the simulation
    gravity = gravitySlider.get()
    yVelocity = yVelocitySlider.get()
    xVelocity = xVelocitySlider.get()
    energyLossFactor = energyLossFactorSlider.get()
    friction = frictionSlider.get()
    speed = speedSlider.get()
    airResistance = airResistanceSlider.get()
    ballSize = ballSizeSlider.get()

    # # if the user doesn't input anything, set the variables to their default values
    # if gravity == "":
    #     gravity = -9.82
    # else:
    #     gravity = float(gravity)
    # if yVelocity == "":
    #     yVelocity = 0
    # else:
    #     yVelocity = float(yVelocity)
    # if xVelocity == "":
    #     xVelocity = -1
    # else:
    #     xVelocity = float(xVelocity)
    # if energyLossFactor == "":
    #     energyLossFactor = 0.85
    # else:
    #     energyLossFactor = float(energyLossFactor)
    # if friction == "":
    #     friction = 0.9
    # else:
    #     friction = float(friction)
    # if speed == "":
    #     speed = 0.01
    # else:
    #     speed = float(speed)
    # if airResistance == "":
    #     airResistance = 0.9999
    # else:
    #     airResistance = float(airResistance)

    # display the current gravity on the screen
    gravityDisplay = turtle.Turtle()
    gravityDisplay.hideturtle()
    gravityDisplay.penup()
    gravityDisplay.sety(height/2.2)
    gravityDisplay.write("Gravity: " + str(gravity),
                         font=("Arial", 16, "normal"))

    # display the current energy loss factor on the screen
    energyLossFactorDisplay = turtle.Turtle()
    energyLossFactorDisplay.hideturtle()
    energyLossFactorDisplay.penup()
    energyLossFactorDisplay.sety(height/2.2 - 20)
    energyLossFactorDisplay.write(
        "Energy Loss Factor: " + str(energyLossFactor), font=("Arial", 16, "normal"))

    # display the current friction on the screen
    frictionDisplay = turtle.Turtle()
    frictionDisplay.hideturtle()
    frictionDisplay.penup()
    frictionDisplay.sety(height/2.2 - 40)
    frictionDisplay.write("Friction: " + str(friction),
                          font=("Arial", 16, "normal"))

    # display the current air resistance on the screen
    airResistanceDisplay = turtle.Turtle()
    airResistanceDisplay.hideturtle()
    airResistanceDisplay.penup()
    airResistanceDisplay.sety(height/2.2 - 60)
    airResistanceDisplay.write(
        "Air Resistance: " + str(airResistance), font=("Arial", 16, "normal"))

    # display the current speed on the screen
    speedDisplay = turtle.Turtle()
    speedDisplay.hideturtle()
    speedDisplay.penup()
    speedDisplay.sety(height/2.2 - 80)
    speedDisplay.write("Speed of Sim: " + str(speed),
                       font=("Arial", 16, "normal"))

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
        velocityDisplay.sety(height/2.2 - 100)
        velocityDisplay.write("Velocity: " + str(round(xVelocity, 3)) + ", " + str(round(yVelocity, 3)),
                              font=("Arial", 16, "normal"))  # round to 3 decimals to make it easier to read

        # move the ball
        ball.sety(ball.ycor()+yVelocity)
        ball.setx(ball.xcor()+xVelocity)
        yVelocity += gravity/100 * airResistance
        xVelocity *= airResistance

        # speed up or slow down the simulation
        time.sleep(speed)

        # check for collisions
        if ball.ycor() < -height/2.2:
            yVelocity = -yVelocity * energyLossFactor * airResistance
            xVelocity = xVelocity * friction * airResistance
            # The ball gets stuck sometime in the floor. This eliminates the problem.
            ball.sety(-height/2.19)
        if ball.ycor() > height/2.2:
            yVelocity = -yVelocity * energyLossFactor * airResistance
            xVelocity = xVelocity * friction * airResistance
            # The ball gets stuck sometime in the floor. This eliminates the problem.
            ball.sety(height/2.19)
        if ball.xcor() > width/2:
            xVelocity = -xVelocity * friction * airResistance
            # The ball gets stuck sometime in the wall. This eliminates the problem.
            ball.setx(width/2)
        if ball.xcor() < -width/2:
            xVelocity = -xVelocity*friction * airResistance
            # The ball gets stuck sometime in the wall. This eliminates the problem.
            ball.setx(-width/2)

        # clear the velocity display so it can be updated with the new velocity
        velocityDisplay.clear()

        try:
            # update the screen
            window.update()
        except:
            initalizeTurtle()

        ball.clear()
        ball.dot(ballSize, "red")


# gravity slider and label
gravitySlider = Scale(gui, from_=20, to=-20, resolution=0.01)
gravitySlider.set(-9.82)
gravitySlider.place(x=60, y=10)

gravitySliderLabel = Label(gui, text="Gravity", font=('Helvetica 13'))
gravitySliderLabel.place(x=10, y=50)

# xVelocity slider and label
xVelocitySlider = Scale(gui, from_=-100, to=100, orient=HORIZONTAL)
xVelocitySlider.place(x=205, y=30)

xVelocityLabel = Label(gui, text="X-Velocity", font=('Helvetica 13'))
xVelocityLabel.place(x=215, y=80)

# yVelocity slider and label
yVelocitySlider = Scale(gui, from_=100, to=-100, orient=VERTICAL)
yVelocitySlider.place(x=360, y=10)

yVelocityLabel = Label(gui, text="Y-Velocity", font=('Helvetica 13'))
yVelocityLabel.place(x=410, y=50)

# ball size slider and label
ballSizeSlider = Scale(gui, from_=1, to=100, orient=HORIZONTAL)
ballSizeSlider.set(10)
ballSizeSlider.place(x=170, y=210)

ballSizeSliderLabel = Label(gui, text="Ball Size", font=('Helvetica 13'))
ballSizeSliderLabel.place(x=10, y=230)

# energy loss factor slider and label
energyLossFactorSlider = Scale(
    gui, from_=0, to=1, resolution=0.01, orient=HORIZONTAL)
energyLossFactorSlider.set(0.9)
energyLossFactorSlider.place(x=170, y=270)

energyLossFactorSliderLabel = Label(
    gui, text="Energy Loss Factor", font=('Helvetica 13'))
energyLossFactorSliderLabel.place(x=10, y=290)

# friction slider and label
frictionSlider = Scale(gui, from_=0, to=1, resolution=0.01, orient=HORIZONTAL)
frictionSlider.set(0.9)
frictionSlider.place(x=170, y=330)

frictionSliderLabel = Label(gui, text="Friction", font=('Helvetica 13'))
frictionSliderLabel.place(x=10, y=350)

# air resistance slider and label
airResistanceSlider = Scale(
    gui, from_=0.9, to=1, resolution=0.0001, orient=HORIZONTAL)
airResistanceSlider.set(0.98)
airResistanceSlider.place(x=170, y=390)

airResistanceSliderLabel = Label(
    gui, text="Air Resistance", font=('Helvetica 13'))
airResistanceSliderLabel.place(x=10, y=410)

# speed slider and label
speedSlider = Scale(gui, from_=0, to=0.2, resolution=0.01, orient=HORIZONTAL)
speedSlider.set(0.01)
speedSlider.place(x=170, y=450)

speedSliderLabel = Label(gui, text="Speed", font=('Helvetica 13'))
speedSliderLabel.place(x=10, y=470)


ttk.Button(gui, text="Start simulation", command=initalizeTurtle).place(
    x=400, y=450)

gui.mainloop()
