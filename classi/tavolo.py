class Tavolo:

    
    def __init__(self, giocatori):
        self.__giocatori = giocatori
        self.__scommesse = {}
        self.__carte_totali = {}
        
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

