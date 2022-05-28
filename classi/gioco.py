


class Gioco:

    def __init__(self) -> None:
        self.__turno = 0

    def get_turno(self):
        return self.__turno
    
    def primo_turno(self, giocatore, banco):
        pass

    def chiedi_scommessa(self, giocatore):
        pass

    def manda_carta(self,banco):
        pass

    def singolo_turno(self,giocatore,banco):
        pass

    def chiedi_mossa(self,giocatore):
        pass

    def turno_banco(self,banco):
        pass

    def confronto(self,giocatori):
        pass

    def manda_risultato(self):
        self.confronto()