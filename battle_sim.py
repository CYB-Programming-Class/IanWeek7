from ninja_turtle import NinjaTurtle
import turtle
import random

Colors = ["AliceBlue", "AntiqueWhite", "aquamarine", "azure", "beige", "bisque", "BlanchedAlmond", "blue", "BlueViolet",
          "brown", "burlywood", "CadetBlue", "chartreuse", "chocolate", "coral", "CornflowerBlue", "cornsilk", "cyan"]

# this is the main method, the central control system
# where we'll call all our other methods


def main():
    # create screen
    wn = turtle.Screen()
    wn.setup(500, 500, 0, 0)
    wn.bgcolor("black")

    # create turtles
    bob = NinjaTurtle(random.choice(Colors), random.randint(1, 5))
    bill = NinjaTurtle(random.choice(Colors), random.randint(1, 5))
    setup(bob, bill)
    attack(bob, bill)

    wn.exitonclick()


def setup(t1, t2):
    t1.penup()
    t2.penup()
    # move to opposite sides of canvas
    t1.setx(-200)
    t2.setx(200)
    # turn towards center
    t2.setheading(180)


def attack(t1, t2):
    # have turtles go forward until they meet
    while t1.distance(t2) > 10:
        t1.forward(1)
        t2.forward(1)
        # note: the turtles are running on the same thread so you can't
        # have them go at the same time, so we create the illusion by having
        # each of them take turns taking small steps
    if t1.mad_skills >= t2.mad_skills:
        t2.loss()
        t1.victory_dance()
    else:
        t1.loss()
        t2.victory_dance()


main()
# ^^ here we actually call our main method
# so something actually happens
