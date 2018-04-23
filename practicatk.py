from tkinter import *

root = Tk()
def hola():
	print("hola")

menubarra = Menu(root)
menubarra.add_command(label="hola", command=hola)
menubarra.add_command(label="quit", command=root.quit)

root.config(menu=menubarra)

root.mainloop()