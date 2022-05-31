from threading import Thread
from classi.banco import Banco
from classi.casino import Casino
from classi.giocatore import Giocatore



casino = Casino()
banco = Banco(52)
cl1 = Giocatore('Paolo', 1000)


t = Thread(target=cl1.connetti_tavolo, args=(cl1.connetti_casino(),))
t.start()