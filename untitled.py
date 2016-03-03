class Persona:

	def _init_(self,estatura,nombre):
		self.nombre = nombre
		self.estatura = estatura

	@property.setter
	def estatura(self, estatura):
		if estatura> 2:
			estatura = 2
		self.estatura = estatura

	@property
	def estatura(self):
	    return self.estatura
	


