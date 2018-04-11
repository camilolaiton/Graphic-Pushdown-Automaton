from graphviz import Digraph

class automataGrafico:
	def __init__(self, nombre, transiciones):
		self.nombre = nombre
		self.transiciones = transiciones
		self.fileImage = "resources/" + nombre + ".gv.png"

	def generarAutomata(self, mostrar, especial, nodo):
		
		g = Digraph("pushDownAutomaton", filename=self.nombre+".gv", format='png')
		g.attr(bgcolor='purple:pink')
		g.attr('node', shape='circle', style='filled', color='blue:cyan', gradientangle='270')
		g.attr('node', shape='doublecircle', style='filled', color='blue:cyan', gradientangle='270')
		g.attr(label='Push Down Automaton - '+self.nombre)
		g.attr("edge", style="filled", color='black:lightgray', gradientangle='270')

		g.attr(rankdir="UD", size="20")
		g.attr("node", shape="doublecircle")

		if nodo == "p":
			g.node("p", color = "red", shape='circle')
			g.node("q", shape='circle')
			g.node("r")
		elif nodo == "q":
			g.node("p", shape='circle')
			g.node("q", color = "red", shape='circle')
			g.node("r")
		elif nodo == "r":
			g.node("p", shape='circle')
			g.node("q", shape='circle')
			g.node("r", color="red")
		else:
			g.node("p", shape='circle')
			g.node("q", shape='circle')
			g.node("r")

		g.attr("node", shape="circle")

		origen = destino = None

		if especial != "":
			especial = especial.lower()
			divido = especial.split("-")
			origen = divido[0]
			destino = divido[1]

		if origen == "p" and destino == "p":
			g.edge("p", "p", label=self.__labelString(self.transiciones[0]), color="red")
		else:
			g.edge("p", "p", label=self.__labelString(self.transiciones[0]))

		if origen == "p" and destino == "q":
			g.edge("p", "q", label=self.__labelString(self.transiciones[1]), color="red")	
		else:
			g.edge("p", "q", label=self.__labelString(self.transiciones[1]))

		if origen == "q" and destino == "q":
			g.edge("q", "q", label=self.__labelString(self.transiciones[2]), color="red")
		else:
			g.edge("q", "q", label=self.__labelString(self.transiciones[2]))

		if origen == "q" and destino == "r":
			g.edge("q", "r", label=self.__labelString(self.transiciones[3]), color="red")
		else:
			g.edge("q", "r", label=self.__labelString(self.transiciones[3]))

		if nodo != "":
			nombre = "resources/"+self.nombre+nodo
		else:
			nombre = "resources/"+self.nombre+especial

		g.render(nombre, None, mostrar, False)

	def __labelString(self, lista):
		labels = ""

		for i in lista:
			labels = labels + i + "\n"

		return labels


#Transiciones para grafo 1
label_PtoP = ["b/b/bb", "a/b/ba", "b/a/ab", "a/a/aa", "b/#/#b", "a/#/#a"]
label_PtoQ = ["c/#/#", "c/b/b", "c/a/a"]
label_QtoQ = ["b/b/λ", "a/a/λ"]
label_QtoR = ["λ/#/#"]

edges1 = [label_PtoP, label_PtoQ, label_QtoQ, label_QtoR]

#Transiciones para grafo 2
label_PtoP = ["b/b/bb", "a/b/ba", "b/a/ab", "a/a/aa", "b/#/#b", "a/#/#a"]
label_PtoQ = ["b/b/λ", "a/a/λ"]
label_QtoQ = ["b/b/λ", "a/a/λ"]
label_QtoR = ["λ/#/#"]

edges2 = [label_PtoP, label_PtoQ, label_QtoQ, label_QtoR]

automata1 = automataGrafico("Palindromo Impar", edges1)
automata2 = automataGrafico("Palindromo Par", edges2)

automata1.generarAutomata(False, "", "")
automata1.generarAutomata(False, "", "p")
automata1.generarAutomata(False, "", "q")
automata1.generarAutomata(False, "", "r")
automata1.generarAutomata(False, "p-p", "")
automata1.generarAutomata(False, "p-q", "")
automata1.generarAutomata(False, "q-q", "")
automata1.generarAutomata(False, "q-r", "")

automata2.generarAutomata(False, "", "")
automata2.generarAutomata(False, "", "p")
automata2.generarAutomata(False, "", "q")
automata2.generarAutomata(False, "", "r")
automata2.generarAutomata(False, "p-p", "")
automata2.generarAutomata(False, "p-q", "")
automata2.generarAutomata(False, "q-q", "")
automata2.generarAutomata(False, "q-r", "")