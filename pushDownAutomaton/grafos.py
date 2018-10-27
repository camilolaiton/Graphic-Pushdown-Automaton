from graphviz import Digraph

def generarAutomata(nombre, transiciones, mostrar):
		
	g = Digraph("pushDownAutomaton", filename=nombre+".gv", format='png')
	g.attr(bgcolor='purple:pink')
	g.attr('node', shape='circle', style='filled', color='blue:cyan', gradientangle='270')
	g.attr('node', shape='doublecircle', style='filled', color='blue:cyan', gradientangle='270')
	g.attr(label='Push Down Automaton - '+nombre)
	g.attr("edge", style="filled", color='black:lightgray', gradientangle='270')

	g.attr(rankdir="LR", size="20")
	g.attr("node", shape="doublecircle")
	g.node("r")

	g.attr("node", shape="circle")

	g.edge("p", "p", label=labelString(transiciones[0]))

	g.edge("p", "q", label=labelString(transiciones[1]))

	g.edge("q", "q", label=labelString(transiciones[2]))

	g.edge("q", "r", label=labelString(transiciones[3]))

	g.render(None, None, mostrar, False)

def labelString(lista):
	labels = ""

	for i in lista:
		labels = labels + i

	return labels

#Transiciones para grafo 1
label_PtoP = ["b,b/bb \n", "a,b/ba \n", "b,a/ab \n", "a,a/aa \n", "b,#/#b \n", "a,#/#a \n"]
label_PtoQ = ["c,#/# \n", "c,b/b \n", "c,a/a \n"]
label_QtoQ = ["b,b/λ \n", "a,a/λ \n"]
label_QtoR = ["λ,#/#"]

edges1 = [label_PtoP, label_PtoQ, label_QtoQ, label_QtoR]

#Transiciones para grafo 2
label_PtoP = ["b,b/bb \n", "a,b/ba \n", "b,a/ab \n", "a,a/aa \n", "b,#/#b \n", "a,#/#a \n"]
label_PtoQ = ["b,b/λ \n", "a,a/λ \n"]
label_QtoQ = ["b,b/λ \n", "a,a/λ \n"]
label_QtoR = ["λ,#/#"]

edges2 = [label_PtoP, label_PtoQ, label_QtoQ, label_QtoR]

generarAutomata("Palindromo Impar", edges1, True)
generarAutomata("Palindromo Par", edges2, True)
