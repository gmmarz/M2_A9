from tkinter import *

def converter_para_celcius():
    valor_atual = float(var_entrada.get())
    valor_em_celcius = (valor_atual - 32)/1.8
    print(valor_em_celcius)
def conver




janela = Tk()

var_entrada = StringVar()

titulo = Label(janela,text="Temperatura")

entrada = Entry(janela,textvariable=var_entrada)

botao_celcius = Button(janela,text="P/ Celcius", command= None)
botao_fahrenheit = Button(janela,text="P/ Fahrenheit",command=None)

titulo.grid(row=0,column=0,columnspan=2)
entrada.grid(row=1,column=0,columnspan=2)
botao_celcius.grid(row=2,column=0)
botao_fahrenheit.grid(row=2,column=1)



janela.mainloop()

#Configurando os elementos: