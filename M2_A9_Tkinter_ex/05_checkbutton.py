import tkinter as tk

def Check_get():
    if check_var.get():
        msg_chck.set("Termo aceito")
    else:
        msg_chck.set("Termo não aceito")

root =  tk.Tk()

check_var = tk.BooleanVar(root)
msg_chck = tk.StringVar(root)
#label
label = tk.Label(root, textvariable=msg_chck)

#Checkbox
checkbutton = tk.Checkbutton(root,text="Aceitar termos", variable=check_var,onvalue=True,offvalue=False, command=Check_get)

#Montando os elementos
label.pack()
checkbutton.pack()


root.mainloop()