from classi.carte import Mazzo
from classi.giocatore import Giocatore

class Banco(Giocatore):

    __mazzo = None

    def __init__(self,numero_carte):
        super().__init__('Banco', 1)
        self.__mazzo = Mazzo(numero_carte)
        
    #METODO PER L'ESTRAZIONE DELLE CARTE DAL MAZZO
    def estrai(self):
        return self.__mazzo.get_Mazzo().pop(len(self.__mazzo.get_Mazzo())-1)    #Uso la funzioe pop

    def get_mazzo(self):
        return self.__mazzo.get_Mazzo()
    
    
    #METODO PER SOMMARE TUTTE LE CARTE DEL GIOCATORE
    def get_somma_carte_giocatore(self,giocatore):
        x = 0
        for i in self.get_carte_giocatore(giocatore):
            if i.get_numero() == 'J' or i.get_numero() == 'K' or i.get_numero() == 'Q':     #Le figure valgono sempre 10
                x += 10
            elif i.get_numero() == 'A':
                x += 11
            else:
                x += i.get_numero()
        if x > 21:                                                                          #L'asso assume il valore di 1 se con 11 sballa
            for i in self.get_carte_giocatore(giocatore):
                if i.get_numero() == 'A':
                    x -= 10
        return x
    
    
    #METODO PER IL CONFRONTO DEI RISULTATI DELLE CARTE DEI GIOCATORI A FINE GIOCO
    def confronto(self, giocatori, scommesse, carte):
        for i in range(len(giocatori)-1):
            if self.get_somma_carte_giocatore(giocatori[-1]) > 21 and giocatori[i].get_perso() == False:
                giocatori[i].set_soldi(giocatori[i].get_soldi() + scommesse[giocatori[i].get_id()]*2)
                print(giocatori[i].get_nome(),'  vinto')

            elif giocatori[i].get_perso() == True or self.get_somma_carte_giocatore(giocatori[-1]) > self.get_somma_carte_giocatore(giocatori[i]):
                print(giocatori[i].get_nome(),'  perso')

            elif self.get_somma_carte_giocatore(giocatori[-1]) == self.get_somma_carte_giocatore(giocatori[i]):
                giocatori[i].set_soldi(giocatori[i].get_soldi() + scommesse[giocatori[i].get_id()])
                print(giocatori[i].get_nome(),'  pari')

            elif self.get_somma_carte_giocatore(giocatori[-1]) < self.get_somma_carte_giocatore(giocatori[i]):
                giocatori[i].set_soldi(giocatori[i].get_soldi() + scommesse[giocatori[i].get_id()]*2)
                print(giocatori[i].get_nome(),'  vinto')

            elif self.get_somma_carte_giocatore(giocatori[-1]) == 21 and len(carte[giocatori[-1].get_id()]) == 2 and len(carte[giocatori[i].get_id()]) > 2:
                print(giocatori[i].get_nome(),'  perso')

            else:
                giocatori[i].set_soldi(giocatori[i].get_soldi() + scommesse[giocatori[i].get_id()]*2)
                print(giocatori[i].get_nome(),'  vinto')
        




