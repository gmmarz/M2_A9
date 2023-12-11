# from tkinter import * # jeito que importa todas as funções do tkinter.
import tkinter as tk

def imprimir_ola(mensagem):
    print(mensagem)
    meu_texto.set("variavel alterada") #Exemplo para alterar o valor pelo botão.

janela = tk.Tk()

#Criando uma variável que é monitorada pelo tkinter.
meu_texto = tk.StringVar(janela,"Olá")
# meu_texto.set("Outra coisa") #Maneira para se alterar o valor de uma variavel do tkinter.
#Jeito para pegar o valor da variável
valor = meu_texto.get()
print(valor)

#label(rotulo)
texto = tk.Label(janela, text="Olá, mundo!!", font=("Arial",12))
texto2 = tk.Label(janela, textvariable=meu_texto, font=("Arial",12))

#Quando a função do botão precisa receber um argumento, utilizamos a função lambda para no comando do botão. 
#O comando do botão é responsável por executar a função por isso caso a gente passe o argumento diretamente ele executa diratamente sem esperar o botão
botao = tk.Button(janela,text="Clique aqui!",command= lambda:imprimir_ola("Ola"))

entrada = tk.Entry(janela,textvariable=meu_texto)

#funcao pack é uma função de posicionamento que empilha os elementos na janela.
texto.pack()
texto2.pack()
botao.pack()
entrada.pack()


janela.mainloop()