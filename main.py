from tkinter import *
from pila import Pila 

def pintarPila(coord, mensaje):
	
	i = canvas.create_rectangle(coord, width=5, fill='red', activefill="#0017F9")
	m = canvas.create_text (coord[2]-80, coord[1]+20, text = mensaje, activefill="blue")
	return i, m

def borrarPila(i, m):
	canvas.delete(m)
	canvas.delete(i)

class pilaGrafica:
	def __init__(self, coord):
		self.coord = coord
		self.lista = []
		self.mensajes = []
		self.aumentarPila()

	def aumentarPila(self):
		
		if len(self.lista) < 10:
			i, m = pintarPila(self.coord, "cristian es caga")
			self.lista.append(i)
			self.mensajes.append(m)
			self.coord = self.coord[0], self.coord[1]-50, self.coord[2], self.coord[3]-50

	def decrementarPila(self):

		if len(self.lista) > 1:
			self.coord = self.coord[0], self.coord[1]+50, self.coord[2], self.coord[3]+50
			borrarPila(self.lista.pop(), self.mensajes.pop())

main_window = Tk()
main_window.title("PushDown Automaton")
main_window.geometry("1000x600")
main_window.config(background="dark turquoise")
main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)

imagenAuto = PhotoImage(file="Palindromo Impar.gv.png")

label0 = Label(main_window, text="Pushdown Automaton", bg="gold", fg="black")
label0.grid(row=0, column=1, sticky="nsew")

label1 = Label(main_window, bg="dark turquoise", image=imagenAuto)
label1.grid(row=1, column=0, sticky="nsew")

label2 = Label(main_window, bg="dark turquoise")
label2.grid(row=1, column=1, sticky="nsew")

canvas = Canvas(label2, bg='dark turquoise')

coord = 30, 500, 200, 550

#lista = []
#cuadrito = canvas.create_rectangle(coord, width=5, fill='red', activefill="#0017F9")

#canvas.insert(cuadrito, 0, "hola")
canvas.pack(expand=YES, fill=BOTH)

label3 = Label(main_window, bg="dark turquoise")
label3.grid(row=1, column=2, sticky="nsew")

pila = pilaGrafica(coord)

AumentarPila = Button(label3, text="Aumentar pila", command=pila.aumentarPila)
AumentarPila.pack(expand=False, fill=BOTH)

DecrementarPila = Button(label3, text="Decrementar Pila", command=pila.decrementarPila)
DecrementarPila.pack(expand=False, fill=BOTH)

main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=15)
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)
main_window.mainloop()

"""
ventana = Tk()
ventana.title("PushDown Automaton")
ventana.geometry("1000x600")
ventana.config(background="dark turquoise")
etiqueta = Label(ventana, text="Automatas", bg="gold", fg="black")
etiqueta.pack()

ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

imagenAuto = PhotoImage(file="Palindromo Impar.gv.png")
lbImage = Label(ventana, image=imagenAuto)
lbImage.pack()

ventana.mainloop()
"""