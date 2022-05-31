from threading import Thread
from banco import Banco
from casino import Casino



casino = Casino()
banco = Banco(52)


casino.ricevi_giocatori()
casino.manda_tavoli()
