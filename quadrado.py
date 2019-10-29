"""
"""
bases 	= "01"
tamanho	= 73

class Quadro:
	def __str__ (self):
		res = 'Quadrado()'
		if __name__ != '__main__':
			res = 'quadrado.%s' %res
		return res

	def __repr__ (self):
		return self.__str__()

def gerar ():
	return ''

def mutar (c):
	return c

def cruzar (a,b):
	return a+b

def cromossomo ()