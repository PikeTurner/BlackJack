from threading import Thread
from banco import Banco
from casino import Casino



casino = Casino()
banco = Banco(4)


casino.ricevi_giocatori()
casino.manda_tavoli()
