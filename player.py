from turtle import Turtle

START = (0, -260)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.goto(START)
        self.setheading(90)

    def go_up(self):
        self.forward(10)

    def go_down(self):
        self.backward(10)

    def next_stage(self):
        self.goto(START)


