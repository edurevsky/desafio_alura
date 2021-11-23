from abc import ABCMeta, abstractmethod


class Validador(metaclass=ABCMeta):
    @abstractmethod
    def valida(self):
        pass


class Cgm(Validador):

    def __init__(self, cgm):
        self.__cgm = cgm

    def valida(self):
        if len(str(self.__cgm)) == 8:
            if int(self.__cgm):
                return True
        return False


class Email(Validador):

    def __init__(self, email):
        self.__email = email

    def valida(self):
        dominio = '@escola.pr.gov.br'
        if dominio in self.__email:
            if ' ' not in self.__email:
                return True
        return False
