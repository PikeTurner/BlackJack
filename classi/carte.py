from random import random
import random

class Mazzo:
    __mazzo_carte = []
    def __init__(self, numero_carte):
        for i in range (1,numero_carte + 1, 1):
            self.__mazzo_carte.append(Quadri(i))
            self.__mazzo_carte.append(Picche(i))
            self.__mazzo_carte.append(Cuori(i))
            self.__mazzo_carte.append(Fiori(i))

        random.shuffle(self.__mazzo_carte)

    def get_Mazzo(self):
        return self.__mazzo_carte


class Carta:

    __seme = ""
    __numero = 0

    def get_seme(self):
        return self.__seme

    def __repr__(self):
        return str(self.__numero) + " di " + self.__seme

    def get_numero(self):
        return self.__numero

    def set_seme(self,seme):
        self.__seme = seme

    def set_numero(self,numero):
        self.__numero = numero

class Quadri(Carta):

    def __init__(self, numero):
        self.set_seme("Quadri")
        if numero == 11:
            self.set_numero('J')
        elif numero == 12:
            self.set_numero('Q')
        elif numero == 13:
            self.set_numero('K')
        elif numero == 1:
            self.set_numero('A')
        else:
            self.set_numero(numero)


class Fiori(Carta):

    def __init__(self, numero):
        self.set_seme("Fiori")
        if numero == 11:
            self.set_numero('J')
        elif numero == 12:
            self.set_numero('Q')
        elif numero == 13:
            self.set_numero('K')
        elif numero == 1:
            self.set_numero('A')
        else:
            self.set_numero(numero)


class Picche(Carta):

    def __init__(self, numero):
        self.set_seme("Picche")
        if numero == 11:
            self.set_numero('J')
        elif numero == 12:
            self.set_numero('Q')
        elif numero == 13:
            self.set_numero('K')
        elif numero == 1:
            self.set_numero('A')
        else:
            self.set_numero(numero)


class Cuori(Carta):

    def __init__(self, numero):
        self.set_seme("Cuori")
        if numero == 11:
            self.set_numero('J')
        elif numero == 12:
            self.set_numero('Q')
        elif numero == 13:
            self.set_numero('K')
        elif numero == 1:
            self.set_numero('A')
        else:
            self.set_numero(numero)
