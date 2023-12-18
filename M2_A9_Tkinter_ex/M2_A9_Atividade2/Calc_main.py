import tkinter as tk

def but_get_num():
    pass
def but_get_operacao():
    pass


#Configuração da Janela
root = tk.Tk()
root.title("Tk Calculator")


#Declaração das variáveis de interface
num1 = tk.DoubleVar()
oper = tk.StringVar()
oper_display = tk.StringVar(root,value="-")

lst_num = []
lst_oper = []

#Definindo os elementos:

lbl_calc_display = tk.Label(root,textvariable= oper_display, bg="white")

but1 = tk.Button(root, text= "1", command=but_get_num)
but2 = tk.Button(root, text= "2", command=but_get_num)
but3 = tk.Button(root, text= "3", command=but_get_num)
but4 = tk.Button(root, text= "4", command=but_get_num)
but5 = tk.Button(root, text= "5", command=but_get_num)
but6 = tk.Button(root, text= "6", command=but_get_num)
but7 = tk.Button(root, text= "7", command=but_get_num)
but8 = tk.Button(root, text= "8", command=but_get_num)
but9 = tk.Button(root, text= "9", command=but_get_num)
but0 = tk.Button(root, text= "0", command=but_get_num)

but_plus = tk.Button(root, text= "+", command=but_get_operacao)
but_subtract = tk.Button(root, text="-", command=but_get_operacao)
but_equal = tk.Button(root,text='-',command=but_get_operacao)

#Posicionando os elementos com grid

lbl_calc_display.grid(row=0,column=0, )


root.mainloop()
