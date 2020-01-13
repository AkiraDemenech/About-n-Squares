try:
	import quadrado, quadro
except ImportError:
	from Aboutn import quadrado
	from Aboutn import quadro
tela = quadrado.tela
quadro.__len__()
quadrado.__len__()

print('Tupla de coordenadas dos %d sentidos:'%len(tela.sentidos),tela.sentidos,'\nCoordenadas máximas:\t %d,%d' %(tela.mx,tela.my),'\nDistância máxima:\t',tela.d_max,'\nAptidão máxima: \t',quadrado.f_max,'\nTamanho cromossômico:\t',quadrado.tamanho,'\t(%s)\nTamanho populacional:\t' %quadrado.algarismos,quadro.tamanho)

def iniciar (classe=tela.Tela, fechar=True):
	try:
		classe().s.iniciar(x=fechar)
	except AttributeError:
		classe().iniciar(x=fechar)

def start (**argumentos):
	iniciar(**argumentos)

if __name__ == "__main__":
	start(fechar=False)	# ALT+END para Fechar
#	iniciar()
#    quadrado.Quadrado().s.iniciar()
#    quadro.Quadro().s.iniciar()
#    tela.Tela().iniciar()
