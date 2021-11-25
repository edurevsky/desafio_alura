from abc import ABCMeta, abstractmethod


"""
Os validadores serão usados apenas quando for implementado o sistema de interface
no terminal
"""

class Validador(metaclass=ABCMeta):
    @abstractmethod
    def valida(self):
        pass


class Cgm(Validador):

    def __init__(self, cgm):
        self.__cgm = cgm

    def valida(self):
        if str(self.__cgm) == 8:
            if int(self.__cgm):
                return True
        return False


class Email(Validador):

    def __init__(self, email):
        self.__email = email

    def valida(self):
        email = self.__email
        dominio = '@escola.pr.gov.br'
        if email == email.lower():
            if dominio in email:
                if ' ' not in email:
                    return True
        return False
