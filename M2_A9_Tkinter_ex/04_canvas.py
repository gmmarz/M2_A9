import tkinter as tk

root =  tk.Tk()

#canvas(tela)
canvas = tk.Canvas(root,width=500,height=300)
canvas.pack()

canvas.create_rectangle(10,10,100,60,fill="blue")

root.mainloop()