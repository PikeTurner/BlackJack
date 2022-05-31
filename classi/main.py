from threading import Thread
from classi.banco import Banco
from classi.casino import Casino
from classi.giocatore import Giocatore



casino = Casino()
banco = Banco(52)
giocatore = Giocatore('Paolo', 1000)

casino.ricevi_giocatori()
giocatore.connetti_casino()

tavoli = giocatore.ricevi_lita_tavoli()

for t in tavoli:
    print(t)

'''
t = Thread(target=giocatore.connetti_tavolo, args=(giocatore.connetti_casino(),))
t.start()
'''