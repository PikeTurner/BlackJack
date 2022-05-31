from threading import Thread
from banco import Banco
from casino import Casino
from giocatore import Giocatore



giocatore = Giocatore('Paolo', 1000)

giocatore.connetti_casino()


tavoli = giocatore.ricevi_lita_tavoli()

for t in tavoli:
    print(t)
'''
t = Thread(target=giocatore.connetti_tavolo, args=(giocatore.connetti_casino(),))
t.start()
'''