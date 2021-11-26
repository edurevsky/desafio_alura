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
        """Verifica se o CGM possui obrigatóriamente 8 dígitos
        
        e se é aplicável a um tipo int."""
        if len(str(self.__cgm)) == 8:
            if int(self.__cgm):
                return True
        return False


class Email(Validador):

    def __init__(self, email):
        self.__email = email

    def valida(self):
        """Verifica se o domínio '@escola.pr.gov.br' está presente no email;

        Verifica se o email está em lowercase;

        E verifica se não há espaços no email."""
        email = self.__email
        dominio = '@escola.pr.gov.br'
        if email == email.lower():
            if dominio in email:
                if ' ' not in email:
                    return True
        return False
