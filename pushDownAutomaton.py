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
			self.proceso.append([simboloInicial, 1, "", ""])

	def setEdges(self, edges):
		self.edges = edges

	def sacarCaminos(self, nodo):

		caminos = []#Lista de caminos

		if self.edges != None:
			#Saco los posibles caminos de un punto a otro
			for w in self.edges:
				divido = w[0].split("-")
				origen = divido[0]

				if origen == nodo:
					caminos.append(w)

		return caminos

	def __caminosPosibles(self, letra, caminos):

		caminosPosibles = []

		for x in caminos:
			for i in x:

				if "-" in i:
					caminosPosibles.append(i)
				else:
					leo, saco, meto = extraerExpresion(i)
					if leo == letra or leo == "λ":
							caminosPosibles.append(i)

		return caminosPosibles

	def evaluarCadena(self, cadena, nodo, pila, proceso, direccion):

		if self.edges != None:

			if cadena == "" and nodo == self.estadoFinal:
				self.pila = pila
				self.proceso = proceso
				return True

			if cadena == "":
				letra = "λ"

			caminosNodo = self.sacarCaminos(nodo)

			if caminosNodo != []:

				retorno = False
				caminosNodo = self.__caminosPosibles(cadena[0], caminosNodo)

				for i in caminosNodo:

					if "-" in i:
						direccion = i.split("-")

					else:
						leer, sacar, meter = extraerExpresion(i)

						if (leer == cadena[0] or leer == "λ") and (sacar == pila.verTope()):
							proceso.append([pila.sacarPila(), "0", i, direccion])

							for x in meter:
								if x != "λ":
									pila.apilar(x)
									proceso.append([x, "1", i, direccion])

						retorno = self.evaluarCadena(cadena[1:], direccion[1], pila, proceso, direccion)

					if retorno == True:
						self.pila = pila
						self.proceso = proceso 
						return True

				return retorno

			else:
				self.pila = pila
				self.proceso = proceso
				return False

#  Transiciones grafo 1 --- REGLAS CON ESTE AUTOMATA YA ESTA BUENO
"""
label_PtoP = ["p-p","b/b/bb", "a/b/ba", "b/a/ab", "a/a/aa", "b/#/#b", "a/#/#a"]
label_PtoQ = ["p-q","c/#/#", "c/b/b", "c/a/a"]
label_QtoQ = ["q-q","b/b/λ", "a/a/λ"]
label_QtoR = ["q-r","λ/#/#"]
"""
#Transiciones grafo 2 

label_PtoP = ["p-p","b/b/bb", "a/b/ba", "b/a/ab", "a/a/aa", "b/#/#b", "a/#/#a"]
label_PtoQ = ["p-q","b/b/λ", "a/a/λ"]
label_QtoQ = ["q-q","b/b/λ", "a/a/λ"]
label_QtoR = ["q-r","λ/#/#"]

edges = [label_PtoQ, label_PtoP, label_QtoR, label_QtoQ]

automata = PDA("p", "r", "#")
automata.setEdges(edges)
resultado = automata.evaluarCadena("aaaabbbbaaaa", automata.estadoInicial, automata.pila, automata.proceso, None)
print("\nResultado 2: ", resultado, " Proceso: ", automata.proceso)