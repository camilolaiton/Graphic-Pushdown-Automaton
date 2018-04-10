from pila import Pila

def extraerExpresion(cadena):
	divido = cadena.split("/")
	leer = divido[0]
	saca = divido[1]
	mete = divido[2]

	return leer, saca,  mete

class PDA:
	def __init__(self, estadoInicial, estadoAceptacion, simboloInicial):
		self.estadoInicial = estadoInicial
		self.estadoFinal = estadoAceptacion
		self.edges = None
		self.pila = Pila()
		self.proceso = [] # 1 para meter, 0 para sacar
		
		if simboloInicial != None:
			self.pila.apilar(simboloInicial)
			self.proceso.append([simboloInicial, 1])
			print(self.pila.verTope())

	def setEdges(self, edges):
		self.edges = edges

	def buscarNodo(self, nodo):

		caminos = []#Lista de caminos

		#Saco los posibles caminos de un punto a otro
		for w in self.edges:
			divido = w[0].split("-")
			origen = divido[0]

			if origen == nodo:
				caminos.append(w)

		if caminos != []:
			return True, caminos

		return False, caminos

	def evaluarCadena(self, cadena, actual):

		if self.edges != None:
			
			if (cadena == "" or cadena == "λ") and actual == self.estadoFinal:
				return "Palabra aceptada"

			if cadena != "":
				letra = cadena[0]

			else:
				cadena = letra = "λ"

			actual = actual.lower()#Nodo donde se encuentra

			encontro, posibleCamino = self.buscarNodo(actual)
			#Recorro todos los posibles caminos si los hay

			if posibleCamino != []:

				encontroCamino = False

				for w in posibleCamino:
					ver = w[0]
					
					#Divido el string para saber Nodo origen a nodo destino
					divido = ver.split("-")
					origen = divido[0]
					destino = divido[1]

					#Recorro cada regla para sacar leo/saco/meto para evaluar

					for regla in w:

						if "-" not in regla:
							leo, saco, meto = extraerExpresion(regla)

							if leo == letra or leo == "λ":
								if saco == self.pila.verTope():
									#Meto valores en la pila
									#Si el leo y saco estan bien
									encontroCamino = True
									
									self.proceso.append([self.pila.sacarPila(), 0])

									for x in meto:
										if x != "λ":
											self.pila.apilar(x)
											self.proceso.append([x, 1])

									if leo == "λ":
										return self.evaluarCadena(cadena, destino)
									else:
										cadena = cadena[1:]
										return self.evaluarCadena(cadena, destino)

				if encontroCamino == False:
					return "Palabra no aceptada, no encontro camino"

			else:
				return "Palabra no aceptada, no encontro caminos"

automata1 = PDA("p", "r", "#")
#  Transiciones grafo 1 --- REGLAS CON ESTE AUTOMATA YA ESTA BUENO

label_PtoP = ["p-p","b/b/bb", "a/b/ba", "b/a/ab", "a/a/aa", "b/#/#b", "a/#/#a"]
label_PtoQ = ["p-q","c/#/#", "c/b/b", "c/a/a"]
label_QtoQ = ["q-q","b/b/λ", "a/a/λ"]
label_QtoR = ["q-r","λ/#/#"]

#Transiciones grafo 2 
"""
label_PtoP = ["p-p","b/b/bb", "a/b/ba", "b/a/ab", "a/a/aa", "b/#/#b", "a/#/#a"]
label_PtoQ = ["p-q","b/b/λ", "a/a/λ"]
label_QtoQ = ["q-q","b/b/λ", "a/a/λ"]
label_QtoR = ["q-r","λ/#/#"]"""

edges1 = [label_PtoQ, label_PtoP, label_QtoR, label_QtoQ]

automata1.setEdges(edges1)
print(automata1.evaluarCadena("abbcbba", automata1.estadoInicial))
print(automata1.proceso)