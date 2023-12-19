import tkinter as tk

def but_display(but_valor):
    valor_atual = oper_display.get()
    oper_display.set(valor_atual + str(but_valor))
def but_clear_display():
    oper_display.set("")
def but_calcular_operacao():
    resultado = eval(oper_display.get())
    oper_display.set(resultado)

#Configuração da Janela
root = tk.Tk()
root.title("Tk Calculator")


#Declaração das variáveis de interface
oper_display = tk.StringVar(root,value="")

lst_num = []
lst_oper = []

#Definindo os elementos:

lbl_calc_display = tk.Label(root,textvariable= oper_display, bg="#FFFFFF", width=30)

num_Frame = tk.Frame(root)

but1 = tk.Button(num_Frame, text= "1", command=lambda: but_display("1"),width=10)
but2 = tk.Button(num_Frame, text= "2", command=lambda: but_display("2"),width=10)
but3 = tk.Button(num_Frame, text= "3", command=lambda: but_display("3"),width=10)
but4 = tk.Button(num_Frame, text= "4", command=lambda: but_display("4"),width=10)
but5 = tk.Button(num_Frame, text= "10", command=lambda: but_display("5"),width=10)
but6 = tk.Button(num_Frame, text= "6", command=lambda: but_display("6"),width=10)
but7 = tk.Button(num_Frame, text= "7", command=lambda: but_display("7"),width=10)
but8 = tk.Button(num_Frame, text= "8", command=lambda: but_display("8"),width=10)
but9 = tk.Button(num_Frame, text= "9", command=lambda: but_display("9"),width=10)
but0 = tk.Button(num_Frame, text= "0", command=lambda: but_display("0"),width=10)

# but_open_parenteses = tk.Button(num_Frame,text= "(", command=lambda:but_display("("), width = 10)

# but_close_parenteses = tk.Button(num_Frame,text= ")", command=lambda:but_display(")"), width = 10)


but_plus = tk.Button(num_Frame, text= "+", command=lambda: but_display("+"),width=10)
but_subtract = tk.Button(num_Frame, text="-", command=lambda: but_display("-"),width=10)
but_mult = tk.Button(num_Frame,text="*",command=lambda: but_display("*"),width=10)
but_div = tk.Button(num_Frame,text="/",command=lambda: but_display("/"),width=10)
but_clear = tk.Button(num_Frame,text="C",command=but_clear_display,width=10)

but_equal = tk.Button(num_Frame,text="Calcular",command=but_calcular_operacao,width=30)

#Posicionando os elementos com grid

lbl_calc_display.pack()

num_Frame.pack(side=tk.LEFT)

but_clear.grid(row=0,column=2)

but7.grid(row=0,column=0)
but8.grid(row=0,column=1)
but9.grid(row=0,column=2)
but_clear.grid(row=0,column=3)


but4.grid(row=1,column=0)
but5.grid(row=1,column=1)
but6.grid(row=1,column=2)
but_div.grid(row=1,column=3)


but1.grid(row=2,column=0)
but2.grid(row=2,column=1)
but3.grid(row=2,column=2)
but_mult.grid(row=2,column=3)

but_plus.grid(row=3,column=0)
but0.grid(row=3,column=1)
but_subtract.grid(row=3,column=2)
but_equal.grid(row=4,column=1,columnspan=2)



root.mainloop()
