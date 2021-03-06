import zmq
import json
import socket


class Giocatore:
    __id = 0
    __nome = ''
    __soldi = 0
    __turno = 0
    __perso = False

    def __init__(self,nome,soldi):
        self.__nome = nome
        self.__soldi = soldi
        self.__id = id(self)
        self.__perso = False

        self.__context = zmq.Context()
        self.__sc = self.__context.socket(zmq.REQ)
        self.__sc.connect("tcp://localhost:5555")


    def connetti_casino(self):
        self.__sc.send_pyobj(self)


    def ricevi_lita_tavoli(self):
        self.__sc.send_string('tavoli')
        tavoli =json.loads(self.__sc.recv_json())

        return tavoli

    def connetti_tavolo(porta_tavolo):

        context = zmq.Context()
        sc = context.socket(zmq.REQ)
        sc.connect("tcp://localhost:" + porta_tavolo)
        
        sc.send_string("connesso alla porta 8000")
        message = sc.recv_string()
        print(message)

    #METODO PER STAMPARE LE SCELTE POSSIBILI
    def scelta(self):
        print('1 - Shtatt ferm')
        print('2 - Chiedi carta')
        if self.__turno == 0:   #È possibile raddoppiare solo il primo turno
            print('3 - Raddoppia')
        self.__turno = 1
        return int(input('Scegli mossa:  '))    #Il giocatore insersce la mossa voluta
    
    #METODO PER SETTARE LA SCOMMESSA
    def scommetti(self):
        scommessa = int(input(self.__nome + ' inserisci scommessa:  '))
        if scommessa <= self.__soldi:   #Controllo se ci sono abbastanza soldi
            self.__soldi -= scommessa
            return scommessa
        else:
            print('Non hai abbastanza soldi')
            self.scommetti()   #La funzione continua a chiedere la scommessa finché il valore non è giusto
    
    def get_perso(self):
        return self.__perso

    def get_soldi(self):
        return self.__soldi

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome

    def set_perso(self,x):
        self.__perso = x

    def set_nome(self, nome):
        self.__nome = nome

    def set_soldi(self, soldi):
        self.__soldi = soldi
