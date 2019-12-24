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

mx,my	=	32,16
teto = mx,my
quadrados = []
quad 	= [mx//2,my//2]
vence 	= [0,0]
qtd 	= 2
f_max	= 100
d_max	= ((mx-1)**2 + (my-1)**2)**(1/2)

print('Lista de coordenadas dos %d sentidos:'%len(sentidos),sentidos,'\nCoordenadas máximas: %d,%d' %teto,'\nDistância máxima:',d_max)

 #	aptidão
def avaliar (d,g=None): 
	global quad
	if g == None:
		global d_max
		global f_max
		return f_max*(1-(d/d_max))
	return avaliar(((d-quad[0])**2 + (g-quad[1])**2)**(1/2))
'''
c = d_max
while c >= 0:
	print(c,avaliar(c))
	c -= 1
c = 0
while c <= d_max:
	print(c,avaliar(c))
	c += 1
'''
def gerar ():
	return [int(mx*random()),int(my*random())]

def andar (*coord):
	quadrados[quad[1]][quad[0]].config(**BRA)
	c = 0
	try:
		while len(coord)>c:
			if teto[c] > coord[c] and coord[c] >= 0:
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
	global BRA
	global PRE
	global PRETO
	global BRANCO

	if b != None:
		while len(bots) > 0 and not quad in bots:
			quadrados[b[1]][b[0]].config(**BRA)
			dv = sentidos[int(random()*len(sentidos))]
			c = len(b)
			while c > 0:
				c	+= -1
				b[c]+= dv[c]
				if b[c] < 0:
					b[c] = 0
				if b[c] >= teto[c]:
					b[c] = teto[c] - 1
			quadrados[b[1]][b[0]].config(**PRE)
			print(b,avaliar(*b))
			if b != quad:
				sleep((11/12)-(random()/8))
			if b == quad:
				print('\a\t',b)
				bots.clear()
				qtd += 1#= len(bots) + 1
				vence,quad = b,[mx//2,my//2]
				sleep((12/11)+(random()/4))
				ativar(quadrados)
				return
		quadrados[b[1]][b[0]].config(**BRA)
		BRANCO,BRA,PRE,PRETO = PRETO,PRE,BRA,BRANCO
		return
	
	b = vence
	c = qtd
	while c>0:	
		if b != quad:
			bots.append(b)
		b = gerar()
		c -= 1
	if len(bots) < 2:
		b = bots
		cuidar(bots=b)
		print("Ação de emergência utilizada")
	else:
		print(len(bots),bots)
	for b in bots:
		Thread(None, lambda: cuidar(b,bots)).start()
	
a = Tk()
#a.config(bg='WHITE')
a.title("About 2") #a História de n Quadrados
#a.attributes('-fullscreen', True)
#a.geometry('%dx%d' %(a.winfo_screenwidth()//2, a.winfo_screenheight()//2))
#b = {'width':a.winfo_screenwidth()//9,'height':a.winfo_screenheight()//8,'master':a}
#b = Frame(**b),Frame(**b)
b = [Label(a,text="\n\n")]
b.extend((Button(a,command=lambda destruir=b: iniciar(a,mx,my,*destruir,botoes=quadrados),**VER,text=VERMELHO), Button(a,command=a.quit,bg=PRETO,text="n")))
b[1].pack(side=RIGHT)
b[2].pack()
b[0].pack()
b = '0123456789ABCDEF'
c = 0
while c < len(sentidos):
	for d in (b[c]*2).title():
		a.bind(d,lambda event,x=sentidos[c][0],y=sentidos[c][1]: andar(quad[0]+x,quad[1]+y))
	c += 1
#Thread(None, xadrez, None, (a,)).start()
#Thread(None, ).start()
a.mainloop()