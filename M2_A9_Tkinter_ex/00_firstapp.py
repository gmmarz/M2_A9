# from tkinter import * # jeito que importa todas as funções do tkinter.
import tkinter as tk

def button_click():
    label.config(text="Botão clicado")


janela = tk.Tk()

#label(rotulo)
label = tk.Label(janela, text="Olá, mundo!!", font=("Arial",12))
label.pack()


button = tk.Button(janela,text="Clique em mim!", command=button_click)
button.pack()

janela.mainloop()