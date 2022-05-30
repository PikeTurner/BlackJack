from classi.carte import Mazzo
from classi.giocatore import Giocatore

class Banco():

    __nome = 'Banco'
    __mazzo = None

    def __init__(self,numero_carte):
        super().__init__('Banco', 1)
        self.__mazzo = Mazzo(numero_carte)
        
    #METODO PER L'ESTRAZIONE DELLE CARTE DAL MAZZO
    def estrai(self):
        return self.__mazzo.get_Mazzo().pop(len(self.__mazzo.get_Mazzo())-1)    #Uso la funzioe pop

    def get_mazzo(self):
        return self.__mazzo.get_Mazzo()
    
    

    
    






