from graphviz import Digraph

def labelString(lista):
	labels = ""

	for i in lista:
		labels = labels + i

	return labels

#Transiciones 
label_PtoP = ["b,b/bb \n", "a,b/ba \n", "b,a/ab \n", "a,a/aa \n", "b,#/#b \n", "a,#/#a \n"]
label_PtoQ = ["c,#/# \n", "c,b/b \n", "c,a/a \n"]
label_QtoQ = ["b,b/λ \n", "a,a/λ \n"]
label_QtoR = ["λ,#/#"]

transiciones = [label_PtoP, label_PtoQ, label_QtoQ, label_QtoR]

g = Digraph("pushDownAutomaton", filename="pda.gv", format='png')
g.attr(bgcolor='purple:pink')
g.attr('node', shape='circle', style='filled', color='blue:cyan', gradientangle='270')
g.attr('node', shape='doublecircle', style='filled', color='blue:cyan', gradientangle='270')
g.attr(label='Push Down Automaton - Palindromo Impar')
g.attr("edge", style="filled", color='black:lightgray', gradientangle='270')

g.attr(rankdir="LR", size="20")
g.attr("node", shape="doublecircle")
g.node("r")

g.attr("node", shape="circle")

g.edge("p", "p", label=labelString(label_PtoP))

g.edge("p", "q", label=labelString(label_PtoQ))

g.edge("q", "q", label=labelString(label_QtoQ))

g.edge("q", "r", label=labelString(label_QtoR))

g.render(None, None, True, False)
