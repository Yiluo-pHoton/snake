from Tkinter import *
import operator
import copy
import random
import numpy as np

class Directions:
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


class GameStatus:
    START = 0
    ONGOING = 1
    GAME_OVER = 2

class Snake:
    '''
    This is the Snake object for player to control
    '''
    def __init__(self):
        self.body = [(0, 0), (1, 0), (2, 0)]
        self.tail = self.body[0]
        self.direction = Directions.RIGHT

    def step(self):
        self.head = self.body[-1]
        self.body.append(np.array(self.head) + np.array(self.direction))
        del self.body[0]
        self.tail = self.body[0]

    def set_direction(self, direction):
        if (direction != self.direction and
            direction != tuple(np.array(self.direction) * np.array((-1, -1)))):
            self.direction = direction

    def is_eating(self):
        return "stub"

    def grow(self):
        self.body.insert(0, copy.deepcopy(self.tail))

    def update(self):
        self.step()

    def render(self, canvas):
        assert isinstance(canvas, Canvas)
        for seg in self.body:
            canvas.create_oval(seg[0] * 20, seg[1] * 20,
                               seg[0] * 20 + 20,
                               seg[1] * 20 + 20, fill = "#33FFAA")

    def is_game_over(self):
        return "stub"


class Food:
    '''
    This is a class for randomly generated food in the game
    '''
    def __init__(self):
        self.x = random.randint(0, 40)
        self.y = random.randint(0, 30)

    def render(self, canvas):
        assert isinstance(canvas, Canvas)
        canvas.create_oval(self.x * 20, self.y * 20,
                           self.x * 20 + 20,
                           self.y * 20 + 20, fill = "#ee00ff")

    def generate_food(self):
        self.x = random.randint(0, 40)
        self.y = random.randint(0, 30)


class SnakeGame:
    '''
    This is the game class that runs the snake game
    '''
    def __init__(self):
        self.frame = Tk()
        self.canvas = Canvas(self.frame, width=800, height=600, bg="#545454")
        self.canvas.pack()
        self.my_snake = Snake()
        self.food = Food()
        self.frame.bind("<KeyPress>", self.print_key_info)

    # Set directions for the snake
    def print_key_info(self, event):
        if event.keysym == "Up" or event.keysym == "w":
                self.my_snake.set_direction(Directions.UP)
        elif event.keysym == "Down" or event.keysym == "s":
                self.my_snake.set_direction(Directions.DOWN)
        elif event.keysym == "Left" or event.keysym == "a":
                self.my_snake.set_direction(Directions.LEFT)
        elif event.keysym == "Right" or event.keysym == "d":
                self.my_snake.set_direction(Directions.RIGHT)

    def run(self):
        self.canvas.delete(ALL)
        self.render()
        self.frame.after(20, self.run)

    def update(self):
        self.my_snake.update()

    def render(self):
        self.my_snake.render(self.canvas)
        self.food.render(self.canvas)

if __name__ == "__main__":
    my_game = SnakeGame()
    my_game.run()
    my_game.frame.mainloop()
