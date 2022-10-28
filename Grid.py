#importando bibliotecas importantes
from random import randint
from Button import Button
import tkinter as tk


class Grid:
    def __init__(self):
        #configurando tela
        self.root = tk.Tk()
        self.root.title("Jogo da Velha")
        self.root.resizable(False, False)
        self.root.geometry("150x150")
        self.win = 0

        #iniciando variáveis importantes
        self._ = [[0,0,0],[0,0,0],[0,0,0]]
        self.turn = randint(1,2)

        #renderizando botões
        for y in range(3):
            for x in range(3):
                self._[y][x] = Button(self, x, y)

    
    def run(self):
        #rodando programa
        self.root.mainloop()

    
    def check(self):
        #checando se alguém ganhou
        grid = self._

        for i in range(3):
            #na horizontal
            aux = []
            buttons = []

            for j in range(3):
                aux.append(grid[i][j].value)
                buttons.append(self._[i][j])
            
            if (aux == [1,1,1]) or (aux == [2,2,2]):
                self.win = 1
                for b in buttons: b.green()

        for j in range(3):
            #na vertical
            aux = []
            buttons = []

            for i in range(3):
                aux.append(grid[i][j].value)
                buttons.append(self._[i][j])
            
            if (aux == [1,1,1]) or (aux == [2,2,2]):
                self.win = 1
                for b in buttons: b.green()
        
        aux = []
        buttons = []
        
        for i in range(3):
            #na diagonal secondária            
            aux.append(grid[i][2-i].value)
            buttons.append(self._[i][2-i])
            
            if (aux == [1,1,1]) or (aux == [2,2,2]):
                self.win = 1
                for b in buttons: b.green()
        
        aux = []
        buttons = []
        
        for i in range(3):
            #na diagonal secondária            
            aux.append(grid[i][i].value)
            buttons.append(self._[i][i])
            
            if (aux == [1,1,1]) or (aux == [2,2,2]):
                self.win = 1
                for b in buttons: b.green()