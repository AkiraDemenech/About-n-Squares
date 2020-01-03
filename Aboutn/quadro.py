from Aboutn import quadrado

def popular (n=0,p=None):
	if p == None:
		p = []
	while len(p) < n//4:
		p.append(quadrado.gerar(quadrado.Quadrado))
	for q in (quadrado.reverter,quadrado.negativar):
		m = len(p)
		while m > 0:
			m -= 1
			p.append(q(p[m]))
	while len(p) < n:
		p.append(quadrado.gerar(quadrado.Quadrado))
	return p

def sortear (p,n=range(2)):
	p.sort()
	c = len(p)
	while c > 0:
		r = []
		f = p.f
		for d in n:
			d = 0
			a = quadrado.tela.random() * f
			while True:
				if not d in r:
					if a < p.populacao[d].f:
						break
					a -= p.populacao[d].f
				d += 1
			f -= p.populacao[d].f
			r.append(d)
		yield r
		c -= 1

class Quadro:

	populacao = s = f = None

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
	def __iadd__ (self,o):
		self.populacao += list(o)#.populacao
		return self
	def __imul__ (self,o):
		self.populacao *= o
		return self
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
	
	def __init__ (self, mestra=None, populacao=None):#16):#2):
		if type(mestra) in (Quadro,quadrado.Quadrado):
			if populacao == None:
				try:
					populacao = mestra.populacao
				except AttributeError:
					if mestra.s != None and mestra.s.n != None:
						populacao = mestra.s.n.populacao
			mestra = mestra.s
		if not type(populacao) in (list,tuple,set):
			if populacao == None:
				populacao = 16
			populacao = popular(populacao)
		elif type(populacao) != list:
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

	def continuar (self):
		self.pausar()
		t = []
		for x,y in sortear(self):
			print(x,y)
			t.append(quadrado.cruzar(self.populacao[x],self.populacao[y]))
		t.append(self.populacao[0])
		t,self.populacao = self.populacao,t
		self.mestra()
		self.s.q.ir(para=(quadrado.tela.qx,quadrado.tela.qy),permissao=True)
		self.s.continuar(len(self)%2==1,t)
		self.iniciar()
		print(len(self),'em campo.')
	
	def reiniciar (self,event=False):
		self.pausar()
		self.populacao.clear()
		self.__init__(self.s)
		print(len(self),'novos quadrados gerados')
		if event:
			self.iniciar()
	
	def iniciar (self):
		if self.s.q in self:
			self.reiniciar(True)
		self.s.q.iniciar()
		for q in self:#.populacao:
			q.iniciar()

	def pausar (self):
		self.s.q.pausar()
		for q in self:#.populacao:
			q.pausar()

	def avaliar (self):
		self.f = 0
		for ind in self:#.populacao:
			self.f += ind.avaliar()
		return self.f

	def sort (self,decrescente=True,naoavalie=False):
		if not naoavalie:
			self.avaliar()
		self.populacao.sort()
		if decrescente:
			self.reverse()
	
	def reverse (self):
		self.populacao.reverse()
