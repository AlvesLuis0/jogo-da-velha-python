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
buttons[0][0] = [0, button(0,0)]
buttons[0][0][1].place(x=0,y=0)
buttons[0][1] = [0, button(0,1)]
buttons[0][1][1].place(x=50,y=0)
buttons[0][2] = [0, button(0,2)]
buttons[0][2][1].place(x=100,y=0)

buttons[1][0] = [0, button(1,0)]
buttons[1][0][1].place(x=0,y=50)
buttons[1][1] = [0, button(1,1)]
buttons[1][1][1].place(x=50,y=50)
buttons[1][2] = [0, button(1,2)]
buttons[1][2][1].place(x=100,y=50)

buttons[2][0] = [0, button(2,0)]
buttons[2][0][1].place(x=0,y=100)
buttons[2][1] = [0, button(2,1)]
buttons[2][1][1].place(x=50,y=100)
buttons[2][2] = [0, button(2,2)]
buttons[2][2][1].place(x=100,y=100)


# iniciando looping
root.mainloop()