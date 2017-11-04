from Tkinter import *

class Snake:
    '''
    This is the Snake object for player to control
    '''
    class Directions:
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3

    class GameStatus:
        START = 0
        ONGOING = 1
        GAME_OVER = 2

    def __init__(self):

    def step(self):
        "stub"

    def turn(self, direction):
        "stub"

    def is_eating(self):
        "stub"

    def grow():
        "stub"

    def is_game_over(self):
        "stub"


class Food:
    '''
    This is a class for randomly generated food in the game
    '''
    def __init__():
        "stub"


class Display:
    coordinate = [100, 200]
    def __init__(self):
        self.frame = Tk()
        self.canvas = Canvas(self.frame, width=800, height=600, bg="#545454")
        self.canvas.pack()

    def run(self):
        self.canvas.delete(ALL)
        self.coordinate = [self.coordinate[0] + 2, self.coordinate[1]]
        self.frame.after(10, self.run)

if __name__ == "__main__":
    game = Display()
    game.run()
    game.frame.mainloop()
