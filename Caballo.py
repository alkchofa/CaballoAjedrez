#########################################################################################
## Autor: Cantarell Maximiliano														#####
## Version: 1.0 																	#####
## Descripcion: Calcular movimientos de un caballo para recorrer todo el tablero	#####
#########################################################################################

class Tablero:
	tablero=[]
	pisadas=[]
	fin= False

	def __init__(self):
		for i in range(1,9):
			for j in range(1,9):
				self.tablero.append( (i,j) )

	def mostarPosiciones(self):
		for posicion in self.tablero:
			print posicion

	def moverA(self,posicion):
		self.pisadas.append(posicion)
		if len(self.pisadas) == 64:
			self.fin = True

	def desmarcar(self,posicion):
		self.pisadas.remove(posicion)

	def estaDisponible(self,posicion):
		return self.pisadas.count(posicion) == 0

	def existe(self,posicion):
		return self.tablero.count(posicion) == 1

	def termino(self):
		return self.fin

class Caballo:
	listaDePasos=[]
	tablero = Tablero()

	def __init__(self,x,y):	
		self.posicionActual=(x,y)
		self.listaDePasos.append(self.posicionActual)
		
	def generarListaDePosiblesPasos(self,(x,y)):
		## Esto es asqueroso, perdon D:
		listaAuxiliar=[]
		listaFinal=[]
		listaAuxiliar.append((x-2,y-1))
		listaAuxiliar.append((x-2,y+1))
		listaAuxiliar.append((x+2,y-1))
		listaAuxiliar.append((x+2,y+1))
		listaAuxiliar.append((x-1,y+2))
		listaAuxiliar.append((x+1,y+2))
		listaAuxiliar.append((x+1,y-2))
		listaAuxiliar.append((x-1,y-2))

		for posicion in listaAuxiliar:
			if self.tablero.existe(posicion) and self.tablero.estaDisponible(posicion):
				listaFinal.append(posicion)

		return listaFinal

	def imprimirPasos(self):
		print "Al FIIIIN, estos son los pasos: "
		for pasos in listaDePasos:
			print pasos

	def saltar(self):
		if self.tablero.termino():
			self.imprimirPasos()
			exit(0)

		posiblesPasos=self.generarListaDePosiblesPasos(self.posicionActual)

		for paso in posiblesPasos:
			self.tablero.moverA(paso)
			print "Me muevo a "+ str(paso)
			self.posicionActual=paso
			self.saltar()
			self.tablero.desmarcar(paso)
			print "Quito a "+ str(paso)


caballito = Caballo(1,1)
caballito.saltar()