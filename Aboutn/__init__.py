from Aboutn import quadrado, quadro, tela

def iniciar (classe=tela.Tela):
	try:
		classe().s.iniciar()
	except AttributeError:
		classe().iniciar()

#if __name__ == "__main__":
#    quadrado.Quadrado().s.iniciar()
#    quadro.Quadro().s.iniciar()
#    tela.Tela().iniciar()