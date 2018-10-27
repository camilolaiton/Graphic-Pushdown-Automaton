from tkinter import *
from turingMachine import TuringMachine
from grafos import automataGrafico
import win32com.client as clwin
import ast

#153 - 203 -> 130
#103 - 153 -> 130
#53 - 103 -> 80
#3 - 103 -> 30

def convertirDiccionario(transiciones):
	estadoInicial = estadoFinal = None
	contador = 0

	for clave, valor in transiciones.items():

		if (len(transiciones.items())-1) - (len(transiciones.items())-1) == contador:
			estadoInicial = clave[0]

		if len(transiciones.items())-1 == contador:
			estadoFinal = valor[0]

		contador = contador + 1

	return estadoInicial, estadoFinal

def hija():

	def dibujarCerrar():
		diccionario = entrada.get()
		t1.destroy()
		return convertirDiccionario(ast.literal_eval(diccionario))


	t1 = Toplevel(main_window,bg="white")
	t1.geometry("300x200")

	t1.focus_set()
	t1.grab_set()
	t1.transient(master=main_window)
	entrada = Entry(t1)
	entrada.pack(expand=YES, fill=BOTH)
	Button(t1, text="Ingresar", bg="white", command=dibujarCerrar).pack()

def SapiLee(lectura):
	habla = clwin.Dispatch("SAPI.SpVoice")
	habla.Speak(lectura)

def comenzar():

	if entrada.get() != "":
		if len(entrada.get()) > 11:
			SapiLee("Palabras aceptadas menores a tamaño 13, por espacio grafico")
			return

		T1.setCadena(entrada.get())
		cinta1.eliminarCinta()
		cinta1.dibujarCinta()
		cinta1.reemplazarCinta()

	else:
		SapiLee("Por favor, introduzca una cadena de caracteres")

def cambiarImagen(elegir):
	
    photo2 = PhotoImage(file="turingResources/TuringMachine"+elegir+".png")
    label1.configure(image=photo2)
    label1.image = photo2

def makeentry(parent, caption, width=None, **options):
    Label(parent, text=caption).pack(side=TOP)
    entry = Entry(parent, **options)
    if width:
        entry.config(width=width)
    entry.pack(fill=BOTH)
    return entry

class cintaGrafica:

	def __init__(self, coord, proceso, canvas):
		self.coord = coord
		self.proceso = proceso
		self.canvas = canvas
		self.indexLinea = -1
		self.cuadritos = []
		self.textos = []
		self.coordLinea = []
		self.indiceCabeza = 0

	def dibujarCinta(self):
		self.coordLinea = []
		self.indexLinea = -1
		self.proceso = []
		self.cuadritos = []
		self.textos = []

		for i in range(20):
			self.aumentarCinta()

	def aumentarCinta(self):
		i = self.canvas.create_rectangle(self.coord, width=5, fill="purple", activefill="#FF0202")
		m = self.canvas.create_text(self.coord[0]+27, self.coord[3]-30, text = "□", activefill="blue", fill="white")
		self.coord = self.coord[0]+50, self.coord[1], self.coord[2]+50, self.coord[3]
		self.cuadritos.append(i)
		self.textos.append(m)

	def eliminarCinta(self):

		if self.cuadritos != [] and self.textos != []:
			self.coord = 3, 100, 53, 150

			for i in range(20):
				self.canvas.delete(self.cuadritos.pop())
				self.canvas.delete(self.textos.pop())

			self.cuadritos = self.textos = []
			self.canvas.delete(self.indexLinea)
			self.coordLinea = []
			self.indexLinea = -1
			self.indiceCabeza = 0

	def reemplazarCinta(self):
		
		var = 0
		cadena = T1.cadena

		for i in range(3,14):
			ide = self.textos[i]

			if i == 3:
				indice = self.cuadritos[i]
				self.coordLinea = canvas.coords(indice)
				self.coordLinea = self.coordLinea[0], self.coordLinea[1]+50, self.coordLinea[2], self.coordLinea[1]+50
				self.indexLinea = self.canvas.create_line(self.coordLinea[0], self.coordLinea[1], self.coordLinea[2], self.coordLinea[3], fill="red", width=6)
				self.indiceCabeza = self.textos[3]

			w = cadena[var]
			var += 1
			self.reemplazarTexto(ide, w)

			if len(cadena) == var:
				return 

	def reemplazarTexto(self, ide, texto):
		self.canvas.itemconfig(ide, text=texto)

	def correrLineaAdelante(self):
		self.coordLinea = self.coordLinea[0]+50, self.coordLinea[1], self.coordLinea[2]+50, self.coordLinea[3]
		self.canvas.delete(self.indexLinea)
		self.indexLinea = self.canvas.create_line(self.coordLinea[0], self.coordLinea[1], self.coordLinea[2], self.coordLinea[3], fill="red", width=6)

	def correrLineaAtras(self):
		self.coordLinea = self.coordLinea[0]-50, self.coordLinea[1], self.coordLinea[2]-50, self.coordLinea[3]
		self.canvas.delete(self.indexLinea)
		self.indexLinea = self.canvas.create_line(self.coordLinea[0], self.coordLinea[1], self.coordLinea[2], self.coordLinea[3], fill="red", width=6)

	def pasoApaso(self):
		if T1.cadena != [] and T1.acabarProceso() == False:
			simbolo_nuevo, direccion, imagen, rule = T1.evaluarLetra()

			if T1.terminado == True and rule == None:
				SapiLee("No se ha encontrado una transicion válida.")
				return 

			self.reemplazarTexto(self.indiceCabeza, simbolo_nuevo)
			self.reemplazarTexto(ruleID, "REGLA USADA:  "+rule)
			self.indiceCabeza = self.textos[3+T1.posCabeza]

			if T1.terminado == False:
				self.canvas.after(0, lambda:cambiarImagen(imagen[0]+"-"+imagen[1]))
				self.canvas.after(400, lambda:cambiarImagen(imagen[1]))
			else:
				SapiLee("La maquina de Turing ha finalizado su proceso.")
				return

			if direccion == None:
				SapiLee("La maquina de Turing ha finalizado su proceso.")
			elif "R" == direccion or "r" == direccion:
				self.correrLineaAdelante()
			else:
				self.correrLineaAtras()

		else:
			SapiLee("La maquina de Turing ha finalizado su proceso.")

	def procesoEntero(self):
		if T1.cadena != []:
			if T1.acabarProceso() == False:
				self.pasoApaso()
				self.canvas.after(600, self.procesoEntero)
			else:
				SapiLee("La maquina de Turing ha finalizado su proceso.")

transiciones = {
				("q1", "a"):("q1", "a", "R"),
				("q1", "b"):("q1", "a", "R"),
				("q1", "□"):("q2", "□", "L"),
				("q2", "a"):("q2", "a", "L"),
				("q2", "□"):("q3", "□", "L")
				}

estadoInicial, estadoFinal = convertirDiccionario(transiciones)

turing1 = automataGrafico("TuringMachine", transiciones)
turing1.generarNuevoTuring()

T1 = TuringMachine(estadoInicial, [estadoFinal], transiciones)

main_window = Tk()
main_window.title("PushDown Automaton")
main_window.geometry("1000x600")
main_window.config(background="dark turquoise")
main_window.columnconfigure(0, weight=1)
main_window.columnconfigure(1, weight=2)
main_window.rowconfigure(0, weight=5)
main_window.rowconfigure(1, weight=0)

imagenAuto = PhotoImage(file="turingResources/TuringMachine.png")

label0 = Label(main_window, text="Turing Machine", bg="dark turquoise", fg="black")
label0.grid(row=0, column=0, sticky="nsew")

label1 = Label(main_window, bg="dark turquoise", image=imagenAuto)
label1.grid(row=0, column=1, sticky="nsew")

label2 = Label(main_window, bg="dark turquoise")
label2.grid(row=1, column=0, sticky="nsew")

label3 = Label(main_window, bg="dark turquoise")
label3.grid(row=1, column=1, sticky="nsew")

#Elementos label 3
canvas = Canvas(label3, bg='dark turquoise')
canvas.pack(expand=YES, fill=BOTH)
ruleID = canvas.create_text(200, 30, text = "REGLA USADA: ", activefill="blue", fill="white", font="Tahoma")
#Fin elementos label 3

#Inicio de la union logica y grafica

coord = 3, 100, 53, 150
cinta1 = cintaGrafica(coord, [], canvas)
#Fin logica y grafica

#Elementos para label 2
labelInterno2 = Label(label2, bg="dark turquoise", text="MENU")
labelInterno2.pack(expand=False, fill=BOTH)
entrada = makeentry(label2, "Introduzca la cadena", 10)
comenzarProceso = Button(label2, text="Guardar cadena", command=comenzar)
comenzarProceso.pack(expand=False, fill=BOTH)
paso = Button(label2, text="Paso a paso", command=cinta1.pasoApaso)
paso.pack(expand=False, fill=BOTH)
proceso = Button(label2, text="Proceso entero", command=cinta1.procesoEntero)
proceso.pack(expand=False, fill=BOTH)
nuevoTuring = Button(label2, text="Nuevo turing", command=hija)
nuevoTuring.pack(expand=False, fill=BOTH)
#Fin elementos label 2

main_window.mainloop()