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

#Transiciones grafo 2 

label_PtoP = ["p-p","b/b/bb", "a/b/ba", "b/a/ab", "a/a/aa", "b/#/#b", "a/#/#a"]
label_PtoQ = ["p-q","b/b/λ", "a/a/λ"]
label_QtoQ = ["q-q","b/b/λ", "a/a/λ"]
label_QtoR = ["q-r","λ/#/#"]

edges2 = [label_PtoQ, label_PtoP, label_QtoR, label_QtoQ]

def cambiarProceso(automata):
	if automata == "Palindromo Par":
		automata1.setEdges(edges2)
	else:
		automata1.setEdges(edges1)
	automata1.automata = automata
	cambiarImagen("", automata1.automata)


def funtion(boton):
	#print("click")
	
	if boton == botonRapido:
		botonRapido.config(bg="green")
		botonLento.config(bg="red")
		pila.sapi = False
		
	else:
		botonRapido.config(bg="red")
		botonLento.config(bg="green")
		pila.sapi = True


def cambiarImagen(elegir, automata):
	
    photo2 = PhotoImage(file="resources/"+automata+elegir+".png")
    label1.configure(image=photo2)
    label1.image = photo2

def comenzar():

	if txtUsuario.get() != "":
		resultado = automata1.evaluarCadena(txtUsuario.get(), automata1.estadoInicial, automata1.pila, automata1.proceso)
		pila.dibujarPila()
		
		cadena = ""
		if resultado == True:
			cadena = "Cadena Aceptada"
		else:
			cadena = "Cadena no Aceptada"

		if pila.indiceDeTexto != -1:
			canvas2.delete(pila.indiceDeTexto)
			pila.indiceDeTexto = -1

		pila.indiceDeTexto = canvas2.create_text(100, 20, text=cadena , activefill="blue", font="ArialBlack")

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
		self.automata = "Palindromo Impar"
		self.indiceDeTexto = -1

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
				
				if pila.sapi == True:
					SapiLee("Introduzco " + w[0]+" en pila")
				
				cambiarImagen(w[3], self.automata)
		
			else:
				self.decrementarPila()
				
				if pila.sapi == True:
					SapiLee("Saco " + w[0] +" en pila")
				
				cambiarImagen(w[3], self.automata)
			
			if destino != None:
				self.canvas.after(800, lambda:cambiarImagen(destino, self.automata))
			
			if pila.indiceDeTexto != -1:
				canvas2.delete(pila.indiceDeTexto)
				pila.indiceDeTexto = -1
			
			pila.indiceDeTexto = canvas2.create_text(170, 20, text = w[2], activefill="blue", font="ArialBlack")
			
			self.bandera += 1
			self.canvas.after(1000, self.dibujarPila)


coord = 130, 450, 300, 500

main_window = Tk()
main_window.title("PushDown Automaton")
main_window.geometry("1000x675")
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

label4 = Label(main_window, text="Estado", bg="white")
label4.grid(row=0, column=0, sticky ="nsew")

canvas2 = Canvas(label4, bg="white", width=350, height=150)
canvas2.pack()
canvas = Canvas(label2, bg='dark turquoise')
canvas.pack(expand=YES, fill=BOTH)

label3 = Label(main_window, bg="dark turquoise")
label3.grid(row=0, column=2, sticky="nsew")

label5 = Label(main_window, bg="dark turquoise")
label5.grid(row=1, column=2, sticky="nsew")

entrada = StringVar()

txtUsuario = Entry(label3, textvariable=entrada)
txtUsuario.pack()

automata1 = PDA("p", "r", "#")
automata1.setEdges(edges1)

pila = pilaGrafica(coord, automata1.proceso, canvas)

comenzarProceso = Button(label3, text="Comenzar", command=comenzar)
comenzarProceso.pack(expand=False, fill=BOTH)

botonLento = Radiobutton(label5, text="Lento",  bg="green", command=lambda:funtion(botonLento), value = "1")
botonLento.pack(expand=True, fill=BOTH)
botonRapido = Radiobutton(label5, text="Rapido", bg="red", command=lambda:funtion(botonRapido), value = "2")
botonRapido.pack(expand=True, fill=BOTH)

menugeneral = Menu(main_window)

menubarra = Menu(menugeneral, tearoff=0)
menubarra.add_command(label="Automata Par", command=lambda:cambiarProceso("Palindromo Par"))
menubarra.add_command(label="Automata Impar", command=lambda:cambiarProceso("Palindromo Impar"))
menubarra.add_separator()
menubarra.add_command(label="Salir", command=main_window.quit)

menugeneral.add_cascade(label="Seleccionar Automata", menu=menubarra)

main_window.config(menu=menugeneral)

main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=15)
main_window.columnconfigure(0, weight=0)
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
