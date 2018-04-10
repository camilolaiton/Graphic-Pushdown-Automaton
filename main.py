from tkinter import *
from pila import Pila 
from pushDownAutomaton import PDA
import time

def pintarPila(coord, mensaje):	
	i = canvas.create_rectangle(coord, width=5, fill='red', activefill="#0017F9")
	m = canvas.create_text (coord[2]-80, coord[1]+20, text = mensaje, activefill="blue")
	return i, m

def borrarPila(i, m):
	canvas.delete(m)
	canvas.delete(i)

class pilaGrafica:
	def __init__(self, coord, proceso):
		self.coord = coord
		self.lista = []
		self.mensajes = []
		self.proceso = proceso

	def aumentarPila(self, mensaje):
		
		if len(self.lista) < 10:
			i, m = pintarPila(self.coord, mensaje)
			self.lista.append(i)
			self.mensajes.append(m)
			self.coord = self.coord[0], self.coord[1]-50, self.coord[2], self.coord[3]-50

	def decrementarPila(self):

		if len(self.lista) > 1:
			self.coord = self.coord[0], self.coord[1]+50, self.coord[2], self.coord[3]+50
			borrarPila(self.lista.pop(), self.mensajes.pop())

	def dibujarPila(self):

		for w in self.proceso:
			if w[1] == 1:
				print("mete")
				self.aumentarPila(w[0])
			else:
				print("saco")
				self.decrementarPila()

			#time.sleep(1)

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

automata1 = PDA("p", "r", "#")
#  Transiciones grafo 1 --- REGLAS CON ESTE AUTOMATA YA ESTA BUENO

label_PtoP = ["p-p","b/b/bb", "a/b/ba", "b/a/ab", "a/a/aa", "b/#/#b", "a/#/#a"]
label_PtoQ = ["p-q","c/#/#", "c/b/b", "c/a/a"]
label_QtoQ = ["q-q","b/b/λ", "a/a/λ"]
label_QtoR = ["q-r","λ/#/#"]

edges1 = [label_PtoQ, label_PtoP, label_QtoR, label_QtoQ]
automata1.setEdges(edges1)

print(automata1.evaluarCadena("abbcbba", automata1.estadoInicial))
print("Proceso de la pila donde 1 es meter y 0 es sacar: \n", automata1.proceso)

pila = pilaGrafica(coord, automata1.proceso)

Comenzar = Button(label3, text="Comenzar proceso", command=pila.dibujarPila)
Comenzar.pack(expand=False, fill=BOTH)

"""
AumentarPila = Button(label3, text="Aumentar pila", command=pila.aumentarPila)
AumentarPila.pack(expand=False, fill=BOTH)

DecrementarPila = Button(label3, text="Decrementar Pila", command=pila.decrementarPila)
DecrementarPila.pack(expand=False, fill=BOTH)
"""
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=15)
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)
main_window.mainloop()
