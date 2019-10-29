class Quadro:
	def __str__ (self):
		res = 'Quadro()'
		if __name__ != '__main__':
			res = 'quadro.%s' %res
		return res

	def __repr__ (self):
		return self.__str__()