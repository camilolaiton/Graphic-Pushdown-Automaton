
from tkinter import *

nodoInicial = []
listaNodos = []
elegido = 0
inicial = 0

def cambiarElegido(value):
	global elegido
	elegido = value

def dibujarFlecha(posX, posY):
	canvas.create_line(posX-60, posY+30, posX, posY+30, width=3, fill="black")

def elegirClaseNodo():

	def dibujarCerrar():
		t2.destroy()

	t2 = Toplevel(main_window,bg="white")
	t2.geometry("300x200")

	t2.focus_set()
	t2.grab_set()
	t2.transient(master=main_window)
	nodoInicial = Radiobutton(t2, text="Nodo inicial", value="1", indicatoron=0, command=lambda:cambiarElegido(1))
	nodoInicial.pack(expand=YES, fill=BOTH)

	nodoNormal = Radiobutton(t2, text="Nodo normal", value="2", indicatoron=0, command=lambda:cambiarElegido(2))
	nodoNormal.pack(expand=YES, fill=BOTH)

	nodoFinal = Radiobutton(t2, text="Nodo final", value="3", indicatoron=0, command=lambda:cambiarElegido(3))
	nodoFinal.pack(expand=YES, fill=BOTH)

	Cerrar = Button(t2, text="ELEGIR", bg="white", command=dibujarCerrar).pack()

def hija(texto):
 
    t1 = Toplevel(main_window,bg="white")
    t1.geometry('300x100')
 
    t1.focus_set()
    t1.grab_set()
    t1.transient(master=main_window)
    Label(t1, text=texto,bg="white").pack(padx=10, pady=10)
    Button(t1,text="Cerrar",bg="red", command=t1.destroy).pack()
    t1.wait_window(t1)

def buscarNodo(posX, posY):
	for i in listaNodos:
		aux = canvas.coords(i)

		if((posX >= aux[0] - 100 and posX <= aux[0] + 100) and (posY >= aux[1] - 100 and posY <= aux[1] + 100)):
			return True

	return False

"""
def key(event):
    print ("pressed", repr(event.char))
"""

def callback(event):
	if buscarNodo(event.x, event.y) == False:
		global inicial

		if elegido == 2:
			listaNodos.append(canvas.create_oval(event.x, event.y, event.x+70, event.y+70, width=3, fill="purple"))
		elif elegido == 3:
			listaNodos.append(canvas.create_oval(event.x, event.y, event.x+70, event.y+70, width=3, fill="purple"))
			canvas.create_oval(event.x+10, event.y+10, event.x+60, event.y+60, width=3, fill="purple")
		elif inicial == 0 and elegido == 1:
			inicial = inicial + 1
			dibujarFlecha(event.x, event.y)
			listaNodos.append(canvas.create_oval(event.x, event.y, event.x+70, event.y+70, width=3, fill="purple"))
	else:
		hija("No hay suficiente espacio entre nodos")

def elegirPintar(event):
	global elegido
	elegido = elegirClaseNodo()

main_window = Tk()
main_window.title("Turing Automaton")
main_window.geometry("1000x600")
main_window.rowconfigure(0, weight=1)
main_window.rowconfigure(1, weight=1)
main_window.columnconfigure(0, weight=2)
main_window.columnconfigure(1, weight=1)

label0 = Label(main_window, bg="gold")
label0.grid(row=0, column=0, sticky="nsew")

label1 = Label(main_window, text="Colocar nodo", bg="gold")
label1.bind("<Button-1>", elegirPintar)
label1.grid(row=0, column=1)

canvas= Canvas(label0, width=930)
#canvas.bind("<Key>", key)
canvas.bind("<Button-1>", callback)
canvas.pack(expand=YES, fill=BOTH)

main_window.mainloop()