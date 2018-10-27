class TuringMachine():

	def __init__(self, estadoInicial, estadosFinales, transiciones):
		self.estadoInicial = estadoInicial
		self.estadosFinales = estadosFinales
		self.estadoActual = estadoInicial
		self.transiciones = transiciones
		self.cadena = []
		self.proceso = []
		self.terminado = False
		self.posCabeza = 0

	def setTransiciones(self, transiciones):
		self.transiciones = transiciones

	def setCadena(self, cadena):
		self.terminado = False
		self.cadena = self.__convertirCadena(cadena)
		self.proceso = []
		self.posCabeza = 0
		self.estadoActual = self.estadoInicial

	def __convertirCadena(self, cadena):
		
		lista = []

		for i in cadena:
			lista.append(i)

		return lista

	def evaluarLetra(self):

		if self.cadena != [] and self.acabarProceso() == False:

			if self.posCabeza > (len(self.cadena)-1) or self.posCabeza < 0:
				letra_en_cabeza = "□"
			else:
				letra_en_cabeza = self.cadena[self.posCabeza]

			regla_origen = (self.estadoActual, letra_en_cabeza)

			if regla_origen in self.transiciones:

				regla_destino = self.transiciones[regla_origen]

				if self.posCabeza > (len(self.cadena)-1) or self.posCabeza < 0:
					pass
				else:
					self.cadena[self.posCabeza] = regla_destino[1]

				if regla_destino[2] in ["R", "r"]:
					self.posCabeza += 1
				elif regla_destino[2] in ["L", "l"]:
					self.posCabeza -= 1

				self.proceso.append([self.estadoActual+"-"+regla_destino[0], regla_origen, regla_destino])
				cambio = [self.estadoActual, regla_destino[0]]
				self.estadoActual = regla_destino[0]

				regla = str(regla_origen)+" : "+str(regla_destino)#PARA IMPLEMENTACION GRAFICA
				regla = regla.replace("'","")
				return regla_destino[1], regla_destino[2], cambio, regla#PARA IMPLEMENTACION GRAFICA

			self.terminado = True
		return None, None, None, None

	def acabarProceso(self):
		
		if self.estadoActual in self.estadosFinales or self.terminado == True:
			self.terminado = True
			return True
		else:
			return False

	def evaluarCadena(self):
		while T1.acabarProceso() == False:
			T1.evaluarLetra()

"""
transiciones = {
				("q1", "a"):("q1", "a", "R"),
				("q1", "b"):("q1", "a", "R"),
				("q1", "□"):("q2", "□", "L"),
				("q2", "a"):("q2", "a", "L"),
				("q2", "□"):("q3", "□", "R"),
				}

T1 = TuringMachine("q1", ["q3"], transiciones)
T1.setCadena("abba")
T1.evaluarCadena()
"""