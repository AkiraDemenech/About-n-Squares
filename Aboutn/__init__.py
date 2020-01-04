from Aboutn import quadrado
from Aboutn import quadro
tela = quadrado.tela

print('Tupla de coordenadas dos %d sentidos:'%len(tela.sentidos),tela.sentidos,'\nCoordenadas máximas:\t %d,%d' %(tela.mx,tela.my),'\nDistância máxima:\t',tela.d_max,'\nAptidão máxima: \t',quadrado.f_max,'\nTamanho cromossômico:\t',quadrado.tamanho,'\t(%s)\nTamanho populacional:\t' %quadrado.algarismos,quadro.tamanho)

def iniciar (classe=tela.Tela):
	try:
		classe().s.iniciar()
	except AttributeError:
		classe().iniciar()

#if __name__ == "__main__":
#	iniciar()
#    quadrado.Quadrado().s.iniciar()
#    quadro.Quadro().s.iniciar()
#    tela.Tela().iniciar()
