class Pila():
	def __init__(self):
		self.datos = []

	def apilar(self, dato):
		self.datos.append(dato)

	def sacarPila(self):
		try:
			return self.datos.pop()

		except:
			raise ValueError("La pila esta vacia")

	def isEmpty(self):
		return self.datos == []

	def cantidadDatos(self):
		return len(self.datos)