from threading import Thread
from time import sleep
from tkinter import *

def xadrez (mestre, x=8,y=None):
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
			sleep(1/(x*y))
		#	print(x,y)
			x -= 1
		y -= 1
		x = n
	return matriz

a = Tk()
a.title("a História de n Quadrados")
#a.attributes('-fullscreen', True)
#a.geometry('%dx%d' %(a.winfo_screenwidth()//2, a.winfo_screenheight()//2))
Thread(None, xadrez, None, (a,32,16)).start()
a.mainloop()
