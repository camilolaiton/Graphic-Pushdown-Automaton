from pila import Pila

class PDA:
	def __init__(self, estadoInicial, estadoAceptacion, simboloInicial):
		self.estadoInicial = estadoInicial
		self.estadoFinal = estadoAceptacion
		self.edges = None
		self.pila = Pila()
		
		if simboloInicial != None:
			self.pila.apilar(simboloInicial)
			print(self.pila.verTope())

	def setEdges(self, edges):
		self.edges = edges

	def evaluarCadena(self, cadena):
		

automata1 = PDA("p", "r", "Z")

label_PtoP = ["b,b/bb \n", "a,b/ba \n", "b,a/ab \n", "a,a/aa \n", "b,#/#b \n", "a,#/#a \n"]
label_PtoQ = ["c,#/# \n", "c,b/b \n", "c,a/a \n"]
label_QtoQ = ["b,b/λ \n", "a,a/λ \n"]
label_QtoR = ["λ,#/#"]

edges1 = [label_PtoP, label_PtoQ, label_QtoQ, label_QtoR]

automata1.setEdges(edges1)






