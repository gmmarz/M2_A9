import tkinter as tk


root =  tk.Tk()

#Radio button
radio_var = tk.StringVar()

radio1 = tk.Radiobutton(root,text="Opcao 1", variable=radio_var, value="Opcao1")
radio2 = tk.Radiobutton(root,text="Opcao 2", variable=radio_var, value="Opcao2")

#Mostrnado os elementos
radio1.pack()
radio2.pack()



root.mainloop()