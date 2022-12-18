# Author: William Espegren
import turtle
import time
from tkinter import *
from tkinter import ttk
import tkinter

gui = tkinter.Tk()

gui.geometry("500x500")
gui.title("Ball Physics")


def ball_physics():
    # initialize the window
    window = turtle.Screen()

    # initialize the ball
    ball = turtle.Turtle()


    # set the height and width of the window
    height = 500
    width = 500
    window.setup(height=height, width=width)
    window.tracer(0)

    # class Ball(turtle.Turtle):
    # set the gravity, y velocity, x velocity, energy loss factor, friction, and speed of the simulation
    gravity = entry.get()
    yVelocity = input("yVelocity (0): ")
    xVelocity = input("xVelocity (-1): ")
    energyLossFactor = input("energyLossFactor (0.85): ")
    friction = input("Friction (0.9): ")
    speed = input("Speed (0.01): ")
    airResistance = input("Air Resistance (0.9999): ")

    # if the user doesn't input anything, set the variables to their default values
    if gravity == "":
        gravity = -9.82
    else:
        gravity = float(gravity)
    if yVelocity == "":
        yVelocity = 0
    else:
        yVelocity = float(yVelocity)
    if xVelocity == "":
        xVelocity = -1
    else:
        xVelocity = float(xVelocity)
    if energyLossFactor == "":
        energyLossFactor = 0.85
    else:
        energyLossFactor = float(energyLossFactor)
    if friction == "":
        friction = 0.9
    else:
        friction = float(friction)
    if speed == "":
        speed = 0.01
    else:
        speed = float(speed)
    if airResistance == "":
        airResistance = 0.9999
    else:
        airResistance = float(airResistance)

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

        try:

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

            # update the screen
            window.update()

        except:
            # if the user closes the window, the program will close
            turtle.bye()
            break


# Create an Entry Widget
entry = Entry(gui, width=42)
entry.place(relx=.5, rely=.5, anchor=CENTER)

# Inititalize a Label widget
label = Label(gui, text="", font=('Helvetica 13'))
label.pack()

# Create a Button to get the input data
ttk.Button(gui, text="Click to Show", command=ball_physics).place(
    relx=.7, rely=.5, anchor=CENTER)

gui.mainloop()
