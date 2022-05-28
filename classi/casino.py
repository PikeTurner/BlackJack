import zmq
import json

from classi.tavolo import Tavolo


class Casino:
    __giocatori = []
    __tavoli = []

    def __init__(self) -> None:
        for i in range(5):
            porta = 8000+i
            self.__tavoli.append(Tavolo(str(porta, 6)))

        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.REP)
        self.__socket.bind("tcp://*:5555")



    def ricevi_giocatori(self):
        giocatore = self.__socket.recv_object()
        self.__giocatori.append(giocatore)

    def manda_tavoli(self):
        self.__socket.send_json(json.dumps(self.__tavoli))



    def get_giocatori(self):
        return self.__giocatori

    def get_tavoli(self):
        return self.__tavoli

    def set_giocatore(self, g):
        self.__giocatori.append(g)

    def set_tavolo(self, t):
        self.__tavoli.append(t)
    