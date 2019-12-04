"""
ATENÇÃO: ESTE CÓDIGO ESTÁ BUGADO
PRA CARAMBA

TODOS OS QUADRADOS PRETOS, QUANDO UM ÚNICO ALCANÇA O VERMELHO,
DESTROEM E RECONTROEM A MESMA POPULAÇÃO AO MESMO TEMPO,
UM BUG INCRÍVEL DA MASSA DESVAIRADA

PARA APRECIAÇÃO PROPOSITAL DO ERRO.

"""

from tkinter import BOTH, RIGHT, LEFT, Tk, Frame, Button, Label
from threading import Thread
from time import sleep, time
from random import random

VERMELHO='RED'; 	VER = {"bg":VERMELHO,"fg":VERMELHO}
BRANCO = 'WHITE'; 	BRA = {"bg": BRANCO, "fg":BRANCO}
PRETO  = 'BLACK'; 	PRE = {"bg": PRETO, "fg": PRETO}

#	diferença entre x,y da coisa relativa e do objeto de origem (ex: player relativo ao bot)
	#		(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1),(2,0),(2,2),(0,2),(-2,2),(-2,0),(-2,-2),(0,-2),(2,-2)
sentidos = [(1,0),(1,1),(0,1),(-1,1)]
for i in (-1,2):
	j,k = 0,len(sentidos)
	while j < k:
		sentidos.append((sentidos[j][0]*i,sentidos[j][1]*i))
#		print(sentidos[len(sentidos)-1])
		j += 1
print('Lista de coordenadas dos %d sentidos:'%len(sentidos),sentidos)

mx,my	=	32,16
teto = mx,my
quadrados = []
quad 	= [mx//2,my//2]
vence 	= [0,0]
qtd 	= 2#10+int(5*random())

def andar (*coord):
	quadrados[quad[1]][quad[0]].config(**BRA)
	c = 0
	try:
		while len(coord)>c:
			quad[c] = coord[c]
			c += 1
	except Exception:
		pass
	quadrados[quad[1]][quad[0]].config(**VER)

def xadrez (mestre, c=8,h=None,espera=0,matriz=[],funcao=None,ligue=False):
	mestre = Frame(mestre)
	mestre.pack(fill=BOTH)
	t = time()
	if (h==None):
		h = c
	y = h
	while y>0:
		x = c
		m = Frame(mestre)
		m.pack(fill=BOTH)
		matriz.insert(0,[])
		while x>0:
		#	l = Frame(m,width=mestre.winfo_screenwidth()//n,height=mestre.winfo_screenheight()//n)
		#	l.pack()
			matriz[0].insert(0,Button(m,text=(x,y),command=funcao))
			matriz[0][0].pack(fill=BOTH, side=RIGHT)
			matriz[0][0].coord = x,y
			matriz[0][0].ir = lambda col=x-1,lin=y-1: andar(col,lin)#matriz[lin][col].config(**VER)#print(pos)
		#	print(x,y)
			sleep(espera/(x*y))
			x -= 1
		y -= 1

	if ligue:
		t = time() - t
		mestre.master.title("About n []")
		print ('Espera máxima:\t%f\nTempo total:\t%f\nTempo médio:\t%f\nTotal:\t%d botões\n'%(espera,t,t/(h*c),c*h))
		ativar(matriz)
	return matriz

def iniciar (mestre, x=16,y=None,*imolados,tempo=1/13,botoes=[]):
	for i in imolados:
		try:
			i.destroy()
		except Exception:
			print('\t\aNão foi possível destruir o elemento',i)
	Thread(None, xadrez, None, (mestre,x,y,tempo,botoes,None,True)).start()
	print ('Tupla de objetos destruídos:',imolados)
	mestre.title("About n")

def ativar (tabuleiro):
	try:
		for l in tabuleiro:
			for c in l:
				c.config(**BRA,command=c.ir)#lambda pos=c.coord: print(pos))
			c.master.config(bg=BRANCO)
		c.master.master.config(bg=BRANCO)
		c.master.master.master.config(bg=BRANCO)
		c.master.master.master.title ("About n [Squares]")
	except Exception:
		print("\t\aUm erro ocorreu na construção da tela branca, no caso de permanência do cinza claro padrão em algum elemento, por favor, repita esta operação.")

	cuidar()

def cuidar (b=None,bots=[]):
	global vence
	global quad
	global qtd

	if b != None:
		while len(bots) > 0 and not quad in bots:
			quadrados[b[1]][b[0]].config(**BRA)
			dv = sentidos[int(random()*len(sentidos))]
			for c in range(2):
				b[c] += dv[c]
				if b[c] < 0:
					b[c] = 0
				if b[c] >= teto[c]:
					b[c] = teto[c] - 1
			quadrados[b[1]][b[0]].config(**PRE)
			sleep((11/12)-(random()/8))
		#if b != quad:
		#	return

		bots.clear()
		qtd += 1
		vence,quad = quad,[mx//2,my//2]
		sleep((12/11)+(random()/4))
		ativar(quadrados)
		return
	
	bots.append(vence)
	for contador in range(qtd):
		bots.append([int(mx*random()),int(my*random())])
	for b in bots:
		Thread(None, lambda: cuidar(b,bots)).start()
	print(qtd,bots)
	
a = Tk()
#a.config(bg='WHITE')
a.title("About 2") #a História de n Quadrados
#a.attributes('-fullscreen', True)
#a.geometry('%dx%d' %(a.winfo_screenwidth()//2, a.winfo_screenheight()//2))
#b = {'width':a.winfo_screenwidth()//9,'height':a.winfo_screenheight()//8,'master':a}
#b = Frame(**b),Frame(**b)
b = [Label(a,text="\n\n")]
b.extend((Button(a,command=lambda: iniciar(a,mx,my,*b,botoes=quadrados),**VER,text=VERMELHO), Button(a,command=a.quit,bg=PRETO,text="n")))
b[1].pack(side=RIGHT)
b[2].pack()
b[0].pack()
#Thread(None, xadrez, None, (a,)).start()
#Thread(None, ).start()
a.mainloop()