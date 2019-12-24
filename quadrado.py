import tela
bases 	= "01"
tamanho	=  73

def gerar ():
	return ''

def mutar (c):
	return c

def cruzar (a,b):
	return a+b

def reverter (c):
	try:
		return c.reverse()
	except AttributeError:
		return c[len(c)::-1]

def negativar (c):
	try:
		return -c
	except AttributeError:
		return 

def cromossomo ():
	return

class Quadrado:

	y = x = 0
	s = c = cor = None

	def __ne__ (self,outro):
		return not self.__eq__(outro)
	def __eq__ (self,outro):
		try:
			if None != self.c:
				return self.c == outro.c
	
			return self.y == outro.y and self.x == outro.x #and self.s == outro.s
		except AttributeError:
			return False
		
	def __lt__ (self,outro):
		try:
			if type(outro) != Quadrado:
				return None
			return self.f < outro.f
		except AttributeError:
			return self.y < outro.y or (self.y == outro.y and self.x < outro.x)
		#	return self.c < outro.c
	def __gt__ (self,outro):
		try:
			if type(outro) != Quadrado:
				return None
			return self.f > outro.f
		except AttributeError:
			return self.y > outro.y or (self.y == outro.y and self.x > outro.x)
		#	return self.c > outro.c
	def __ge__ (self,outro):
		return not self.__lt__(outro)
	def __le__ (self,outro):
		return not self.__gt__(outro)

	def __repr__ (self):
		return self.__str__()
	def __str__ (self):
		res = 'Quadrado(%s)' %(self.c.__repr__(), "None, False,%d,%d"%(self.x,self.y))[self.c==None]
		if __name__ != '__main__':
			res = 'quadrado.%s' %res
		return res
	
	def __init__ (self, cromossomo=None, mestra=None,x=0,y=0,cor=None):
		try:
			if type(mestra) != tela.Tela:
				mestra = mestra.s
		except AttributeError:
			mestra = None
		if None==mestra==cromossomo:
			mestra = tela.Tela(self)
		else:
			self.c = cromossomo
		self.x,self.y = x,y
		self.mestra(mestra,cor)

	def __neg__ (self):
		return Quadrado(negativar(self.c),self.s,self.x,self.y,self.cor)

	def reverse (self):
		return Quadrado(reverter(self.c),self.s,self.x,self.y,self.cor)

	def mestra (self,mestra=None,cor=None):
		if None != cor:
			self.cor = cor
		if None == mestra:
			return self.s
		self.s = mestra