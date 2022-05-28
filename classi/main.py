from threading import Thread
from classi.giocatore import Giocatore


cl1 = Giocatore('Nikola', 1000)


t = Thread(target=cl1.connetti_tavolo, args=(cl1.connetti_casino(),))
t.start()