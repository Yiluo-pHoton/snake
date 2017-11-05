from Tkinter import *
import operator
import copy
import random
import numpy as np

class Directions:
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    DEFAULT = RIGHT


class GameStatus:
    START = 0
    ONGOING = 1
    GAME_OVER = 2
    DEFAULT = START


class Handler:
    def __init__(self, game):
        self.game = game

    def get_game(self):
        return self.game

    def get_snake(self):
        return self.game.my_snake

    def get_food(self):
        return self.game.food

    def get_player(self):
        return "stub"


class Snake:
    '''
    This is the Snake object for player to control
    '''
    def __init__(self, handler):
        self.body = [(0, 0), (1, 0), (2, 0)]
        self.tail = self.body[0]
        self.direction = Directions.DEFAULT
        self.handler = handler

    def step(self):
        self.head = self.body[-1]
        self.body.append(tuple(np.array(self.head) + np.array(self.direction)))
        del self.body[0]
        self.tail = self.body[0]
        print(self.head)

    def set_direction(self, direction):
        if (direction != self.direction and
            direction != tuple(np.array(self.direction) * np.array((-1, -1)))):
            self.direction = direction

    def grow(self):
        self.body.insert(0, copy.deepcopy(self.tail))

    def update(self):
        self.step()

        self.food = self.handler.get_food()
        self.food_coor = (self.food.x, self.food.y)
        if self.head == self.food_coor:
            self.grow()

    def render(self, canvas):
        assert isinstance(canvas, Canvas)
        for seg in self.body:
            canvas.create_oval(seg[0]*20, seg[1]*20,
                               seg[0]*20+20, seg[1]*20+20,
                               fill="#14b4ff", width=0)

    def is_game_over(self):
        return "stub"


class Food:
    '''
    This is a class for randomly generated food in the game
    '''
    def __init__(self, handler):
        self.x = random.randint(0, 40)
        self.y = random.randint(0, 30)
        self.coor = (self.x, self.y)
        self.handler = handler

    def update(self):
        self.snake = self.handler.get_snake()
        self.snake_head = self.snake.head

        if self.snake.head == self.coor:
            self.generate_food()

    def render(self, canvas):
        assert isinstance(canvas, Canvas)
        canvas.create_oval(self.x*20, self.y*20,
                           self.x*20+20,self.y*20+20,
                           fill="#8e2af9", outline="#5400af", width=3)

    def generate_food(self):
        self.x = random.randint(0, 39)
        self.y = random.randint(0, 29)
        self.coor = (self.x, self.y)


class SnakeGame:
    '''
    This is the game class that runs the snake game
    '''
    def __init__(self):
        self.frame = Tk()
        self.canvas = Canvas(self.frame, width=800, height=600, bg="#000")
        self.canvas.pack()
        self.handler = Handler(self)
        self.my_snake = Snake(self.handler)
        self.food = Food(self.handler)
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
        self.update()
        self.render()
        self.frame.after(100, self.run)

    def update(self):
        self.my_snake.update()
        self.food.update()

    def render(self):
        self.my_snake.render(self.canvas)
        self.food.render(self.canvas)

if __name__ == "__main__":
    my_game = SnakeGame()
    my_game.run()
    my_game.frame.mainloop()
