from threading import Thread
from time import sleep
from tkinter import *

def xadrez (mestre, x=8,y=None,espera=0):
	matriz,n = [],x
	if (y==None):
		y = x
	while y>0:
		m = Frame(mestre)
		m.pack(fill=BOTH)
		matriz.insert(0,[])
		while x>0:
		#	l = Frame(m,width=mestre.winfo_screenwidth()//n,height=mestre.winfo_screenheight()//n)
		#	l.pack()
			matriz[0].insert(0,Button(m,text=(x,y)))
			matriz[0][0].pack(fill=BOTH, side=RIGHT)
			sleep(espera/(x*y))
		#	print(x,y)
			x -= 1
		y -= 1
		x = n
	return matriz

def iniciar (mestre, x=16,y=None,*imolados,tempo=0.55,nome="About n [Squares]"):
	for i in imolados:
		try:
			i.destroy()
		except Exception:
			print('\t\aA destruição de %s não foi possível!'%str(i))
#	for l in xadrez(mestre,x,y,tempo):
#		for q in l:
#			q.config(bg='WHITE')
	Thread(None, xadrez, None, (mestre,x,y,tempo)).start()
	print(imolados)
	mestre.title(nome)

a = Tk()
#a.config(bg='WHITE')
a.title("About 2") #a História de n Quadrados
#a.attributes('-fullscreen', True)
#a.geometry('%dx%d' %(a.winfo_screenwidth()//2, a.winfo_screenheight()//2))
b = {'width':a.winfo_screenwidth()//9,'height':a.winfo_screenheight()//8,'master':a}
b = Frame(**b),Frame(**b)
Button(b[1],command=lambda: iniciar(a,32,16,*b),bg='RED').pack(fill=BOTH)
Button(b[0],command=a.quit, bg='BLACK').pack(fill=BOTH)
b[0].pack(side=RIGHT)
b[1].pack()
#Thread(None, xadrez, None, (a,)).start()
a.mainloop()
