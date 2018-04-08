from tkinter import *

ventana = Tk()
ventana.title("nueva ventana")
ventana.geometry("900x500")
ventana.config(background="dark turquoise")
etiqueta = Label(ventana, text="Automatas", bg="gold", fg="black")
etiqueta.pack()
imagenAuto = PhotoImage(file="Palindromo Impar.gv.png")
lbImage = Label(ventana, image=imagenAuto)
lbImage.pack()
ventana.mainloop()