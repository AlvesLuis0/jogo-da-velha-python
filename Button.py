#importando bibliotecas importantes
import tkinter as tk


class Button:
    def __init__(self, grid, x:int, y:int):
        self.x = x
        self.y = y
        self.value = 0
        self._ = tk.Button(
            grid.root,
            text=" ",
            padx=22,
            pady=14,
            command=lambda: self.pressed(grid)
        )

        self._.place(x=x*50, y=y*50)


    def pressed(self, grid):
        if (self.value) or (grid.win): return

        config = [
            {
                "text": "x",
                "color": "yellow2",
                "sizex": 21
            },
            {
                "text": "o",
                "color": "lightblue",
                "sizex": 20
            }
        ][grid.turn-1]

        self._.config(text=config["text"], bg=config["color"], padx=config["sizex"])
        self.value = grid.turn

        grid.turn = [2,1][grid.turn-1]

        grid.check()
    
    
    def green(self):
        self._.config(bg="green2")