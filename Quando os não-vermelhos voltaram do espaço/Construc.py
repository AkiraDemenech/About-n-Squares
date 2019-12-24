from random import random as rand
from threading import Thread
from time import sleep
from tkinter import *

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
#print(str(sentidos).replace(' ',''))

def xadrez (mestre, x=8,y=None,espera=0,matriz=[],funcao=None):
	mestre = Frame(mestre)
	mestre.pack(fill=BOTH)
	n = x
	if (y==None):
		y = x
	while y>0:
		m = Frame(mestre)
		m.pack(fill=BOTH)
		matriz.insert(0,[])
		while x>0:
		#	l = Frame(m,width=mestre.winfo_screenwidth()//n,height=mestre.winfo_screenheight()//n)
		#	l.pack()
			matriz[0].insert(0,Button(m,text=(x,y),command=funcao))
			matriz[0][0].pack(fill=BOTH, side=RIGHT)
			matriz[0][0].coord = x,y
			if rand() > 1/2:
				matriz[0][0].ir = lambda lin=x-1,col=y-1: matriz[col][lin].config(**VER)#print(pos)
			else:
				matriz[0][0].ir = lambda lin=x-1,col=y-1: matriz[col][lin].config(**PRE)#print(pos)
		#	print(x,y)
			sleep(espera/(x*y))
			x -= 1
		y -= 1
		x = n
	return matriz

def iniciar (mestre, x=16,y=None,*imolados,tempo=0.55,botoes=[]):
	for i in imolados:
		try:
			i.destroy()
		except Exception:
			print('\t\aA destruição de %s não foi possível!'%str(i))
	Thread(None, xadrez, None, (mestre,x,y,tempo,botoes,lambda:ativar(botoes))).start()
	mestre.title("About n")
	print(imolados)

def ativar (tabuleiro):
	try:
		for l in tabuleiro:
			for c in l:
				c.config(**BRA,command=c.ir)#lambda pos=c.coord: print(pos))
			c.master.config(bg=BRANCO)
		c.master.master.config(bg=BRANCO)
		c.master.master.master.config(bg=BRANCO)
		c.master.master.master.title("About n [Squares]")
	except Exception:
		print("Um erro ocorreu na construção da tela branca, no caso de permanência do cinza claro padrão em algum elemento, por favor, repita esta operação.")

a = Tk()
#a.config(bg='WHITE')
a.title("About 2") #a História de n Quadrados
#a.attributes('-fullscreen', True)
#a.geometry('%dx%d' %(a.winfo_screenwidth()//2, a.winfo_screenheight()//2))
b = {'width':a.winfo_screenwidth()//9,'height':a.winfo_screenheight()//8,'master':a}
b = Frame(**b),Frame(**b)
Button(b[1],command=lambda: iniciar(a,32,16,*b),bg=VERMELHO).pack(fill=BOTH)
Button(b[0],command=a.quit, bg=PRETO).pack(fill=BOTH)
b[0].pack(side=RIGHT)
b[1].pack()
#Thread(None, xadrez, None, (a,)).start()
a.mainloop()
