from turtle import Turtle
import time
import random
Colors = ["AliceBlue", "AntiqueWhite", "aquamarine", "azure", "beige", "bisque", "BlanchedAlmond", "blue", "BlueViolet",
          "brown", "burlywood", "CadetBlue", "chartreuse", "chocolate", "coral", "CornflowerBlue", "cornsilk", "cyan"]


class NinjaTurtle(Turtle):
    # inherits from ^^ Turtle

    # This is the constructor. It's what's run whenever
    # you create a new ninja turtle
    def __init__(self, color, skill_level):
        # call parent class constructor
        # this sets up all the basic turtle stuff
        Turtle.__init__(self)

        # make standard turtle more ninja-like
        self.shape("turtle")
        self.speed("fastest")

        # set instance variables
        # (stuff that's unique to each ninja turtle)
        self.color(color)
        self.mad_skills = skill_level

    def loss(self):
        self.hideturtle()
        time.sleep(.1)
        self.showturtle()
        for _ in range(5):
            self.hideturtle()
            time.sleep(.3)
            self.right(random.randint(-180, 180))
            self.showturtle()
            time.sleep(.3)

    def victory_dance(self):
        time.sleep(1)
        self.setheading(90)
        self.forward(115)
        self.right(90)
        self.pendown()
        for i in range(18):
            for x in range(i):
                self.right(x / 2)
                self.pensize(x)
                self.forward(x)
            self.pencolor(random.choice(Colors))
        self.right(90)
        self.pensize(10)
        self.forward(220)
        self.hideturtle()
