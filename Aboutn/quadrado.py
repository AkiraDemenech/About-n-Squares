
try:
#	import warnings
	import tela
except ImportError:
	from Aboutn import tela

representacao= (5,) + ((4,) * (len(tela.sentidos) + 1))
algarismos	 = "01"#'ai'#' \t'
f_max	= 100
tamanho	=   0 #73 == 5 + (4 * (len(tela.sentidos) + 1))

def __len__ ():
	global tamanho
	for r in representacao:
		tamanho += r
	return tamanho

def verificar (*ind):
	e = 0
	for i in ind:
		try:
			if i.erro == None or i.verificar():
				e += 1
		except AttributeError:
			if i == None or len(i) != tamanho:
				e += 1
	return e

def gerar (tipo=str):
	if tipo==str:
		c = ''
		d = tamanho
		while d > 0:
			d -= 1
			c += algarismos[int(len(algarismos)*tela.random())]
		return c
	return tipo(gerar())

def mutar (c):
	return c

def cruzar (a,b):
	try:
		c = 1 + int(tela.random() * (tamanho - 2))
		return a[:c] + b[c:]
	except TypeError:
		if type(a) == str:
			return b + a
		#	a, b = b, a
		return a + b

def reverter (c):
	try:
		return c.reverse()
	except AttributeError:
		return c[len(c)::-1]

def negativar (c):
	try:
		return -c#.__neg__()
	except TypeError:
		a = ''
		for b in c.__str__():
			try:
				a += algarismos[len(algarismos) - (algarismos.find(b) + 1)]
			except IndexError:
				a += b			
		return a

def decimal (b):
#	if type (b) != str:
#		b = str(b)
	a = c = 0
	while c < len(b):
		if not b[c] in algarismos:
			print('Dígito %s sem valor em %s' %(b[c],b))
			#warnings.warn('Dígito %s sem valor em %s' %(b[c],b),SyntaxWarning)
		a = (a*len(algarismos)) + algarismos.find(b[c])
		c += 1
	return a

class Quadrado:

	y = x = 0
	f = s = c = cor = erro = correr = None

	def __ne__ (self,outro):
		return not self.__eq__(outro)
	def __eq__ (self,outro):
		try:
			if None != self.c and outro.c != None:
				return self.c == outro.c
	
			return self.y == outro.y and self.x == outro.x #and self.s == outro.s
		except AttributeError:
			#print('Não sou None!')
			return False
		
	def __lt__ (self,outro):
		try:
			if type(outro) != Quadrado:
				return None
			return self.f < outro.f
		except TypeError:
			return self.y < outro.y or (self.y == outro.y and self.x < outro.x)
		#	return self.c < outro.c
	def __gt__ (self,outro):
		try:
			if type(outro) != Quadrado:
				return None
			return self.f > outro.f
		except TypeError:
			return self.y > outro.y or (self.y == outro.y and self.x > outro.x)
		#	return self.c > outro.c
	def __ge__ (self,outro):
		return not self.__lt__(outro)
	def __le__ (self,outro):
		return not self.__gt__(outro)
	def __len__ (self):
		try:
			return self.c.__len__()
		except AttributeError:
			return -1
	def __iter__ (self):
		try:
			return self.c.__iter__()
		except AttributeError:
			return NotImplemented
	def __contains__ (self,gene):
		try:
			return self.c.__contains__(gene)
		except AttributeError:
			return None
	
	def __repr__ (self):
		return self.__str__()
	def __str__ (self):
		if None==self.c:
			res = "None, False,%d,%d"%(self.x,self.y)
		else:
			res = self.c.__repr__()#'"%s"' %self.c
			if self.f != None:
				res += ', x=%d,y=%d, apto=%f' %(self.x, self.y, self.f)
		res = 'Quadrado(%s)' %res
		if __name__ != '__main__':
			res = 'quadrado.%s' %res
		return res
	
	def __init__ (self, cromossomo=None, mestra=None,x=None,y=None,cor=None,apto=None):
		while type(cromossomo) == Quadrado:
#			if self.erro == None:
#				self.erro = cromossomo.erro
			if apto == None:
				try:
					apto = cromossomo.f
				except AttributeError:
					pass
			if None == x:
				x = cromossomo.x
			if None == y:
				y = cromossomo.y
			if None == cor:
				cor = cromossomo.cor
			if None == mestra:
				mestra = cromossomo.s
			cromossomo = cromossomo.c
		try:
			if type(mestra) != tela.Tela:
				mestra = mestra.s
		except AttributeError:
			mestra = None
		if None==mestra==cromossomo:
			mestra = tela.Tela(self)
			if None==x:
				x = tela.qx
			if None==y:
				y = tela.qy
		else:
#			if None==cromossomo:
#				cromossomo = gerar()
#			else:
#				self.__len__ = self.c.__len__
#				self.__contains__ = self.c.__contains__
			self.c = cromossomo
		self.mestra(mestra,cor)
		if self.analisar() and apto != None:
			self.f = apto
		if y != None:
			self.y = y
		if x != None:
			self.x = x

	def __abs__ (self):
		return decimal(self.c)#.__abs__()

	def __add__ (self,outro):
		if verificar(self,outro):#self.verificar() or Quadrado(outro).verificar():
			print('Cruzamento inválido')
			return None

		try:
			c = cruzar(self.c,outro.c)
		except AttributeError:
			c = cruzar(self.c,outro)
		return Quadrado(c,self.s,cor=self.cor)
	#	return Quadrado(c,self.s,self.x,self.y,self.cor)

	def __neg__ (self):
		return Quadrado(negativar(self.c),self.s,cor=self.cor)

	def reverse (self):
		return Quadrado(reverter(self.c), self.s,cor=self.cor)

	def index (self,gene):
		return self.c.index(gene)
	def find (self, gene):
		try:
			return self.c.find(gene)
		except AttributeError:
			return -2
	def count (self,gene):
		try:
			return self.c.count(gene)
		except AttributeError:
			return  0

	def copy (self):
		return Quadrado(self.c,self.s,cor=self.cor)

	def mestra (self,mestra=None,cor=None):
		if None != cor:
			self.cor = cor
		if None == mestra:
			return self.s
		self.s = mestra

	def verificar (self):
		return self.erro or self.c == None or len(self.c) != tamanho

	def analisar (self):
#		while type(self.c) == Quadrado:
#			self.c = self.c.c
		if self.verificar():
			#print(self,':',self.c,'inválido como Cromossomo')
			return None#NotImplemented
		r = 0
		rotas = []
		for l in representacao:
			#print(self.c[r:r+l],decimal(self.c[r:r+l]))
			rotas.append(decimal(self.c[r:r+l]))
			r += l
		self.x = rotas.pop(0)
		self.y = rotas.pop(0)
		self.rotas = {}
		r = len(tela.sentidos)#rotas
		try:
			while r > 0:
				r += -1
				self.rotas[tela.sentidos[r]] = tela.sentidos[rotas[r]]
		except Exception:
			self.erro = True
		else:
			self.erro = False
		finally:
			return not self.erro

	def avaliar (self):
		try:
		#	d = ((self.y-self.s.q.y)**2 + (self.x-self.s.q.x)**2)**(1/2)
			self.f = f_max*(1-((((self.y-self.s.q.y)**2 + (self.x-self.s.q.x)**2)**(1/2))/tela.d_max))
		#	self.f = 100*(1-((((self.y-self.s.q.y)**2 + (self.x-self.s.q.x)**2)**(1/2))/tela.d_max))
		#	self.f = (101**(1-(d/d_max))) - 1
		#	self.f = (101/(101**(d/d_max)))-1
		except AttributeError:
			self.f = 0
			print(str(self) + '.avaliar(): Mestra, seu Protagonista ou as Coordenadas do último não encontrado(a)(s)')
			#warnings.warn(str(self) + '.avaliar(): Mestra, seu Protagonista ou as Coordenadas do último não encontrado(a)(s)',RuntimeWarning)
			#RuntimeWarning('Mestra, seu Protagonista ou as Coordenadas do último não encontrado(a)(s)')
		return self.f
	
	def localizar (self):
		try:
			coord = [self.x - self.s.q.x, self.y - self.s.q.y]
			z = len(coord)
			while z > 0:
				z += -1
				if coord[z] < -2:
					coord[z] = -2
				if coord[z] > 2:
					coord[z] = 2
			return tuple(coord)
		except AttributeError:
			print(str(self) + '.localizar(): Mestra, seu Protagonista ou as Coordenadas do último não encontrado(a)(s)')

	def mover (self,dex=0,dey=0):
		i = self.s.colorir(dex,dey)
		j = self.s.colorir(self.x,self.y,self.cor)
		return i and j

	def ir (self,dx=None,dy=None,para=None,permissao=False):
		if not (self.correr or permissao):
			return None

		if para == None:
			try:
				if None==dx==dy:
					dx,dy = self.rotas[self.localizar()]
			except KeyError:
				dy=dx = 0
			#	dx,dy = tela.sentidos[int(len(tela.sentidos)*tela.random())]
				#print('No ponto cego de',str(self))

			self.x,dx = self.x+dx,self.x
			self.y,dy = self.y+dy,self.y
		else:
			try:
				dx,dy = self.x,self.y
				self.x,self.y = para[:2]
			except TypeError:
				pass
			except ValueError:
				pass
			
		if self.y >= tela.my:
			self.y = tela.my - 1
		if self.x >= tela.mx:
			self.x = tela.mx - 1
		if self.x < 0:
			self.x = 0
		if self.y < 0:
			self.y = 0

		if not (self.mover(dx,dy) or permissao):
			#print('Movimentação de',self,'não concluída.')
			return False
		return True

#	def travar (self,v=True):
#		self.vencido = v

	def andar (self):
		while self.s.n.correr and self.correr and self.ir():
			if self.s.q == self:
				self.s.n.continuar(self)
			tela.sleep(0.55 + tela.random())
		#print(self,'parou de andar.')

	def iniciar (self):
		self.correr = True
		if self.c != None:
			tela.Thread(None,self.andar,str(self)).start()

	def pausar (self):
		self.correr = False
