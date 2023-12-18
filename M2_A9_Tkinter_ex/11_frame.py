import tkinter as tk

janela = tk.Tk()

agrupamento = tk.Frame(janela)

titulo = tk.Label(janela, text= "Seja bem vindo!")


texto_nome = tk.Label(agrupamento, text="Nome: ")
entrada_nome = tk.Entry(agrupamento)
botao = tk.Button(agrupamento,text="Clique aqui",width=20)

#Posicionando os elementos
titulo.pack()
agrupamento.pack()

#Posicionando os elementos no agrupamento
texto_nome.grid(row=0, column=0)
entrada_nome.grid(row=0,column=1)
botao.grid(row=1,column=0,columnspan=2)


janela.mainloop()