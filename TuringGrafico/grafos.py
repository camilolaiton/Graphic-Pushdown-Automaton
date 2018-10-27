from graphviz import Digraph
import os
import shutil

class automataGrafico:
	def __init__(self, nombre, transiciones2):
		self.nombre = nombre
		self.transiciones2 = transiciones2
		self.__nodos = []
		self.__listaTrabajo = []

	def verificarRuta(self):
		if os.path.exists("turingResources"):
			shutil.rmtree("turingResources")

		os.mkdir("turingResources")

	def obtenerListaTrabajo(self):
		listaAux = []
		for clave, valor in self.transiciones2.items():
			if clave[0]+"-"+valor[0] not in listaAux:
				listaAux.append(clave[0]+"-"+valor[0])
				listaAux.append(clave[1]+","+valor[1]+","+valor[2])
			else:
				index = listaAux.index(clave[0]+"-"+valor[0])
				listaAux.insert(index+1, clave[1]+","+valor[1]+","+valor[2])

		self.__listaTrabajo = listaAux

	def __extraerNodos(self, listaAux):
		listaNodos = []
		for i in listaAux:
			if "-" in i:
				divido = i.split("-")
				origen = divido[0]
				destino = divido[1]

				if origen not in listaNodos:
					listaNodos.append(origen)

				if destino not in listaNodos:
					listaNodos.append(destino)

		self.__nodos = listaNodos

	def generarTuring(self):
		self.obtenerListaTrabajo()
		self.__extraerNodos(self.__listaTrabajo)

		g = Digraph("Turing Machine", filename="TuringMachine.gv", format='png')
		g.attr(bgcolor="purple:pink")
		g.attr('node', shape='circle', style='filled', color='blue:cyan', gradientangle='270')
		g.attr('node', shape='doublecircle', style='filled', color='blue:cyan', gradientangle='270')
		g.attr(label='Turing Machine - '+ self.nombre)
		g.attr("edge", style="filled", color='black:lightgray', gradientangle='270')

		g.attr(rankdir='LR', size='20')
		g.attr('node', shape='doublecircle')

		for i in self.__nodos:
			if i == self.__nodos[len(self.__nodos)-1]:
				g.node(i)
			else:
				g.node(i, shape='circle')

		g.attr("node", shape="circle")

		origen = destino = None
		acum = ""

		for i in self.__listaTrabajo:

			if "-" in i:

				if acum != "":
					g.edge(origen, destino, label=acum)
					acum = ""

				divido = i.split("-")
				origen = divido[0]
				destino = divido[1]

			else:
				acum = acum +"\n"+ i

		g.edge(origen, destino, label=acum)#para cuando se sale de la ultima iteracion del for
		g.render("turingResources/"+self.nombre, None, False, False)

	def generarTuringNodos(self):

		nodos = self.__nodos

		for x in nodos:
			g = Digraph("Turing Machine", filename="TuringMachine.gv", format='png')
			g.attr(bgcolor="purple:pink")
			g.attr('node', shape='circle', style='filled', color='blue:cyan', gradientangle='270')
			g.attr('node', shape='doublecircle', style='filled', color='blue:cyan', gradientangle='270')
			g.attr(label='Turing Machine - '+ self.nombre)
			g.attr("edge", style="filled", color='black:lightgray', gradientangle='270')

			g.attr(rankdir='LR', size='20')
			g.attr('node', shape='doublecircle')

			for i in self.__nodos:
				if i == self.__nodos[len(self.__nodos)-1]:
					
					if i == x:
						g.node(i, color="red")
					else:
						g.node(i)
				else:
					if i == x:
						g.node(i, shape='circle', color = "red")
					else:
						g.node(i, shape='circle')

			origen = destino = None
			acum = ""

			for i in self.__listaTrabajo:

				if "-" in i:

					if acum != "":
						g.edge(origen, destino, label=acum)
						acum = ""

					divido = i.split("-")
					origen = divido[0]
					destino = divido[1]

				else:
					acum = acum +"\n"+ i

			g.edge(origen, destino, label=acum)#para cuando se sale de la ultima iteracion del for
			g.render("turingResources/"+self.nombre+x, None, False, False)

	def generarFlechasNodos(self):
		
		lista = self.__listaTrabajo

		for x in lista:

			if "-" in x:
				g = Digraph("Turing Machine", filename="TuringMachine.gv", format='png')
				g.attr(bgcolor="purple:pink")
				g.attr('node', shape='circle', style='filled', color='blue:cyan', gradientangle='270')
				g.attr('node', shape='doublecircle', style='filled', color='blue:cyan', gradientangle='270')
				g.attr(label='Turing Machine - '+ self.nombre)
				g.attr("edge", style="filled", color='black:lightgray', gradientangle='270')

				g.attr(rankdir='LR', size='20')
				g.attr('node', shape='doublecircle')

				for i in self.__nodos:
					if i == self.__nodos[len(self.__nodos)-1]:
						g.node(i)
					else:
						g.node(i, shape='circle')

				g.attr("node", shape="circle")

				origen = destino = ""
				acum = ""

				for i in self.__listaTrabajo:

					if "-" in i:
						
						if acum != "":

							if x == origen+"-"+destino:
								g.edge(origen, destino, label=acum, color="red")
							else:
								g.edge(origen, destino, label=acum)
							acum = ""

						divido = i.split("-")
						origen = divido[0]
						destino = divido[1]

					else:
						acum = acum +"\n"+ i

				if x == origen+"-"+destino:
					g.edge(origen, destino, label=acum, color="red")
				else:
					g.edge(origen, destino, label=acum)#para cuando se sale de la ultima iteracion del for
				g.render("turingResources/"+self.nombre+x, None, False, False)

	def generarNuevoTuring(self):
		self.verificarRuta()
		self.generarTuring()
		self.generarTuringNodos()
		self.generarFlechasNodos()

	def __labelString(self, lista):
		labels = ""

		for i in lista:
			labels = labels + i + "\n"

		return labels
