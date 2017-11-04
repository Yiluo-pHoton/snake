from Tkinter import *

class Display:
    coordinate = [100, 200]
    def __init__(self):
        self.frame = Tk()
        self.canvas = Canvas(self.frame, width=800, height=600, bg="#545454")
        self.canvas.pack()

    def run(self):
        self.canvas.delete(ALL)
        self.canvas.create_oval(
            self.coordinate[0],
            self.coordinate[1],
            self.coordinate[0] + 40,
            self.coordinate[1] + 40,
            fill = "#80FF00"
        )
        self.coordinate = [self.coordinate[0] + 1, self.coordinate[1]]
        self.frame.after(300, self.run)

game = Display()
game.run()
game.frame.mainloop()
