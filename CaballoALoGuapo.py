#########################################################################################
## Autor: Cantarell Maximiliano														#####
## Version: 1.0 																	#####
## Descripcion: Calcular movimientos de un caballo para recorrer todo el tablero	#####
#########################################################################################

class Tablero:
	tablero=[] #Posee todos los casilleros posibles en forma de tupla (x, y)
	pisadas=[] #Posee todos los movimientos en el orden echo. 
	fin= False
	maximo=0

	def __init__(self,x,y):
		for i in range(1,x+1):
			for j in range(1,y+1):
				self.tablero.append( (i,j) )

	def mostarPosiciones(self):
		for posicion in self.tablero:
			print posicion

	def moverA(self,posicion):
		self.pisadas.append(posicion)
		if len(self.pisadas)>self.maximo:
			print "Nuevo maximo: "+str(len(self.pisadas))
			self.maximo=len(self.pisadas)
		if len(self.pisadas) == len(self.tablero):
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
	tablero = Tablero(8,8) #Dimensiones del tablero

	def __init__(self,x,y):	#Posicion inicial del Caballo
		self.posicionActual=(x,y)
		
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

	def guardarEnTxt(self):
		archivo = open("movimientos.txt", "a")		 
		archivo.writelines(str(self.tablero.pisadas))

	def imprimirPasos(self):
		print "Al FIIIIN, estos son los pasos: "
		print self.tablero.pisadas

	def correrPrueba(self):
		self.saltar(self.posicionActual)
		print "No existe secuencia posible."

	def saltar(self,movimiento):
		self.tablero.moverA(movimiento)

		if self.tablero.termino():
			self.imprimirPasos()
			self.guardarEnTxt()
			exit(0)

		posiblesPasos=[]
		posiblesPasos=self.generarListaDePosiblesPasos(movimiento)

		for paso in posiblesPasos:
			self.saltar(paso)
			self.tablero.desmarcar(paso)


caballito = Caballo(5,5)
caballito.correrPrueba()