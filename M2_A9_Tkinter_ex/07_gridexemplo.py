import tkinter as tk

#Exemplo de grid
#A grid deve se apoiar em um elemento ou na borda do grid. 
#O elemento recebe duas informações a row e a column

root =  tk.Tk()

var_nome = tk.StringVar(root)
var_idade = tk.IntVar(root)
var_nota = tk.DoubleVar(root)

#Configurando os elementos:
#Labels
lbl_Titulo = tk.Label(root,text="Cadastro de alunos")
lbl_nome = tk.Label(root, text= "Nome do aluno:")
lbl_idade = tk.Label(root,text="Idade do aluno:")
lbl_nota = tk.Label(root,text="Nota do aluno:")

#Entradas
entry_nome = tk.Entry(root,textvariable=var_nome)
entry_idade = tk.Entry(root,textvariable=var_idade)
entry_nota = tk.Entry(root,textvariable=var_nota)

#Mostrando os elementos com o grid
lbl_Titulo.grid(row=0, column= 3)
lbl_nome.grid(row=1, column= 0)
entry_nome.grid(row=1, column=1)
lbl_idade.grid(row=2,column=0)
entry_idade.grid(row=2,column=1)
lbl_nota.grid(row=3,column=0)
entry_nota.grid(row=3,column=1)

root.mainloop()