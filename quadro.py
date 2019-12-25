import quadrado

def popular (n=0,p=[]):
	return p

class Quadro:

	populacao = []
	s = None

	def __contains__ (self,algo):
		return self.populacao.__contains__(algo)
	def __eq__ (self,outro):
		try:
			return self.populacao.__eq__(outro.populacao) #and self.s == outro.s
		except Exception:
			return False
	def __ne__ (self,outro):
		return self.__lt__(outro) or self.__gt__(outro) #self.populacao.__ne__(outro.populacao)
	def __le__ (self,o):
		try:
			return self.__eq__(o) or self.populacao.__lt__(o.populacao)
		except AttributeError:
			return NotImplemented
	def __ge__ (self,o):
		try:
			return self.__eq__(o) or self.populacao.__gt__(o.populacao)
		except AttributeError:
			return NotImplemented
	def __gt__ (self,o):
		return not self.__le__(o)
	def __lt__ (self,o):
		return not self.__ge__(o)
	def __add__ (self,o):
		return Quadro(self.s,self.populacao+list(o))#.populacao
	def __mul__ (self,o):
		return Quadro(self.s,self.populacao*o)
	def __len__ (self):	
		return self.populacao.__len__()
	def __repr__ (self):
		return self.__str__()
	def __str__ (self):
		res = 'Quadro(populacao=%s)' %self.populacao.__repr__()
		if __name__ != '__main__':
			res = 'quadro.%s' %res
		return res
	def __iter__ (self):
		return self.populacao.__iter__()
	
	def __init__ (self, mestra=None, populacao=2):
		if not type(populacao) in (list,tuple,set):
			popular(populacao, self.populacao)
		else:
			if type(populacao) != list:
				populacao = list(populacao)
			self.populacao = populacao
		self.mestra(mestra)
		if mestra == None:
			mestra = quadrado.tela.Tela(None,self)

	def mestra (self, mestra=None):
		if None == mestra:
			mestra = self.s
			if None == self.s:
				return
		else:
			self.s = mestra
			if None == mestra.q:
				self.s.protagonista(quadrado.Quadrado(mestra=mestra))

		if type(self.populacao) in (set,tuple,list):
			if type(self.populacao) != list:
				self.populacao = list(self.populacao)
		c = len(self.populacao)
		while c > 0:
			c += -1
			if type(self.populacao[c]) != quadrado.Quadrado:
				self.populacao[c] = quadrado.Quadrado(self.populacao[c])
			self.populacao[c].mestra(mestra,quadrado.tela.PRE)
		