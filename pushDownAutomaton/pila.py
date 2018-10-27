class Pila():
	def __init__(self):
		self.datos = []

	def apilar(self, dato):
		self.datos.append(dato)

	def sacarPila(self):
		try:
			return self.datos.pop()

		except:
			return None

	def isEmpty(self):
		return self.datos == []

	def cantidadDatos(self):
		return len(self.datos)

	def verTope(self):
		tope = self.sacarPila()

		if tope != None:
			self.apilar(tope)
			
		return tope