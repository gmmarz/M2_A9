import tkinter as tk

root =  tk.Tk()

#Text (caixa de texto)

text = tk.Text(root,height=5,width=30)
text.pack()

text.insert(tk.END,"Este é um exemplo de caixa de texto")

root.mainloop()