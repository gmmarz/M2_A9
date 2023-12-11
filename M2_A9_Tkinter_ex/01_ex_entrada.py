import tkinter as tk

root =  tk.Tk()

#bg é para mudar o background color do campo de entrada
entry_text = tk.StringVar()
entry = tk.Entry(root,textvariable=entry_text, bg= 'red')
entry.pack()

root.mainloop()
