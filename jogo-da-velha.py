# importando o "tkinter", que é o responsável pela interface gráfica, e "math" pelos cálculos
from tkinter import *
from random import randint


# configurando janela
root = Tk()
root.title("Jogo da Velha")
root.resizable(False, False)
root.geometry("150x150")

# iniciando variáveis importantes
turn = randint(1,3)
buttons = [[0,0,0],[0,0,0],[0,0,0]]
symbol = [
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
]


# função de criar botões mais facilmente
def button(i, j):
    return Button(
        root,
        text=" ",
        padx=22,
        pady=14,
        command=lambda: press(i, j)
    )


#criando a função de pressionar o botão
def press(i, j):
    if buttons[i][j][0]: return
    global symbol, turn
    config = symbol[turn-1]

    buttons[i][j][1].config(text=config["text"], bg=config["color"], padx=config["sizex"])
    buttons[i][j][0] = turn

    if turn == 1: turn = 2
    else: turn = 1


#renderizando botões
for i in range(3):
    for j in range(3):
        buttons[i][j] = [0, button(eval("i"),eval("j"))]
        buttons[i][j][1].place(x=i*50,y=j*50)


# iniciando looping
root.mainloop()