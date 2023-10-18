from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.setpos(-280, 220)
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'Stage: {self.score}', False, 'left', ('Arial', 16, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.color('gold')
        self.write("GAME OVER", False, 'center', ('Courier', 25, 'bold'))