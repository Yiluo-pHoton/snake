from Tkinter import *
import operator
import copy
import random

class Snake:
    '''
    This is the Snake object for player to control
    '''
    class Directions:
        UP = (0, 1)
        DOWN = (0, -1)
        LEFT = (-1, 0)
        RIGHT = (1, 0)

    class GameStatus:
        START = 0
        ONGOING = 1
        GAME_OVER = 2

    self.body = [(0, 0), (1, 0), (2, 0)]

    def __init__(self):
        self.tail = self.body[0]
        self.direction = Directions.RIGHT

    def step(self):
        self.head = self.body[-1]
        self.body.append(tuple(map(operator.add, self.head, self.direction)))

    def set_direction(self, direction):
        if (directions != self.direction and
            directions != tuple(map(operator.mul(self.directions, (-1, -1)))):
            self.direction = direction

    def is_eating(self):
        "stub"

    def grow(self):
        self.body.insert(0, copy.deepcopy(self.tail))

    def update(self):
        self.step()

    def render(self, canvas):
        assert isInstance(canvas, Canvas)
        for seg in self.body:
            canvas.create_oval(seg[0] * 20, seg[1] * 20,
                               seg[0] * 20 + 20,
                               seg[1] * 20 + 20, fill = "#33FFAA")

    def is_game_over(self):
        "stub"


class Food:
    '''
    This is a class for randomly generated food in the game
    '''
    def __init__():
        self.x = random.randint(0, 40)
        self.y = random.randint(0, 30)

    def render():
        canvas.create_oval(self.x * 20, self.y * 20,
                           self.x * 20 + 20,
                           self.y * 20 + 20, fill = "#ee00ff")
    def is_eaten():
        "stub"

    def generate_food():
        self.x = random.randint(0, 40)
        self.y = random.randint(0, 30)


class SnakeGame:
    '''
    This is the game class that runs the snake game
    '''
    coordinate = [100, 200]
    def __init__(self):
        self.frame = Tk()
        self.canvas = Canvas(self.frame, width=800, height=600, bg="#545454")
        self.canvas.pack()
        self.my_sake = Snake()
        self.food = Food()
        self.frame.bind("<KeyPress>", self.key_pressed)

    # Set directions for the snake
    def key_pressed(self, event):
        if event.keysym == "Up" or event.keysym == "w":
                self.my_sake.set_direction(Snake.Directions.UP)
        elif event.keysym == "Down" or event.keysym == "s":
                self.my_sake.set_direction(Snake.Directions.DOWN)
        elif event.keysym == "Left" or event.keysym == "a":
                self.my_sake.set_direction(Snake.Directions.LEFT)
        elif event.keysym == "Right" or event.keysym == "d":
                self.my_sake.set_direction(Snake.Directions.RIGHT)

    def run(self):
        self.canvas.delete(ALL)
        self.update()
        self.render(self.canvas)
        self.frame.after(20, self.run())

    def update(self):
        self.my_sake.update()

    def render(self, canvas):
        self.my_snake.render(canvas)
        self.food.render(canvas)

if __name__ == "__main__":
    my_game = SnakeGame()
    my_game.run()
    my_game.frame.mainloop()
