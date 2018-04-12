import win32com.client as clwin
from tkinter import *
from pila import Pila 
from pushDownAutomaton import PDA
import time

#  Transiciones grafo 1 --- REGLAS CON ESTE AUTOMATA YA ESTA BUENO

label_PtoP = ["p-p","b/b/bb", "a/b/ba", "b/a/ab", "a/a/aa", "b/#/#b", "a/#/#a"]
label_PtoQ = ["p-q","c/#/#", "c/b/b", "c/a/a"]
label_QtoQ = ["q-q","b/b/λ", "a/a/λ"]
label_QtoR = ["q-r","λ/#/#"]

edges1 = [label_PtoQ, label_PtoP, label_QtoR, label_QtoQ]

def cambiarImagen(elegir):
	
    photo2 = PhotoImage(file="resources/Palindromo Impar"+elegir+".png")
    label1.configure(image=photo2)
    label1.image = photo2

def comenzar():

	if txtUsuario.get() != "":
		resultado = automata1.evaluarCadena(txtUsuario.get(), automata1.estadoInicial)
		pila.dibujarPila()
		
		if resultado == "Palabra aceptada":
			resultado1.config(text="palabra aceptada")
		else:
			resultado1.config(text="palabra no aceptada")

	else:
		SapiLee("Por favor, introduzca una cadena de caracteres")
		
def SapiLee(lectura):
	habla = clwin.Dispatch("SAPI.SpVoice")
	habla.Speak(lectura)

class pilaGrafica:
	def __init__(self, coord, proceso, canvas):
		self.coord = coord
		self.lista = []
		self.mensajes = []
		self.proceso = proceso
		self.canvas = canvas
		self.mensaje = ""
		self.bandera = 0

	def aumentarPila(self):
		
		if len(self.lista) < 10:
			#i, m = pintarPila(self.coord, mensaje)
			i = self.canvas.create_rectangle(self.coord, width=5, fill='red', activefill="#0017F9")
			m = self.canvas.create_text(self.coord[2]-80, self.coord[1]+20, text = self.mensaje, activefill="blue")

			self.lista.append(i)
			self.mensajes.append(m)
			self.coord = self.coord[0], self.coord[1]-50, self.coord[2], self.coord[3]-50

	def decrementarPila(self):

		self.coord = self.coord[0], self.coord[1]+50, self.coord[2], self.coord[3]+50
		self.canvas.delete(self.lista.pop())
		self.canvas.delete(self.mensajes.pop())
		#borrarPila(self.lista.pop(), self.mensajes.pop())

	def dibujarPila(self):

		if self.bandera < len(self.proceso):
			
			w = self.proceso[self.bandera]

			destino = None
			ver = w[3]
	
			#Divido el string para saber Nodo origen a nodo destino
			if len(ver) > 1:
				divido = ver.split("-")
				destino = divido[1]

			if w[1] == 1:
				self.mensaje = w[0]
				self.aumentarPila()
				SapiLee("Introduzco " + w[0]+" en pila")
				cambiarImagen(w[3])
		
			else:
				self.decrementarPila()
				SapiLee("Saco " + w[0] +" en pila")
				cambiarImagen(w[3])
			
			if destino != None:
				self.canvas.after(800, lambda:cambiarImagen(destino))

			self.bandera += 1
			self.canvas.after(1000, self.dibujarPila)


def funtion(boton):
	#print("click")
	if boton == botonRapido:
		botonRapido.config(bg="green")
		botonLento.config(bg="red")
	else:
		botonRapido.config(bg="red")
		botonLento.config(bg="green")

coord = 30, 500, 200, 550

main_window = Tk()
main_window.title("PushDown Automaton")
main_window.geometry("1000x600")
main_window.config(background="dark turquoise")
main_window.columnconfigure(0, weight=1)
main_window.rowconfigure(0, weight=1)

imagenAuto = PhotoImage(file="resources/Palindromo Impar.png")

label0 = Label(main_window, text="Pushdown Automaton", bg="gold", fg="black")
label0.grid(row=0, column=1, sticky="nsew")

label1 = Label(main_window, bg="dark turquoise", image=imagenAuto)
label1.grid(row=1, column=0, sticky="nsew")

label2 = Label(main_window, bg="dark turquoise")
label2.grid(row=1, column=1, sticky="nsew")

canvas = Canvas(label2, bg='dark turquoise')
canvas.pack(expand=YES, fill=BOTH)

label3 = Label(main_window, bg="dark turquoise")
label3.grid(row=1, column=2, sticky="nsew")

entrada = StringVar()

txtUsuario = Entry(label3, textvariable=entrada)
txtUsuario.pack()

automata1 = PDA("p", "r", "#")
automata1.setEdges(edges1)

pila = pilaGrafica(coord, automata1.proceso, canvas)

comenzarProceso = Button(label3, text="Comenzar", command=comenzar)
comenzarProceso.pack(expand=False, fill=BOTH)

botonLento = Button(label3, text="Lento", font="Algerian",  bg="green", command=lambda:funtion(botonLento))
#botonLento.pack(expand=False, fill=BOTH)
botonRapido = Button(label3, text="rapido1", highlightcolor="black", font="Algerian", bg="red", command=lambda:funtion(botonRapido))
#botonRapido.pack(expand=False, fill=BOTH)

resultado1 = Label(label1)
#resultado1.pack(expand=False, fill=BOTH)

main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=15)
main_window.columnconfigure(0, weight=5)
main_window.columnconfigure(1, weight=1)
main_window.columnconfigure(2, weight=1)


#pila.dibujarPila()

"""
AumentarPila = Button(label3, text="Aumentar pila", command=pila.aumentarPila)
AumentarPila.pack(expand=False, fill=BOTH)

DecrementarPila = Button(label3, text="Decrementar Pila", command=pila.decrementarPila)
DecrementarPila.pack(expand=False, fill=BOTH)
"""
main_window.mainloop()
