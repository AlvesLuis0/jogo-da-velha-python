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
        self.root.geometry("150x175")
        self.win = 0

        #iniciando variáveis importantes
        self._ = [[0,0,0],[0,0,0],[0,0,0]]
        self.turn = randint(1,2)
        self.label = tk.Label(
            self.root,
            text=f"Vez do {'X' if self.turn==1 else 'O'}"
        )

        #renderizando botões
        for y in range(3):
            for x in range(3):
                self._[y][x] = Button(self, x, y)
        
        self.label.place(x=50, y=152.5)

    
    def run(self):
        #rodando programa
        self.root.mainloop()

    
    def check(self):
        #checando se alguém ganhou
        grid = self._
        self.label.config(text=f"Vez do {'X' if self.turn==1 else 'O'}")

        for i in range(3):
            #na horizontal
            aux = []
            buttons = []

            for j in range(3):
                aux.append(grid[i][j].value)
                buttons.append(self._[i][j])
            
            if aux in [[1,1,1],[2,2,2]]:
                self.win = [[1,1,1],[2,2,2]].index(aux) + 1
                for b in buttons: b.green()
                self.label.config(text=f"O jogador {'X' if self.win==1 else 'O'} ganhou!")
                self.label.place(x=20)

        for j in range(3):
            #na vertical
            aux = []
            buttons = []

            for i in range(3):
                aux.append(grid[i][j].value)
                buttons.append(self._[i][j])
            
            if aux in [[1,1,1],[2,2,2]]:
                self.win = [[1,1,1],[2,2,2]].index(aux) + 1
                for b in buttons: b.green()
                self.label.config(text=f"O jogador {'X' if self.win==1 else 'O'} ganhou!")
                self.label.place(x=20)
        
        aux = []
        buttons = []
        
        for i in range(3):
            #na diagonal secondária            
            aux.append(grid[i][2-i].value)
            buttons.append(self._[i][2-i])
            
            if aux in [[1,1,1],[2,2,2]]:
                self.win = [[1,1,1],[2,2,2]].index(aux) + 1
                for b in buttons: b.green()
                self.label.config(text=f"O jogador {'X' if self.win==1 else 'O'} ganhou!")
                self.label.place(x=20)
        
        aux = []
        buttons = []
        
        for i in range(3):
            #na diagonal secondária            
            aux.append(grid[i][i].value)
            buttons.append(self._[i][i])
            
            if aux in [[1,1,1],[2,2,2]]:
                self.win = [[1,1,1],[2,2,2]].index(aux) + 1
                for b in buttons: b.green()
                self.label.config(text=f"O jogador {'X' if self.win==1 else 'O'} ganhou!")
                self.label.place(x=20)
        
        #empate?
        tie = 1

        for i in range(3):
            for j in range(3):
                if grid[i][j].value == 0:
                    tie = 0
                    break
        
        if tie: self.label.config(text="Empate!")