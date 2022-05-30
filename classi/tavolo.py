import zmq
import json

from classi.banco import Banco
from classi.gioco import Gioco


class Tavolo:
    
    def __init__(self, porta, posti):
        self.__context = zmq.Context()
        self.__socket = self.__context.socket(zmq.REP)
        self.__socket.bind("tcp://*:"+porta)

        self.__id = id(self)
        self.__posti_totali = posti
        self.__banco = Banco(52)
        self.__gioco = Gioco()
        self.__giocatori = []
        self.__scommesse = {}
        self.__carte_totali = {}


    def gioco(self):
        pass

    def ricevi_giocatore(self):
        giocatore = self.__socket.recv_object()
        self.__giocatori.append(giocatore)



    #METODO PER IL CONFRONTO DEI RISULTATI DELLE CARTE DEI GIOCATORI A FINE GIOCO
    def controllo_vincitori(self):
        for i in range(len(self.__giocatori)-1):
            if self.get_somma_carte_giocatore(self.__banco) > 21 and self.__giocatori[i].get_perso() == False:
                self.__giocatori[i].set_soldi(self.__giocatori[i].get_soldi() + self.__scommesse[self.__giocatori[i].get_id()]*2)
                print(self.__giocatori[i].get_nome(),'  vinto')

            elif self.__giocatori[i].get_perso() == True or self.get_somma_carte_giocatore(self.__giocatori[-1]) > self.get_somma_carte_giocatore(self.__giocatori[i]):
                print(self.__giocatori[i].get_nome(),'  perso')

            elif self.get_somma_carte_giocatore(self.__giocatori[-1]) == self.get_somma_carte_giocatore(self.__giocatori[i]):
                self.__giocatori[i].set_soldi(self.__giocatori[i].get_soldi() + self.__scommesse[self.__giocatori[i].get_id()])
                print(self.__giocatori[i].get_nome(),'  pari')

            elif self.get_somma_carte_giocatore(self.__giocatori[-1]) < self.get_somma_carte_giocatore(self.__giocatori[i]):
                self.__giocatori[i].set_soldi(self.__giocatori[i].get_soldi() + self.__scommesse[self.__giocatori[i].get_id()]*2)
                print(self.__giocatori[i].get_nome(),'  vinto')

            elif self.get_somma_carte_giocatore(self.__giocatori[-1]) == 21 and len(self.__carte[self.__giocatori[-1].get_id()]) == 2 and len(self.__carte[self.__giocatori[i].get_id()]) > 2:
                print(self.__giocatori[i].get_nome(),'  perso')

            else:
                self.__giocatori[i].set_soldi(self.__giocatori[i].get_soldi() + self.__scommesse[self.__giocatori[i].get_id()]*2)
                print(self.__giocatori[i].get_nome(),'  vinto')
        


        #METODO PER SOMMARE TUTTE LE CARTE DEL GIOCATORE
    def get_somma_carte_giocatore(self):
        x = 0
        for i in self.get_carte_giocatore(self.__giocatori):
            if i.get_numero() == 'J' or i.get_numero() == 'K' or i.get_numero() == 'Q':     #Le figure valgono sempre 10
                x += 10
            elif i.get_numero() == 'A':
                x += 11
            else:
                x += i.get_numero()
        if x > 21:                                                                          #L'asso assume il valore di 1 se con 11 sballa
            for i in self.get_carte_giocatore(self.__giocatori):
                if i.get_numero() == 'A':
                    x -= 10
        return x

    
        
    def get_carte(self):
        return self.__carte_totali

    def get_scommesse(self):
        return self.__scommesse
        
    def get_carte_giocatore(self,giocatore):
        return self.__carte_totali[giocatore.get_id()]
    
    
    def set_scommessa(self, giocatore, scommessa):
        self.__scommesse[giocatore.get_id()] = scommessa

    #FUNZIONE PER ASSEGNIARE LE CARTE ESTRATTE DAL BANCO AL GIOCATORE
    def set_carte(self, giocatore):
        if giocatore.get_id() in self.__carte_totali:   #Se il giocatore ha già almeno una carta gli viene assegnata una carta
            self.__carte_totali[giocatore.get_id()].append(self.__giocatori[-1].estrai())
        else:                                           #Al contrario gli viene assegniato un array con la carta
            self.__carte_totali[giocatore.get_id()] = [self.__giocatori[-1].estrai()]

